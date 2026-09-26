from sqlalchemy.orm import Session
from app.modules.users.model import User

def get_all_users(db: Session):
    return db.query(User).filter(User.is_deleted == False).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter( User.id == user_id, User.is_deleted == False ).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email, User.is_deleted == False).first()

def create_user(db: Session, user, hashed_password: str):
    new_user = User(username = user.username,
                    email = user.email,
                    hashed_password = hashed_password,
                    full_name = user.full_name,
                    phone = user.phone,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def update_user(db: Session, user_id: int, user):
    old_user = db.query(User).filter(User.id==user_id).first()
    if not old_user:
        return None
    old_user.full_name = user.full_name
    old_user.email = user.email
    old_user.phone = user.phone

    db.commit()
    db.refresh(old_user)

    return old_user

def delete_user(db: Session, user_id:int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.is_deleted = True
    db.commit()
    db.refresh(user)
    return user
