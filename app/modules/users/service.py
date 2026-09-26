from app.modules.users.repository import get_user_by_email, create_user, update_user, delete_user
from sqlalchemy.orm import Session
from app.modules.users.schema import UserResponse, Token, ChangePassword, UserUpdate
from fastapi import HTTPException
from app.core.security import hash_password, verify_password, create_access_token
from app.modules.users.model import User, UserRole
from app.modules.uploads.service import upload_image
import cloudinary.uploader

def register_user(db:Session, user)->UserResponse:
    existing_user = get_user_by_email(db, user.email)

    if existing_user is not None:
        raise HTTPException(
    status_code=400,
    detail="Email already exists"
)
    hashed_password = hash_password(user.password)
    new_user = create_user(db=db, user=user, hashed_password=hashed_password )

    return UserResponse.model_validate(new_user)

def login_user(db: Session, user)->Token:
    found_user = get_user_by_email(db, user.email)
    if found_user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    

    if not verify_password(user.password, found_user.hashed_password):
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    payload = {
         "sub": str(found_user.id),
         "email": found_user.email,
        "role": found_user.role,
    }
    token = create_access_token(payload)
    return Token(access_token=token, token_type="bearer")

def change_password(password: ChangePassword, db: Session, current_user ):
    if not verify_password(password.old_password, current_user.hashed_password):
        raise HTTPException(status_code=400, detail="Current password is incorrect")
    updated_password = hash_password(password.new_password)
    current_user.hashed_password = updated_password

    db.commit()
    db.refresh(current_user)

    return {
        "message":"Password changed successfully"
    }

def update_profile(db: Session, current_user, user: UserUpdate ):
    if current_user.email != user.email:
        existing_user = get_user_by_email(db, user.email)

        if existing_user is not None:
            raise HTTPException(status_code=400, detail="Invalid email")
    updated_user = update_user(db, current_user.id, user)
    return updated_user

def delete_user_service(db, user_id: int):
    user = delete_user(db, user_id)

    if not user:
        return {"message": "User not found"}

    return {"message": "User deleted successfully"}

async def update_avatar(
    db: Session,
    current_user: User,
    file
):
    # Upload avatar mới
    image = await upload_image(
        file=file,
        folder="shopapp/avatars"
    )

    # Xóa avatar cũ trên Cloudinary
    if current_user.avatar_public_id:
        cloudinary.uploader.destroy(
            current_user.avatar_public_id,
            resource_type="image"
        )

    # Cập nhật database
    current_user.avatar_url = image["url"]
    current_user.avatar_public_id = image["public_id"]

    db.commit()
    db.refresh(current_user)

    return current_user