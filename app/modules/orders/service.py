from sqlalchemy.orm import Session
from app.modules.orders import repository
from app.modules.carts.model import Cart
from app.modules.products.model import Product
from fastapi import HTTPException


def create_order(db: Session, user_id: int, cart_id: int):

    cart = db.query(Cart).filter(
        Cart.id == cart_id,
        Cart.user_id == user_id
    ).first()

    if not cart:
        raise HTTPException(404, "Cart not found")

    if not cart.items:
        raise HTTPException(400, "Cart is empty")

    total = 0

    order = repository.create_order_record(db, user_id, 0)

    for item in cart.items:

        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()

        if not product:
            continue

        if product.stock < item.quantity:
            raise HTTPException(
                400,
                f"{product.name} is out of stock"
            )

        product.stock -= item.quantity

        subtotal = product.price * item.quantity
        total += subtotal

        repository.add_order_item(
            db,
            order.id,
            product.id,
            item.quantity,
            product.price
        )

    order.total_price = total

    db.commit()
    db.refresh(order)

    return order

def get_orders(db: Session, user_id: int):
    return repository.get_orders_by_user(db, user_id)


def get_order(db: Session, order_id: int):
    return repository.get_order_by_id(db, order_id)