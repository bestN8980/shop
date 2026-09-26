from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.rbac import require_role
from app.core.enums import UserRole

from app.modules.users.service import delete_user_service
from app.modules.users.repository import get_all_users
from app.modules.users.schema import Message, UserResponse


router = APIRouter(
    prefix="/admin/users",
    tags=["Admin Users"]
)


# GET ALL USERS (ADMIN ONLY)
@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user = Depends(require_role([UserRole.ADMIN]))
):
    return get_all_users(db)


# DELETE USER (SOFT DELETE)
@router.delete("/{user_id}", response_model=Message)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role([UserRole.ADMIN]))
):
    return delete_user_service(db, user_id)
