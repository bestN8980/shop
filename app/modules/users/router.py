from fastapi import APIRouter, Depends, UploadFile, File
from app.modules.users.service import register_user, login_user, change_password, update_profile, delete_user_service
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.modules.users.schema import UserCreate, UserResponse, UserLogin, UserUpdate, ChangePassword, Token, Message
from app.dependencies.auth import get_current_user
from app.modules.users.model import User
from app.dependencies.rbac import require_role
from app.core.enums import UserRole
from app.modules.users.repository import get_all_users
from fastapi.security import OAuth2PasswordRequestForm
from app.modules.users.service import (
    register_user,
    login_user,
    change_password,
    update_profile,
    delete_user_service,
    update_avatar,
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserResponse, status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)

@router.post("/login", response_model=Token, status_code=200)
def login_route(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user)

@router.get("/me", response_model=UserResponse, status_code=200)
def display_info(current_user = Depends(require_role([UserRole.USER, UserRole.ADMIN]))):
    return current_user

@router.put("/me", response_model=UserResponse, status_code=200)
def update_info(user: UserUpdate, db: Session = Depends(get_db), current_user: User= Depends(get_current_user)):
    return update_profile(db,current_user, user)

@router.put("/change-password", response_model=Message, status_code=200)
def change_password_route(password: ChangePassword, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return change_password(password, db, current_user)

@router.get("/admin/users", response_model=list[UserResponse], status_code=200)
def get_all_users_route(current= Depends(require_role([UserRole.ADMIN])), db: Session = Depends(get_db)):
    return get_all_users(db)

@router.delete("/admin/users/{user_id}", response_model=Message, status_code=200)
def delete_user_route(user_id: int, db: Session = Depends(get_db), current_user = Depends(require_role([UserRole.ADMIN]))):
    return delete_user_service(db, user_id)

@router.post("/login/oauth2", response_model=Token, status_code=200)
def login_oauth2(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = UserLogin(
        email=form_data.username,
        password=form_data.password,
    )

    return login_user(db, user)

@router.put("/me/avatar", response_model=UserResponse)
async def update_avatar_route(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await update_avatar(
        db=db,
        current_user=current_user,
        file=file,
    )