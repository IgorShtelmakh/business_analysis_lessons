# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational project for "Технології бізнес-аналітики" (Business Analytics Technologies) course. Contains a FastAPI REST API and data generators for TechStore — a fictional Ukrainian electronics e-commerce platform (2022–2024 period).

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the API server
uvicorn app.main:app --reload

# Generate test CSV data (outputs to data/)
python generate_techstore_data.py

# Generate MySQL SQL dump (outputs techstore_database.sql)
python generate_techstore_data_sql.py

# Import database
mysql -u root -p < techstore_database.sql
```

Swagger UI is at `/docs` when the server is running.

## Architecture

**Layered FastAPI app** with SQLAlchemy ORM over MySQL (`techstore` database, utf8mb4).

- `app/main.py` — FastAPI entry point, registers all 10 routers
- `app/database.py` — engine, session factory, `get_db()` dependency. Connection string from `DATABASE_URL` env var (default: `mysql+pymysql://root:password@localhost:3306/techstore`)
- `app/models.py` — 10 SQLAlchemy models with relationships: Customer, Supplier, Product, PickupLocation, Order, OrderItem, MarketingCampaign, CustomerSupport, WebsiteTraffic, ProductReview
- `app/schemas.py` — Pydantic Base/Create/Read schemas per model (uses `from_attributes=True`)
- `app/crud.py` — generic CRUD helpers (`_get_list`, `_get_by_id`, `_create`, `_update`, `_delete`) plus entity-specific functions
- `app/routers/` — one router per table, standard REST (GET list, GET by id, POST, PUT, DELETE) with pagination via `skip`/`limit` query params. Nested routes: `/orders/{id}/items`, `/products/{id}/reviews`

**Data generators** are standalone scripts (not part of the API):
- `generate_techstore_data.py` — uses pandas/numpy, outputs CSV files to `data/`
- `generate_techstore_data_sql.py` — pure Python, outputs a single `.sql` file with CREATE TABLE + batch INSERTs

## Key Conventions

- All UI-facing strings (enum values, support statuses, priorities) are in Ukrainian
- Database enums match exactly between SQL generator, SQLAlchemy models, and Pydantic schemas
- Primary keys follow the pattern `{table_singular}_id` (e.g., `customer_id`, `order_id`)
- Router URL prefixes use kebab-case (`/pickup-locations`, `/order-items`)
- No test suite exists yet
