from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.modules.orders import service, schema
from app.modules.orders.schema import OrderCreate
from app.modules.users.model import User

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/")
def create_order_route(
    data: OrderCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return service.create_order(db, user.id, data.cart_id)


@router.get("/")
def get_my_orders(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return service.get_orders(db, user.id)  