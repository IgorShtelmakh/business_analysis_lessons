from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/pickup-locations", tags=["Pickup Locations"])


@router.get("/", response_model=list[schemas.PickupLocationRead])
def list_pickup_locations(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.get_pickup_locations(db, skip=skip, limit=limit)


@router.get("/{location_id}", response_model=schemas.PickupLocationRead)
def read_pickup_location(location_id: int, db: Session = Depends(get_db)):
    obj = crud.get_pickup_location(db, location_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Pickup location not found")
    return obj


@router.post("/", response_model=schemas.PickupLocationRead, status_code=201)
def create_pickup_location(data: schemas.PickupLocationCreate, db: Session = Depends(get_db)):
    return crud.create_pickup_location(db, data)


@router.put("/{location_id}", response_model=schemas.PickupLocationRead)
def update_pickup_location(location_id: int, data: schemas.PickupLocationCreate, db: Session = Depends(get_db)):
    obj = crud.get_pickup_location(db, location_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Pickup location not found")
    return crud.update_pickup_location(db, obj, data)


@router.delete("/{location_id}", status_code=204)
def delete_pickup_location(location_id: int, db: Session = Depends(get_db)):
    obj = crud.get_pickup_location(db, location_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Pickup location not found")
    crud.delete_pickup_location(db, obj)
