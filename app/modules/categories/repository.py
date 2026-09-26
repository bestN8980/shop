from sqlalchemy.orm import Session
from app.modules.categories.model import Category

def get_all_categories(db: Session):
    return db.query(Category).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_category_by_name(db: Session, name: str):
    return db.query(Category).filter(Category.name == name).first()

def create_category(db: Session, category):
    new_category = Category(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def update_category(db: Session, category_id: int, category):
    found = get_category_by_id(db, category_id)
    if not found:
        return None

    found.name = category.name
    db.commit()
    db.refresh(found)
    return found

def delete_category(db: Session, category_id: int):
    found = get_category_by_id(db, category_id)
    if not found:
        return None

    db.delete(found)
    db.commit()
    return True