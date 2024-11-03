from sqlalchemy.orm import Session
from app.models.product import Product, ProductStatus
from app.schemas.product import ProductCreate, ProductUpdate
from typing import Optional

def get_products(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    search: Optional[str] = None,
    category: Optional[str] = None
):
    query = db.query(Product)
    
    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))
    
    if category:
        query = query.filter(Product.category == category)
        
    return query.offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        price=product.price,
        sale_price=product.sale_price,
        description=product.description,
        stock=product.stock,
        image_url=product.image_url,
        category=product.category,
        status=ProductStatus.ACTIVE
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = get_product(db, product_id)
    if db_product:
        update_data = product.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return {"message": "Product successfully deleted"}
    return None