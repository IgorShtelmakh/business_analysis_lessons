from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    registration_date = Column(Date, nullable=False)
    full_name = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20))
    city = Column(String(100))
    region = Column(String(100))
    age = Column(Integer)
    gender = Column(String(1))
    customer_segment = Column(
        Enum("Premium", "Standard", "Budget"), nullable=False, server_default="Standard"
    )

    orders = relationship("Order", back_populates="customer")
    support_tickets = relationship("CustomerSupport", back_populates="customer")
    reviews = relationship("ProductReview", back_populates="customer")


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_name = Column(String(200), nullable=False)
    country = Column(String(100))
    contact_person = Column(String(200))
    email = Column(String(100))
    phone = Column(String(30))
    rating = Column(Numeric(2, 1))
    is_active = Column(Boolean, nullable=False, server_default="1")

    products = relationship("Product", back_populates="supplier")


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(300), nullable=False)
    category = Column(String(100), nullable=False)
    subcategory = Column(String(100))
    brand = Column(String(100))
    unit_price = Column(Numeric(10, 2), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"))
    in_stock = Column(Integer, nullable=False, server_default="0")
    is_active = Column(Boolean, nullable=False, server_default="1")

    supplier = relationship("Supplier", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
    reviews = relationship("ProductReview", back_populates="product")


class PickupLocation(Base):
    __tablename__ = "pickup_locations"

    location_id = Column(Integer, primary_key=True, autoincrement=True)
    location_name = Column(String(200), nullable=False)
    city = Column(String(100))
    region = Column(String(100))
    address = Column(String(300))
    open_date = Column(Date)
    is_active = Column(Boolean, nullable=False, server_default="1")
    staff_count = Column(Integer, server_default="0")

    orders = relationship("Order", back_populates="pickup_location")


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    order_date = Column(DateTime, nullable=False)
    shipping_date = Column(DateTime)
    delivery_date = Column(DateTime)
    order_status = Column(
        Enum("Delivered", "Shipped", "Pending", "Cancelled", "Returned"), nullable=False
    )
    channel = Column(
        Enum("Website", "Mobile App", "Partner Store"), nullable=False
    )
    pickup_location_id = Column(Integer, ForeignKey("pickup_locations.location_id"))
    payment_method = Column(Enum("Card", "Cash", "Online"), nullable=False)
    discount_percent = Column(Integer, nullable=False, server_default="0")
    shipping_cost = Column(Numeric(10, 2), nullable=False, server_default="0")
    total_amount = Column(Numeric(12, 2), nullable=False, server_default="0")

    customer = relationship("Customer", back_populates="orders")
    pickup_location = relationship("PickupLocation", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
    reviews = relationship("ProductReview", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False, server_default="1")
    unit_price_at_sale = Column(Numeric(10, 2), nullable=False)
    discount_amount = Column(Numeric(10, 2), nullable=False, server_default="0")
    line_total = Column(Numeric(12, 2), nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")


class MarketingCampaign(Base):
    __tablename__ = "marketing_campaigns"

    campaign_id = Column(Integer, primary_key=True, autoincrement=True)
    campaign_name = Column(String(300), nullable=False)
    campaign_type = Column(
        Enum("Email", "Social Media", "Google Ads", "Banner", "SMS"), nullable=False
    )
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    budget = Column(Numeric(10, 2), nullable=False)
    target_audience = Column(String(100))
    impressions = Column(Integer, server_default="0")
    clicks = Column(Integer, server_default="0")
    conversions = Column(Integer, server_default="0")
    revenue = Column(Numeric(12, 2), server_default="0")
    is_active = Column(Boolean, nullable=False, server_default="0")


class CustomerSupport(Base):
    __tablename__ = "customer_support"

    ticket_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    created_date = Column(DateTime, nullable=False)
    issue_type = Column(String(100), nullable=False)
    priority = Column(
        Enum("Низький", "Середній", "Високий", "Критичний"), nullable=False
    )
    channel = Column(
        Enum("Email", "Phone", "Chat", "Viber", "Telegram"), nullable=False
    )
    status = Column(
        Enum("Закрито", "Відкрито", "В обробці", "Очікує відповіді клієнта"),
        nullable=False,
    )
    response_time_minutes = Column(Integer)
    resolution_time_minutes = Column(Integer)
    customer_rating = Column(Integer)

    customer = relationship("Customer", back_populates="support_tickets")


class WebsiteTraffic(Base):
    __tablename__ = "website_traffic"

    session_id = Column(Integer, primary_key=True, autoincrement=True)
    visit_date = Column(DateTime, nullable=False)
    page = Column(String(100), nullable=False)
    traffic_source = Column(String(50), nullable=False)
    device_type = Column(Enum("Desktop", "Mobile", "Tablet"), nullable=False)
    browser = Column(String(50))
    session_duration_seconds = Column(Integer, server_default="0")
    pages_viewed = Column(Integer, server_default="0")
    bounce = Column(Boolean, nullable=False, server_default="0")
    conversion = Column(Boolean, nullable=False, server_default="0")


class ProductReview(Base):
    __tablename__ = "product_reviews"

    review_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    rating = Column(Integer, nullable=False)
    review_text = Column(Text)
    review_date = Column(Date, nullable=False)
    is_verified_purchase = Column(Boolean, nullable=False, server_default="0")
    helpful_votes = Column(Integer, server_default="0")

    product = relationship("Product", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")
    order = relationship("Order", back_populates="reviews")
