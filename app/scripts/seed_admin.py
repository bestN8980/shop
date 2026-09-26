from sqlalchemy.orm import Session

from app.dependencies.database import SessionLocal
from app.modules.users.model import User
from app.core.security import hash_password


def create_admin(db: Session):
    admin = User(
        username="admin",
        email="admin@gmail.com",
        hashed_password=hash_password("123456"),
        full_name="Admin",
        phone="0000000000",
        role="ADMIN"
    )

    db.add(admin)
    db.commit()
    db.refresh(admin)

    print("Admin created successfully")


if __name__ == "__main__":
    db = SessionLocal()
    create_admin(db)
    db.close()