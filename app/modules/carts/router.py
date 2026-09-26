from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.modules.carts.schema import CartResponse, CartItemCreate
from app.modules.carts import service

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.get("/", response_model=CartResponse)
def get_cart(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return service.get_cart_detail(db, user.id)


@router.post("/items", response_model=CartResponse)
def add_to_cart(
    data: CartItemCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    service.add_to_cart(
        db,
        user.id,
        data.product_id,
        data.quantity
    )

    return service.get_cart_detail(db, user.id)


@router.delete("/items/{item_id}")
def remove_item(
    item_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    service.remove_from_cart(db, user.id, item_id)

    return service.get_cart_detail(db, user.id)