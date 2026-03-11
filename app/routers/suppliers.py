from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.get("/", response_model=list[schemas.SupplierRead])
def list_suppliers(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.get_suppliers(db, skip=skip, limit=limit)


@router.get("/{supplier_id}", response_model=schemas.SupplierRead)
def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    obj = crud.get_supplier(db, supplier_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return obj


@router.post("/", response_model=schemas.SupplierRead, status_code=201)
def create_supplier(data: schemas.SupplierCreate, db: Session = Depends(get_db)):
    return crud.create_supplier(db, data)


@router.put("/{supplier_id}", response_model=schemas.SupplierRead)
def update_supplier(supplier_id: int, data: schemas.SupplierCreate, db: Session = Depends(get_db)):
    obj = crud.get_supplier(db, supplier_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return crud.update_supplier(db, obj, data)


@router.delete("/{supplier_id}", status_code=204)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    obj = crud.get_supplier(db, supplier_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Supplier not found")
    crud.delete_supplier(db, obj)
