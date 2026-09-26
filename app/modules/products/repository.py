from sqlalchemy.orm import Session
from app.modules.products.model import Product

def get_all_product(db: Session):
    return db.query(Product).filter(Product.is_deleted == False).all()

def get_product_by_id(db:Session, product_id:int):
    return db.query(Product).filter((Product.id == product_id) & (Product.is_deleted == False)).first()

def get_product_by_name(db: Session, product_name:str):
    return db.query(Product).filter(Product.name == product_name, Product.is_deleted == False).first()

def get_product_by_category_id(db: Session, category_id):
    return db.query(Product).filter((Product.category_id == category_id) & (Product.is_deleted == False)).all()

def create_product(
    db: Session,
    product,
    image_url: str | None = None,
    image_public_id: str | None = None
):
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        category_id=product.category_id,
        image_url=image_url,
        image_public_id=image_public_id
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

def update_product(db: Session, product, product_id):
    found_product = get_product_by_id(db, product_id)
    
    found_product.name = product.name
    found_product.description = product.description
    found_product.price = product.price
    found_product.stock = product.stock
    found_product.category_id = product.category_id

    db.commit()
    db.refresh(found_product)

    return found_product

def delete_product(db: Session, product_id: int):
    found_product = get_product_by_id(db, product_id)
    if found_product is None:
        return None
    
    found_product.is_deleted = True

    db.commit()
    db.refresh(found_product)   

    return found_product

