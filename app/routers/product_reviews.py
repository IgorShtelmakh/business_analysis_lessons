from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/product-reviews", tags=["Product Reviews"])


@router.get("/", response_model=list[schemas.ProductReviewRead])
def list_reviews(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.get_product_reviews(db, skip=skip, limit=limit)


@router.get("/{review_id}", response_model=schemas.ProductReviewRead)
def read_review(review_id: int, db: Session = Depends(get_db)):
    obj = crud.get_product_review(db, review_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Review not found")
    return obj


@router.post("/", response_model=schemas.ProductReviewRead, status_code=201)
def create_review(data: schemas.ProductReviewCreate, db: Session = Depends(get_db)):
    return crud.create_product_review(db, data)


@router.delete("/{review_id}", status_code=204)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    obj = crud.get_product_review(db, review_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Review not found")
    crud.delete_product_review(db, obj)
