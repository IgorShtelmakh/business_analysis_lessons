from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from enum import Enum as PyEnum

from pydantic import BaseModel, ConfigDict, Field


# ── Customers ──────────────────────────────────────────────

class CustomerBase(BaseModel):
    registration_date: date
    full_name: str
    email: str
    phone: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = Field(None, max_length=1)
    customer_segment: str = "Standard"


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    model_config = ConfigDict(from_attributes=True)
    customer_id: int


# ── Suppliers ──────────────────────────────────────────────

class SupplierBase(BaseModel):
    supplier_name: str
    country: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    rating: Optional[Decimal] = None
    is_active: bool = True


class SupplierCreate(SupplierBase):
    pass


class SupplierRead(SupplierBase):
    model_config = ConfigDict(from_attributes=True)
    supplier_id: int


# ── Products ──────────────────────────────────────────────

class ProductBase(BaseModel):
    product_name: str
    category: str
    subcategory: Optional[str] = None
    brand: Optional[str] = None
    unit_price: Decimal
    cost_price: Decimal
    supplier_id: Optional[int] = None
    in_stock: int = 0
    is_active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    product_id: int


# ── Pickup Locations ──────────────────────────────────────

class PickupLocationBase(BaseModel):
    location_name: str
    city: Optional[str] = None
    region: Optional[str] = None
    address: Optional[str] = None
    open_date: Optional[date] = None
    is_active: bool = True
    staff_count: int = 0


class PickupLocationCreate(PickupLocationBase):
    pass


class PickupLocationRead(PickupLocationBase):
    model_config = ConfigDict(from_attributes=True)
    location_id: int


# ── Orders ────────────────────────────────────────────────

class OrderBase(BaseModel):
    customer_id: int
    order_date: datetime
    shipping_date: Optional[datetime] = None
    delivery_date: Optional[datetime] = None
    order_status: str
    channel: str
    pickup_location_id: Optional[int] = None
    payment_method: str
    discount_percent: int = 0
    shipping_cost: Decimal = Decimal("0")
    total_amount: Decimal = Decimal("0")


class OrderCreate(OrderBase):
    pass


class OrderRead(OrderBase):
    model_config = ConfigDict(from_attributes=True)
    order_id: int


# ── Order Items ───────────────────────────────────────────

class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int = 1
    unit_price_at_sale: Decimal
    discount_amount: Decimal = Decimal("0")
    line_total: Decimal


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemRead(OrderItemBase):
    model_config = ConfigDict(from_attributes=True)
    order_item_id: int


# ── Marketing Campaigns ──────────────────────────────────

class MarketingCampaignBase(BaseModel):
    campaign_name: str
    campaign_type: str
    start_date: date
    end_date: date
    budget: Decimal
    target_audience: Optional[str] = None
    impressions: int = 0
    clicks: int = 0
    conversions: int = 0
    revenue: Decimal = Decimal("0")
    is_active: bool = False


class MarketingCampaignCreate(MarketingCampaignBase):
    pass


class MarketingCampaignRead(MarketingCampaignBase):
    model_config = ConfigDict(from_attributes=True)
    campaign_id: int


# ── Customer Support ──────────────────────────────────────

class CustomerSupportBase(BaseModel):
    customer_id: int
    created_date: datetime
    issue_type: str
    priority: str
    channel: str
    status: str
    response_time_minutes: Optional[int] = None
    resolution_time_minutes: Optional[int] = None
    customer_rating: Optional[int] = None


class CustomerSupportCreate(CustomerSupportBase):
    pass


class CustomerSupportRead(CustomerSupportBase):
    model_config = ConfigDict(from_attributes=True)
    ticket_id: int


# ── Website Traffic ───────────────────────────────────────

class WebsiteTrafficBase(BaseModel):
    visit_date: datetime
    page: str
    traffic_source: str
    device_type: str
    browser: Optional[str] = None
    session_duration_seconds: int = 0
    pages_viewed: int = 0
    bounce: bool = False
    conversion: bool = False


class WebsiteTrafficCreate(WebsiteTrafficBase):
    pass


class WebsiteTrafficRead(WebsiteTrafficBase):
    model_config = ConfigDict(from_attributes=True)
    session_id: int


# ── Product Reviews ───────────────────────────────────────

class ProductReviewBase(BaseModel):
    product_id: int
    customer_id: int
    order_id: Optional[int] = None
    rating: int
    review_text: Optional[str] = None
    review_date: date
    is_verified_purchase: bool = False
    helpful_votes: int = 0


class ProductReviewCreate(ProductReviewBase):
    pass


class ProductReviewRead(ProductReviewBase):
    model_config = ConfigDict(from_attributes=True)
    review_id: int
