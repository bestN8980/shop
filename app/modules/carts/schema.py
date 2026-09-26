from pydantic import BaseModel, ConfigDict

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = 1



class CartItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: int
    subtotal: int

    model_config = ConfigDict(from_attributes=True)


class CartResponse(BaseModel):
    id: int
    user_id: int
    items: list[CartItemResponse]
    total_price: int | None = None

    model_config = ConfigDict(from_attributes=True)