from fastapi import FastAPI

from .routers import (
    customer_support,
    customers,
    marketing_campaigns,
    order_items,
    orders,
    pickup_locations,
    product_reviews,
    products,
    suppliers,
    website_traffic,
)

app = FastAPI(
    title="TechStore API",
    description="API для інтернет-магазину електроніки TechStore",
    version="1.0.0",
)

app.include_router(customers.router)
app.include_router(suppliers.router)
app.include_router(products.router)
app.include_router(pickup_locations.router)
app.include_router(orders.router)
app.include_router(order_items.router)
app.include_router(marketing_campaigns.router)
app.include_router(customer_support.router)
app.include_router(website_traffic.router)
app.include_router(product_reviews.router)


@app.get("/")
def root():
    return {"message": "TechStore API", "docs": "/docs"}
