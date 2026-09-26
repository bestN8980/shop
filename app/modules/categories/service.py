from sqlalchemy.orm import Session

from app.modules.categories import repository
from app.modules.categories.schema import (
    CategoryCreate,
    CategoryUpdate
)


def create_category_service(db: Session, category: CategoryCreate):
    return repository.create_category(db, category)


def update_category_service(
    db: Session,
    category_id: int,
    category: CategoryUpdate
):
    return repository.update_category(db, category_id, category)


def delete_category_service(db: Session, category_id: int):
    return repository.delete_category(db, category_id)