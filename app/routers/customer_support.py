from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/support-tickets", tags=["Customer Support"])


@router.get("/", response_model=list[schemas.CustomerSupportRead])
def list_tickets(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.get_support_tickets(db, skip=skip, limit=limit)


@router.get("/{ticket_id}", response_model=schemas.CustomerSupportRead)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    obj = crud.get_support_ticket(db, ticket_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return obj


@router.post("/", response_model=schemas.CustomerSupportRead, status_code=201)
def create_ticket(data: schemas.CustomerSupportCreate, db: Session = Depends(get_db)):
    return crud.create_support_ticket(db, data)


@router.put("/{ticket_id}", response_model=schemas.CustomerSupportRead)
def update_ticket(ticket_id: int, data: schemas.CustomerSupportCreate, db: Session = Depends(get_db)):
    obj = crud.get_support_ticket(db, ticket_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return crud.update_support_ticket(db, obj, data)


@router.delete("/{ticket_id}", status_code=204)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    obj = crud.get_support_ticket(db, ticket_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Ticket not found")
    crud.delete_support_ticket(db, obj)
