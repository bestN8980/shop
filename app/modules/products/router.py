from fastapi import APIRouter, Depends, Form, UploadFile, File
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.modules.products.service import (
    create_product_service,
    update_product_service,
    delete_product_service,
    get_all_product_service,
)
from app.modules.products.schema import ProductCreate, ProductResponse, ProductUpdate
from app.dependencies.rbac import require_role
from app.core.enums import UserRole

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse, status_code=201)
async def create_product(
    name: str = Form(...),
    description: str | None = Form(None),
    price: int = Form(...),
    stock: int = Form(...),
    category_id: int = Form(...),
    file: UploadFile | None = File(None),
    db: Session = Depends(get_db),
    admin=Depends(require_role([UserRole.ADMIN])),
):
    product = ProductCreate(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category_id=category_id,
    )

    return await create_product_service(
        db=db,
        product=product,
        file=file,
    )


@router.put("/{product_id}", response_model=ProductResponse, status_code=200)
def update_product(
    product: ProductUpdate,
    product_id: int,
    db: Session = Depends(get_db),
    admin=Depends(require_role([UserRole.ADMIN])),
):
    return update_product_service(db, product_id, product)


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    admin=Depends(require_role([UserRole.ADMIN])),
):
    return delete_product_service(db, product_id)


@router.get("/", response_model=list[ProductResponse], status_code=200)
def get_all_product_route(db: Session = Depends(get_db)):
    return get_all_product_service(db)