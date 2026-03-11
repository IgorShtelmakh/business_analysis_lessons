from sqlalchemy.orm import Session

from . import models, schemas


# ── Generic helpers ───────────────────────────────────────

def _get_list(db: Session, model, skip: int, limit: int):
    return db.query(model).offset(skip).limit(limit).all()


def _get_by_id(db: Session, model, pk_column, pk_value):
    return db.query(model).filter(pk_column == pk_value).first()


def _create(db: Session, model, schema: dict):
    obj = model(**schema)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def _update(db: Session, db_obj, update_data: dict):
    for key, value in update_data.items():
        if value is not None:
            setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def _delete(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()


# ── Customers ─────────────────────────────────────────────

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return _get_list(db, models.Customer, skip, limit)


def get_customer(db: Session, customer_id: int):
    return _get_by_id(db, models.Customer, models.Customer.customer_id, customer_id)


def create_customer(db: Session, data: schemas.CustomerCreate):
    return _create(db, models.Customer, data.model_dump())


def update_customer(db: Session, db_obj, data: schemas.CustomerCreate):
    return _update(db, db_obj, data.model_dump(exclude_unset=True))


def delete_customer(db: Session, db_obj):
    _delete(db, db_obj)


# ── Suppliers ─────────────────────────────────────────────

def get_suppliers(db: Session, skip: int = 0, limit: int = 100):
    return _get_list(db, models.Supplier, skip, limit)


def get_supplier(db: Session, supplier_id: int):
    return _get_by_id(db, models.Supplier, models.Supplier.supplier_id, supplier_id)


def create_supplier(db: Session, data: schemas.SupplierCreate):
    return _create(db, models.Supplier, data.model_dump())


def update_supplier(db: Session, db_obj, data: schemas.SupplierCreate):
    return _update(db, db_obj, data.model_dump(exclude_unset=True))


def delete_supplier(db: Session, db_obj):
    _delete(db, db_obj)


# ── Products ──────────────────────────────────────────────

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return _get_list(db, models.Product, skip, limit)


def get_product(db: Session, product_id: int):
    return _get_by_id(db, models.Product, models.Product.product_id, product_id)


def create_product(db: Session, data: schemas.ProductCreate):
    return _create(db, models.Product, data.model_dump())


def update_product(db: Session, db_obj, data: schemas.ProductCreate):
    return _update(db, db_obj, data.model_dump(exclude_unset=True))


def delete_product(db: Session, db_obj):
    _delete(db, db_obj)


# ── Pickup Locations ──────────────────────────────────────

def get_pickup_locations(db: Session, skip: int = 0, limit: int = 100):
    return _get_list(db, models.PickupLocation, skip, limit)


def get_pickup_location(db: Session, location_id: int):
    return _get_by_id(db, models.PickupLocation, models.PickupLocation.location_id, location_id)


def create_pickup_location(db: Session, data: schemas.PickupLocationCreate):
    return _create(db, models.PickupLocation, data.model_dump())


def update_pickup_location(db: Session, db_obj, data: schemas.PickupLocationCreate):
    return _update(db, db_obj, data.model_dump(exclude_unset=True))


def delete_pickup_location(db: Session, db_obj):
    _delete(db, db_obj)


# ── Orders ────────────────────────────────────────────────

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return _get_list(db, models.Order, skip, limit)


def get_order(db: Session, order_id: int):
    return _get_by_id(db, models.Order, models.Order.order_id, order_id)


def create_order(db: Session, data: schemas.OrderCreate):
    return _create(db, models.Order, data.model_dump())


def update_order(db: Session, db_obj, data: schemas.OrderCreate):
    return _update(db, db_obj, data.model_dump(exclude_unset=True))


def delete_order(db: Session, db_obj):
    _delete(db, db_obj)


# ── Order Items ───────────────────────────────────────────

def get_order_items(db: Session, skip: int = 0, limit: int = 100):
    return _get_list(db, models.OrderItem, skip, limit)


def get_order_item(db: Session, order_item_id: int):
    return _get_by_id(db, models.OrderItem, models.OrderItem.order_item_id, order_item_id)


def get_order_items_by_order(db: Session, order_id: int):
    return db.query(models.OrderItem).filter(models.OrderItem.order_id == order_id).all()


def create_order_item(db: Session, data: schemas.OrderItemCreate):
    return _create(db, models.OrderItem, data.model_dump())


def delete_order_item(db: Session, db_obj):
    _delete(db, db_obj)


# ── Marketing Campaigns ──────────────────────────────────

def get_marketing_campaigns(db: Session, skip: int = 0, limit: int = 100):
    return _get_list(db, models.MarketingCampaign, skip, limit)


def get_marketing_campaign(db: Session, campaign_id: int):
    return _get_by_id(db, models.MarketingCampaign, models.MarketingCampaign.campaign_id, campaign_id)


def create_marketing_campaign(db: Session, data: schemas.MarketingCampaignCreate):
    return _create(db, models.MarketingCampaign, data.model_dump())


def update_marketing_campaign(db: Session, db_obj, data: schemas.MarketingCampaignCreate):
    return _update(db, db_obj, data.model_dump(exclude_unset=True))


def delete_marketing_campaign(db: Session, db_obj):
    _delete(db, db_obj)


# ── Customer Support ──────────────────────────────────────

def get_support_tickets(db: Session, skip: int = 0, limit: int = 100):
    return _get_list(db, models.CustomerSupport, skip, limit)


def get_support_ticket(db: Session, ticket_id: int):
    return _get_by_id(db, models.CustomerSupport, models.CustomerSupport.ticket_id, ticket_id)


def create_support_ticket(db: Session, data: schemas.CustomerSupportCreate):
    return _create(db, models.CustomerSupport, data.model_dump())


def update_support_ticket(db: Session, db_obj, data: schemas.CustomerSupportCreate):
    return _update(db, db_obj, data.model_dump(exclude_unset=True))


def delete_support_ticket(db: Session, db_obj):
    _delete(db, db_obj)


# ── Website Traffic ───────────────────────────────────────

def get_website_traffic(db: Session, skip: int = 0, limit: int = 100):
    return _get_list(db, models.WebsiteTraffic, skip, limit)


def get_website_traffic_session(db: Session, session_id: int):
    return _get_by_id(db, models.WebsiteTraffic, models.WebsiteTraffic.session_id, session_id)


def create_website_traffic(db: Session, data: schemas.WebsiteTrafficCreate):
    return _create(db, models.WebsiteTraffic, data.model_dump())


def delete_website_traffic(db: Session, db_obj):
    _delete(db, db_obj)


# ── Product Reviews ───────────────────────────────────────

def get_product_reviews(db: Session, skip: int = 0, limit: int = 100):
    return _get_list(db, models.ProductReview, skip, limit)


def get_product_review(db: Session, review_id: int):
    return _get_by_id(db, models.ProductReview, models.ProductReview.review_id, review_id)


def get_reviews_by_product(db: Session, product_id: int):
    return db.query(models.ProductReview).filter(models.ProductReview.product_id == product_id).all()


def create_product_review(db: Session, data: schemas.ProductReviewCreate):
    return _create(db, models.ProductReview, data.model_dump())


def delete_product_review(db: Session, db_obj):
    _delete(db, db_obj)
