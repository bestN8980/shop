from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy import Enum

from app.core.enums import UserRole

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    full_name = Column(String(30), nullable=False)
    phone = Column(String(15), nullable=False)

    avatar_url = Column(String(1024), nullable=True)
    avatar_public_id = Column(String(512), nullable=True)

    role = Column(
        Enum(UserRole),
        nullable=False,
        default=UserRole.USER
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    is_deleted = Column(Boolean, default=False)