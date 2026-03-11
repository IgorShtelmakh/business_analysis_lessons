from fastapi import Depends, FastAPI
from fastapi_mcp import FastApiMCP

from .auth import verify_token
from .routers import (
    ask,
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

app.include_router(customers.router, dependencies=[Depends(verify_token)])
app.include_router(suppliers.router, dependencies=[Depends(verify_token)])
app.include_router(products.router, dependencies=[Depends(verify_token)])
app.include_router(pickup_locations.router, dependencies=[Depends(verify_token)])
app.include_router(orders.router, dependencies=[Depends(verify_token)])
app.include_router(order_items.router, dependencies=[Depends(verify_token)])
app.include_router(marketing_campaigns.router, dependencies=[Depends(verify_token)])
app.include_router(customer_support.router, dependencies=[Depends(verify_token)])
app.include_router(website_traffic.router, dependencies=[Depends(verify_token)])
app.include_router(product_reviews.router, dependencies=[Depends(verify_token)])
app.include_router(ask.router, dependencies=[Depends(verify_token)])


mcp = FastApiMCP(app)
mcp.mount()


@app.get("/")
def root():
    return {"message": "TechStore API", "docs": "/docs"}
