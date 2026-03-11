from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/", response_model=list[schemas.OrderRead])
def list_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.get_orders(db, skip=skip, limit=limit)


@router.get("/{order_id}", response_model=schemas.OrderRead)
def read_order(order_id: int, db: Session = Depends(get_db)):
    obj = crud.get_order(db, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Order not found")
    return obj


@router.get("/{order_id}/items", response_model=list[schemas.OrderItemRead])
def list_order_items(order_id: int, db: Session = Depends(get_db)):
    obj = crud.get_order(db, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Order not found")
    return crud.get_order_items_by_order(db, order_id)


@router.post("/", response_model=schemas.OrderRead, status_code=201)
def create_order(data: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, data)


@router.put("/{order_id}", response_model=schemas.OrderRead)
def update_order(order_id: int, data: schemas.OrderCreate, db: Session = Depends(get_db)):
    obj = crud.get_order(db, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Order not found")
    return crud.update_order(db, obj, data)


@router.delete("/{order_id}", status_code=204)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    obj = crud.get_order(db, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Order not found")
    crud.delete_order(db, obj)
