from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/marketing-campaigns", tags=["Marketing Campaigns"])


@router.get("/", response_model=list[schemas.MarketingCampaignRead])
def list_campaigns(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.get_marketing_campaigns(db, skip=skip, limit=limit)


@router.get("/{campaign_id}", response_model=schemas.MarketingCampaignRead)
def read_campaign(campaign_id: int, db: Session = Depends(get_db)):
    obj = crud.get_marketing_campaign(db, campaign_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return obj


@router.post("/", response_model=schemas.MarketingCampaignRead, status_code=201)
def create_campaign(data: schemas.MarketingCampaignCreate, db: Session = Depends(get_db)):
    return crud.create_marketing_campaign(db, data)


@router.put("/{campaign_id}", response_model=schemas.MarketingCampaignRead)
def update_campaign(campaign_id: int, data: schemas.MarketingCampaignCreate, db: Session = Depends(get_db)):
    obj = crud.get_marketing_campaign(db, campaign_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return crud.update_marketing_campaign(db, obj, data)


@router.delete("/{campaign_id}", status_code=204)
def delete_campaign(campaign_id: int, db: Session = Depends(get_db)):
    obj = crud.get_marketing_campaign(db, campaign_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Campaign not found")
    crud.delete_marketing_campaign(db, obj)
