from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String(512), nullable=False)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    category_id = Column(Integer,ForeignKey("categories.id"), nullable=False, index=True)
    image_url = Column(String(1024), nullable=True)
    image_public_id = Column(String(512), nullable=True)
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True),server_default= func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),server_default=func.now(), onupdate=func.now())

    #relationship
    category = relationship("Category", back_populates="products")

