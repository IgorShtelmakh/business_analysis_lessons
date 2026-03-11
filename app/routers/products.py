from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[schemas.ProductRead])
def list_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.get_products(db, skip=skip, limit=limit)


@router.get("/{product_id}", response_model=schemas.ProductRead)
def read_product(product_id: int, db: Session = Depends(get_db)):
    obj = crud.get_product(db, product_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Product not found")
    return obj


@router.post("/", response_model=schemas.ProductRead, status_code=201)
def create_product(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, data)


@router.put("/{product_id}", response_model=schemas.ProductRead)
def update_product(product_id: int, data: schemas.ProductCreate, db: Session = Depends(get_db)):
    obj = crud.get_product(db, product_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db, obj, data)


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    obj = crud.get_product(db, product_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Product not found")
    crud.delete_product(db, obj)


@router.get("/{product_id}/reviews", response_model=list[schemas.ProductReviewRead])
def list_product_reviews(product_id: int, db: Session = Depends(get_db)):
    obj = crud.get_product(db, product_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.get_reviews_by_product(db, product_id)
