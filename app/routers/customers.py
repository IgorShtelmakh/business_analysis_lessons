from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/", response_model=list[schemas.CustomerRead])
def list_customers(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.get_customers(db, skip=skip, limit=limit)


@router.get("/{customer_id}", response_model=schemas.CustomerRead)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    obj = crud.get_customer(db, customer_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Customer not found")
    return obj


@router.post("/", response_model=schemas.CustomerRead, status_code=201)
def create_customer(data: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, data)


@router.put("/{customer_id}", response_model=schemas.CustomerRead)
def update_customer(customer_id: int, data: schemas.CustomerCreate, db: Session = Depends(get_db)):
    obj = crud.get_customer(db, customer_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Customer not found")
    return crud.update_customer(db, obj, data)


@router.delete("/{customer_id}", status_code=204)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    obj = crud.get_customer(db, customer_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Customer not found")
    crud.delete_customer(db, obj)
