from sqlalchemy.orm import Session
from app.modules.carts.model import Cart, CartItem
from app.modules.products.model import Product

def get_cart_by_user(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).first()


def create_cart(db: Session, user_id: int):
    cart = Cart(user_id=user_id)
    db.add(cart)
    db.commit()
    db.refresh(cart)
    return cart


def add_item(db, cart, product_id, quantity):
    product = db.query(Product).filter(Product.id == product_id).first()

    item = CartItem(
        cart_id=cart.id,
        product_id=product_id,
        quantity=quantity,
        price=product.price   # 👈 lưu luôn giá
    )

    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_item_by_id(db: Session, item_id: int):
    # join sẵn Cart để service kiểm tra user_id mà không cần query thêm
    return (
        db.query(CartItem)
        .join(Cart, CartItem.cart_id == Cart.id)
        .filter(CartItem.id == item_id)
        .first()
    )


def remove_item(db: Session, item: CartItem):
    db.delete(item)
    db.commit()