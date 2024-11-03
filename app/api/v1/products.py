from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/api/v1/products",
    tags=["products"]
)

@router.get("/", response_model=List[schemas.Product])
def read_products(
    skip: int = Query(0, description="Skip first N items"),
    limit: int = Query(100, description="Limit the number of items"),
    search: str = Query(None, description="Search in product names"),
    category: str = Query(None, description="Filter by category"),
    db: Session = Depends(get_db)
):
    products = crud.get_products(db, skip=skip, limit=limit, search=search, category=category)
    return products

@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int,
    product: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, product_id=product_id, product=product)

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    db_product = crud.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    result = crud.delete_product(db, product_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return result