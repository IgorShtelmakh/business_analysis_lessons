from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/website-traffic", tags=["Website Traffic"])


@router.get("/", response_model=list[schemas.WebsiteTrafficRead])
def list_traffic(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.get_website_traffic(db, skip=skip, limit=limit)


@router.get("/{session_id}", response_model=schemas.WebsiteTrafficRead)
def read_traffic_session(session_id: int, db: Session = Depends(get_db)):
    obj = crud.get_website_traffic_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Traffic session not found")
    return obj


@router.post("/", response_model=schemas.WebsiteTrafficRead, status_code=201)
def create_traffic_session(data: schemas.WebsiteTrafficCreate, db: Session = Depends(get_db)):
    return crud.create_website_traffic(db, data)


@router.delete("/{session_id}", status_code=204)
def delete_traffic_session(session_id: int, db: Session = Depends(get_db)):
    obj = crud.get_website_traffic_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Traffic session not found")
    crud.delete_website_traffic(db, obj)
