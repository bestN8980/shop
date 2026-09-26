from sqlalchemy.orm import Session
from app.modules.orders.model import Order, OrderItem


def create_order_record(db: Session, user_id: int, total_price: float):
    order = Order(
        user_id=user_id,
        total_price=total_price,
        status="PENDING"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def add_order_item(
    db: Session,
    order_id: int,
    product_id: int,
    quantity: int,
    price: float
):
    item = OrderItem(
        order_id=order_id,
        product_id=product_id,
        quantity=quantity,
        price=price
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def get_orders_by_user(db: Session, user_id: int):
    return (
        db.query(Order)
        .filter(Order.user_id == user_id)
        .all()
    )


def get_order_by_id(db: Session, order_id: int):
    return (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )