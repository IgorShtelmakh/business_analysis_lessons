from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/order-items", tags=["Order Items"])


@router.get("/", response_model=list[schemas.OrderItemRead])
def list_order_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.get_order_items(db, skip=skip, limit=limit)


@router.get("/{order_item_id}", response_model=schemas.OrderItemRead)
def read_order_item(order_item_id: int, db: Session = Depends(get_db)):
    obj = crud.get_order_item(db, order_item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Order item not found")
    return obj


@router.post("/", response_model=schemas.OrderItemRead, status_code=201)
def create_order_item(data: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return crud.create_order_item(db, data)


@router.delete("/{order_item_id}", status_code=204)
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    obj = crud.get_order_item(db, order_item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Order item not found")
    crud.delete_order_item(db, obj)
