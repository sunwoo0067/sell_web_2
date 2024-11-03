from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    price: float
    sale_price: Optional[float] = None
    description: Optional[str] = None
    stock: int = 0
    category: Optional[str] = None
    image_url: Optional[str] = None
    status: str = "active"

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True