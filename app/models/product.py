from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.sql import func
from app.models.base import Base
from enum import Enum as PyEnum

class ProductStatus(PyEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SOLD_OUT = "sold_out"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    price = Column(Float, nullable=False)
    sale_price = Column(Float)
    description = Column(String(1000))
    stock = Column(Integer, default=0)
    status = Column(String(20), default="active")
    image_url = Column(String(500))
    category = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())