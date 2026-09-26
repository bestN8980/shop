from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.modules.carts import repository
from app.modules.products.model import Product
from app.modules.carts.model import CartItem


def get_or_create_cart(db: Session, user_id: int):
    cart = repository.get_cart_by_user(db, user_id)
    if not cart:
        cart = repository.create_cart(db, user_id)
    return cart


def add_to_cart(db, user_id, product_id, quantity):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    cart = repository.get_cart_by_user(db, user_id)

    if not cart:
        cart = repository.create_cart(db, user_id)

    item = CartItem(
        cart_id=cart.id,   # ✅ OK
        product_id=product_id,
        quantity=quantity,
        price=product.price
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def remove_from_cart(db: Session, user_id: int, item_id: int):
    item = repository.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item không tồn tại")
    if item.cart.user_id != user_id:
        raise HTTPException(status_code=404, detail="Item không tồn tại")

    repository.remove_item(db, item)
    return {"message": "Đã xóa item khỏi giỏ hàng"}

def get_cart_detail(db: Session, user_id: int):
    cart = repository.get_cart_by_user(db, user_id)

    if not cart:
        cart = repository.create_cart(db, user_id)

    items = []
    total_price = 0

    for item in cart.items:
        subtotal = item.price * item.quantity

        items.append({
            "id": item.id,
            "product_id": item.product_id,
            "price": item.price,
            "quantity": item.quantity,
            "subtotal": subtotal
        })

        total_price += subtotal

    return {
        "id": cart.id,
        "user_id": cart.user_id,
        "items": items,
        "total_price": total_price
    }