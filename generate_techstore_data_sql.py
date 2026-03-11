"""
Скрипт генерації SQL-файлу для створення MySQL бази даних TechStore
Компанія: TechStore (інтернет-магазин електроніки)
Період: 2022-2024
"""

import random
from datetime import datetime, timedelta

# Налаштування
random.seed(42)

# Константи
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2024, 12, 31)
DB_NAME = 'techstore'

REGIONS = ['Київська', 'Львівська', 'Харківська', 'Дніпропетровська', 'Одеська']
CITIES = {
    'Київська': ['Київ', 'Бровари', 'Біла Церква', 'Вишневе'],
    'Львівська': ['Львів', 'Дрогобич', 'Стрий', 'Червоноград'],
    'Харківська': ['Харків', 'Лозова', 'Ізюм', 'Куп\'янськ'],
    'Дніпропетровська': ['Дніпро', 'Кривий Ріг', 'Нікополь', 'Павлоград'],
    'Одеська': ['Одеса', 'Чорноморськ', 'Южне', 'Білгород-Дністровський']
}


def escape_sql(value):
    """Екранування рядка для SQL."""
    if value is None:
        return 'NULL'
    if isinstance(value, bool):
        return '1' if value else '0'
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("\\", "\\\\").replace("'", "\\'") + "'"


def random_date(start=START_DATE, end=END_DATE, with_time=False):
    delta = (end - start).days
    dt = start + timedelta(
        days=random.randint(0, delta),
        hours=random.randint(0, 23) if with_time else 0,
        minutes=random.randint(0, 59) if with_time else 0,
        seconds=random.randint(0, 59) if with_time else 0
    )
    if with_time:
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    return dt.strftime('%Y-%m-%d')


def write_header(f):
    f.write("-- ============================================\n")
    f.write("-- TechStore MySQL Database\n")
    f.write("-- Інтернет-магазин електроніки\n")
    f.write("-- Період: 2022-2024\n")
    f.write("-- ============================================\n\n")
    f.write(f"DROP DATABASE IF EXISTS `{DB_NAME}`;\n")
    f.write(f"CREATE DATABASE `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;\n")
    f.write(f"USE `{DB_NAME}`;\n\n")
    f.write("SET NAMES utf8mb4;\n")
    f.write("SET FOREIGN_KEY_CHECKS = 0;\n\n")


def write_create_tables(f):
    f.write("-- ============================================\n")
    f.write("-- СТВОРЕННЯ ТАБЛИЦЬ\n")
    f.write("-- ============================================\n\n")

    # 1. customers
    f.write("""CREATE TABLE `customers` (
    `customer_id` INT NOT NULL AUTO_INCREMENT,
    `registration_date` DATE NOT NULL,
    `full_name` VARCHAR(200) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(20),
    `city` VARCHAR(100),
    `region` VARCHAR(100),
    `age` INT,
    `gender` CHAR(1),
    `customer_segment` ENUM('Premium', 'Standard', 'Budget') NOT NULL DEFAULT 'Standard',
    PRIMARY KEY (`customer_id`),
    INDEX `idx_customers_region` (`region`),
    INDEX `idx_customers_segment` (`customer_segment`),
    INDEX `idx_customers_city` (`city`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # 2. suppliers
    f.write("""CREATE TABLE `suppliers` (
    `supplier_id` INT NOT NULL AUTO_INCREMENT,
    `supplier_name` VARCHAR(200) NOT NULL,
    `country` VARCHAR(100),
    `contact_person` VARCHAR(200),
    `email` VARCHAR(100),
    `phone` VARCHAR(30),
    `rating` DECIMAL(2,1),
    `is_active` TINYINT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (`supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # 3. products
    f.write("""CREATE TABLE `products` (
    `product_id` INT NOT NULL AUTO_INCREMENT,
    `product_name` VARCHAR(300) NOT NULL,
    `category` VARCHAR(100) NOT NULL,
    `subcategory` VARCHAR(100),
    `brand` VARCHAR(100),
    `unit_price` DECIMAL(10,2) NOT NULL,
    `cost_price` DECIMAL(10,2) NOT NULL,
    `supplier_id` INT,
    `in_stock` INT NOT NULL DEFAULT 0,
    `is_active` TINYINT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (`product_id`),
    INDEX `idx_products_category` (`category`),
    INDEX `idx_products_brand` (`brand`),
    FOREIGN KEY (`supplier_id`) REFERENCES `suppliers`(`supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # 4. pickup_locations
    f.write("""CREATE TABLE `pickup_locations` (
    `location_id` INT NOT NULL AUTO_INCREMENT,
    `location_name` VARCHAR(200) NOT NULL,
    `city` VARCHAR(100),
    `region` VARCHAR(100),
    `address` VARCHAR(300),
    `open_date` DATE,
    `is_active` TINYINT(1) NOT NULL DEFAULT 1,
    `staff_count` INT DEFAULT 0,
    PRIMARY KEY (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # 5. orders
    f.write("""CREATE TABLE `orders` (
    `order_id` INT NOT NULL AUTO_INCREMENT,
    `customer_id` INT NOT NULL,
    `order_date` DATETIME NOT NULL,
    `shipping_date` DATETIME,
    `delivery_date` DATETIME,
    `order_status` ENUM('Delivered', 'Shipped', 'Pending', 'Cancelled', 'Returned') NOT NULL,
    `channel` ENUM('Website', 'Mobile App', 'Partner Store') NOT NULL,
    `pickup_location_id` INT,
    `payment_method` ENUM('Card', 'Cash', 'Online') NOT NULL,
    `discount_percent` INT NOT NULL DEFAULT 0,
    `shipping_cost` DECIMAL(10,2) NOT NULL DEFAULT 0,
    `total_amount` DECIMAL(12,2) NOT NULL DEFAULT 0,
    PRIMARY KEY (`order_id`),
    INDEX `idx_orders_customer` (`customer_id`),
    INDEX `idx_orders_date` (`order_date`),
    INDEX `idx_orders_status` (`order_status`),
    FOREIGN KEY (`customer_id`) REFERENCES `customers`(`customer_id`),
    FOREIGN KEY (`pickup_location_id`) REFERENCES `pickup_locations`(`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # 6. order_items
    f.write("""CREATE TABLE `order_items` (
    `order_item_id` INT NOT NULL AUTO_INCREMENT,
    `order_id` INT NOT NULL,
    `product_id` INT NOT NULL,
    `quantity` INT NOT NULL DEFAULT 1,
    `unit_price_at_sale` DECIMAL(10,2) NOT NULL,
    `discount_amount` DECIMAL(10,2) NOT NULL DEFAULT 0,
    `line_total` DECIMAL(12,2) NOT NULL,
    PRIMARY KEY (`order_item_id`),
    INDEX `idx_order_items_order` (`order_id`),
    INDEX `idx_order_items_product` (`product_id`),
    FOREIGN KEY (`order_id`) REFERENCES `orders`(`order_id`),
    FOREIGN KEY (`product_id`) REFERENCES `products`(`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # 7. marketing_campaigns
    f.write("""CREATE TABLE `marketing_campaigns` (
    `campaign_id` INT NOT NULL AUTO_INCREMENT,
    `campaign_name` VARCHAR(300) NOT NULL,
    `campaign_type` ENUM('Email', 'Social Media', 'Google Ads', 'Banner', 'SMS') NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE NOT NULL,
    `budget` DECIMAL(10,2) NOT NULL,
    `target_audience` VARCHAR(100),
    `impressions` INT DEFAULT 0,
    `clicks` INT DEFAULT 0,
    `conversions` INT DEFAULT 0,
    `revenue` DECIMAL(12,2) DEFAULT 0,
    `is_active` TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (`campaign_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # 8. customer_support
    f.write("""CREATE TABLE `customer_support` (
    `ticket_id` INT NOT NULL AUTO_INCREMENT,
    `customer_id` INT NOT NULL,
    `created_date` DATETIME NOT NULL,
    `issue_type` VARCHAR(100) NOT NULL,
    `priority` ENUM('Низький', 'Середній', 'Високий', 'Критичний') NOT NULL,
    `channel` ENUM('Email', 'Phone', 'Chat', 'Viber', 'Telegram') NOT NULL,
    `status` ENUM('Закрито', 'Відкрито', 'В обробці', 'Очікує відповіді клієнта') NOT NULL,
    `response_time_minutes` INT,
    `resolution_time_minutes` INT,
    `customer_rating` INT,
    PRIMARY KEY (`ticket_id`),
    INDEX `idx_support_customer` (`customer_id`),
    INDEX `idx_support_status` (`status`),
    FOREIGN KEY (`customer_id`) REFERENCES `customers`(`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # 9. website_traffic
    f.write("""CREATE TABLE `website_traffic` (
    `session_id` INT NOT NULL AUTO_INCREMENT,
    `visit_date` DATETIME NOT NULL,
    `page` VARCHAR(100) NOT NULL,
    `traffic_source` VARCHAR(50) NOT NULL,
    `device_type` ENUM('Desktop', 'Mobile', 'Tablet') NOT NULL,
    `browser` VARCHAR(50),
    `session_duration_seconds` INT DEFAULT 0,
    `pages_viewed` INT DEFAULT 0,
    `bounce` TINYINT(1) NOT NULL DEFAULT 0,
    `conversion` TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (`session_id`),
    INDEX `idx_traffic_date` (`visit_date`),
    INDEX `idx_traffic_source` (`traffic_source`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")

    # 10. product_reviews
    f.write("""CREATE TABLE `product_reviews` (
    `review_id` INT NOT NULL AUTO_INCREMENT,
    `product_id` INT NOT NULL,
    `customer_id` INT NOT NULL,
    `order_id` INT,
    `rating` INT NOT NULL,
    `review_text` TEXT,
    `review_date` DATE NOT NULL,
    `is_verified_purchase` TINYINT(1) NOT NULL DEFAULT 0,
    `helpful_votes` INT DEFAULT 0,
    PRIMARY KEY (`review_id`),
    INDEX `idx_reviews_product` (`product_id`),
    INDEX `idx_reviews_customer` (`customer_id`),
    FOREIGN KEY (`product_id`) REFERENCES `products`(`product_id`),
    FOREIGN KEY (`customer_id`) REFERENCES `customers`(`customer_id`),
    FOREIGN KEY (`order_id`) REFERENCES `orders`(`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n""")


def write_batch_insert(f, table, columns, rows, batch_size=1000):
    """Записує INSERT-и пакетами."""
    cols_str = ', '.join(f'`{c}`' for c in columns)
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i + batch_size]
        f.write(f"INSERT INTO `{table}` ({cols_str}) VALUES\n")
        lines = []
        for row in batch:
            values = ', '.join(escape_sql(v) for v in row)
            lines.append(f"({values})")
        f.write(',\n'.join(lines))
        f.write(';\n\n')


# ============================================
# ГЕНЕРАЦІЯ ДАНИХ
# ============================================

def generate_customers(n=15000):
    print(f"  Генерація {n} клієнтів...")
    first_names_male = ['Олександр', 'Іван', 'Петро', 'Дмитро', 'Сергій', 'Андрій',
                        'Володимир', 'Максим', 'Віктор', 'Олег', 'Юрій', 'Роман']
    first_names_female = ['Марія', 'Олена', 'Наталія', 'Анна', 'Тетяна', 'Катерина',
                          'Світлана', 'Ірина', 'Оксана', 'Людмила', 'Вікторія', 'Юлія']
    last_names = ['Іваненко', 'Коваленко', 'Петренко', 'Шевченко', 'Ткаченко',
                  'Бондаренко', 'Мельник', 'Кравченко', 'Василенко', 'Клименко',
                  'Павленко', 'Кузьменко', 'Савченко', 'Литвиненко', 'Семенченко']
    patronymics_male = ['Олександрович', 'Іванович', 'Петрович', 'Володимирович', 'Сергійович']
    patronymics_female = ['Олександрівна', 'Іванівна', 'Петрівна', 'Володимирівна', 'Сергіївна']

    columns = ['customer_id', 'registration_date', 'full_name', 'email', 'phone',
               'city', 'region', 'age', 'gender', 'customer_segment']
    rows = []

    for i in range(1, n + 1):
        region = random.choice(REGIONS)
        city = random.choice(CITIES[region])
        gender = random.choice(['М', 'Ж'])

        if gender == 'М':
            first_name = random.choice(first_names_male)
            patronymic = random.choice(patronymics_male)
        else:
            first_name = random.choice(first_names_female)
            patronymic = random.choice(patronymics_female)

        last_name = random.choice(last_names)
        full_name = f"{last_name} {first_name} {patronymic}"
        reg_date = random_date()
        email = f"user{i}@{'gmail.com' if i % 2 == 0 else 'ukr.net'}"
        phone = f"+38050{random.randint(1000000, 9999999)}"
        age = random.randint(18, 65)
        segment = random.choices(['Premium', 'Standard', 'Budget'], weights=[0.15, 0.60, 0.25])[0]

        rows.append((i, reg_date, full_name, email, phone, city, region, age, gender, segment))

    return columns, rows


def generate_suppliers(n=30):
    print(f"  Генерація {n} постачальників...")
    countries = ['Україна', 'Польща', 'Німеччина', 'Китай', 'США', 'Чехія']
    company_types = ['Ltd', 'Inc', 'GmbH', 'Corp', 'SA', 'UAB']

    columns = ['supplier_id', 'supplier_name', 'country', 'contact_person',
               'email', 'phone', 'rating', 'is_active']
    rows = []

    for i in range(101, 101 + n):
        country = random.choice(countries)
        company_type = random.choice(company_types)
        rows.append((
            i,
            f"TechSupply-{i} {company_type}",
            country,
            f"Contact Person {i}",
            f"supplier{i}@tech.com",
            f"+{random.choice([48, 49, 86, 380])}{random.randint(100000000, 999999999)}",
            round(random.uniform(3.5, 5.0), 1),
            random.choices([True, False], weights=[0.85, 0.15])[0]
        ))

    return columns, rows


def generate_products(n=500):
    print(f"  Генерація {n} товарів...")
    categories = {
        'Смартфони': {
            'brands': ['Apple', 'Samsung', 'Xiaomi', 'Google', 'OnePlus', 'Realme'],
            'price_range': (5000, 50000),
            'models': ['Pro Max', 'Ultra', 'Note', 'Plus', 'Lite', 'SE']
        },
        'Ноутбуки': {
            'brands': ['Apple', 'Dell', 'HP', 'Lenovo', 'ASUS', 'Acer', 'MSI'],
            'price_range': (15000, 70000),
            'models': ['ThinkPad', 'Inspiron', 'Pavilion', 'ZenBook', 'MacBook', 'Gaming']
        },
        'Планшети': {
            'brands': ['Apple', 'Samsung', 'Lenovo', 'Xiaomi', 'Huawei'],
            'price_range': (8000, 40000),
            'models': ['Tab', 'iPad', 'Pad', 'Tablet']
        },
        'Аксесуари': {
            'brands': ['Anker', 'Belkin', 'JBL', 'Sony', 'Logitech', 'Samsung'],
            'price_range': (200, 5000),
            'models': ['Wireless', 'Pro', 'Plus', 'Mini', 'Max']
        },
        'Побутова техніка': {
            'brands': ['Samsung', 'LG', 'Bosch', 'Philips', 'Xiaomi', 'Dyson'],
            'price_range': (3000, 30000),
            'models': ['Smart', 'Pro', 'Digital', 'Auto']
        }
    }

    columns = ['product_id', 'product_name', 'category', 'subcategory', 'brand',
               'unit_price', 'cost_price', 'supplier_id', 'in_stock', 'is_active']
    rows = []
    product_id = 1
    items_per_category = n // len(categories)

    for category, config in categories.items():
        for _ in range(items_per_category):
            brand = random.choice(config['brands'])
            model = random.choice(config['models'])
            price = random.randint(config['price_range'][0], config['price_range'][1])
            cost_price = int(price * random.uniform(0.65, 0.85))

            rows.append((
                product_id,
                f"{brand} {category[:-1]} {model}-{random.randint(100, 999)}",
                category,
                brand,
                brand,
                price,
                cost_price,
                random.randint(101, 130),
                random.randint(0, 100),
                random.choices([True, False], weights=[0.85, 0.15])[0]
            ))
            product_id += 1

    return columns, rows


def generate_pickup_locations():
    print(f"  Генерація пунктів видачі...")
    columns = ['location_id', 'location_name', 'city', 'region', 'address',
               'open_date', 'is_active', 'staff_count']

    rows = [
        (1, 'Київ Центр', 'Київ', 'Київська', 'вул. Хрещатик 22', '2022-01-01', True, 5),
        (2, 'Київ Позняки', 'Київ', 'Київська', 'просп. Бажана 10', '2022-03-15', True, 4),
        (3, 'Львів Площа Ринок', 'Львів', 'Львівська', 'пл. Ринок 1', '2022-02-01', True, 3),
        (4, 'Львів Сихів', 'Львів', 'Львівська', 'вул. Наукова 5', '2022-06-10', True, 3),
        (5, 'Харків Центр', 'Харків', 'Харківська', 'вул. Сумська 45', '2022-01-20', True, 4),
        (6, 'Харків Салтівка', 'Харків', 'Харківська', 'просп. Героїв Харкова 150', '2022-08-01', True, 3),
        (7, 'Дніпро Центр', 'Дніпро', 'Дніпропетровська', 'просп. Яворницького 23', '2022-02-15', True, 4),
        (8, 'Дніпро Сокол', 'Дніпро', 'Дніпропетровська', 'вул. Титова 1', '2022-09-01', True, 2),
        (9, 'Одеса Дерибасівська', 'Одеса', 'Одеська', 'вул. Дерибасівська 15', '2022-03-01', True, 3),
        (10, 'Одеса Аркадія', 'Одеса', 'Одеська', 'Французький бульвар 60', '2022-07-15', True, 2),
        (11, 'Кривий Ріг', 'Кривий Ріг', 'Дніпропетровська', 'просп. Миру 15', '2023-01-10', True, 2),
        (12, 'Біла Церква', 'Біла Церква', 'Київська', 'пл. Соборна 3', '2023-05-01', True, 2),
    ]

    return columns, rows


def generate_orders(customer_ids, n=80000):
    print(f"  Генерація {n} замовлень...")
    channels = ['Website', 'Mobile App', 'Partner Store']
    statuses = ['Delivered', 'Shipped', 'Pending', 'Cancelled', 'Returned']
    payment_methods = ['Card', 'Cash', 'Online']

    columns = ['order_id', 'customer_id', 'order_date', 'shipping_date', 'delivery_date',
               'order_status', 'channel', 'pickup_location_id', 'payment_method',
               'discount_percent', 'shipping_cost', 'total_amount']
    rows = []
    order_meta = []  # (order_id, status, discount_percent, shipping_cost) for order_items

    for i in range(1, n + 1):
        customer_id = random.choice(customer_ids)
        order_date_dt = START_DATE + timedelta(
            days=random.randint(0, (END_DATE - START_DATE).days),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59)
        )

        status = random.choices(statuses, weights=[0.70, 0.12, 0.05, 0.10, 0.03])[0]

        shipping_date = None
        delivery_date = None
        if status in ['Delivered', 'Shipped', 'Returned']:
            shipping_date_dt = order_date_dt + timedelta(days=random.randint(1, 3))
            shipping_date = shipping_date_dt.strftime('%Y-%m-%d %H:%M:%S')
            if status in ['Delivered', 'Returned']:
                delivery_date_dt = shipping_date_dt + timedelta(days=random.randint(1, 7))
                delivery_date = delivery_date_dt.strftime('%Y-%m-%d %H:%M:%S')

        discount_percent = random.choices([0, 5, 10, 15, 20], weights=[0.5, 0.25, 0.15, 0.07, 0.03])[0]
        shipping_cost = random.choice([0, 50, 70, 100])
        pickup_location_id = random.randint(1, 12) if status != 'Cancelled' else None

        rows.append((
            i, customer_id, order_date_dt.strftime('%Y-%m-%d %H:%M:%S'),
            shipping_date, delivery_date, status,
            random.choice(channels), pickup_location_id,
            random.choice(payment_methods), discount_percent, shipping_cost, 0
        ))

        order_meta.append({
            'order_id': i,
            'status': status,
            'discount_percent': discount_percent,
            'shipping_cost': shipping_cost
        })

        if i % 10000 == 0:
            print(f"    Оброблено {i}/{n} замовлень...")

    return columns, rows, order_meta


def generate_order_items(order_meta, product_data, product_active_ids):
    print(f"  Генерація позицій замовлень...")
    columns = ['order_item_id', 'order_id', 'product_id', 'quantity',
               'unit_price_at_sale', 'discount_amount', 'line_total']
    rows = []
    item_id = 1
    order_totals = {}

    # Build price lookup
    price_lookup = {}
    for row in product_data:
        price_lookup[row[0]] = row[5]  # product_id -> unit_price

    for idx, order in enumerate(order_meta):
        if order['status'] == 'Cancelled':
            order_totals[order['order_id']] = 0
            continue

        items_count = random.choices([1, 2, 3, 4, 5], weights=[0.50, 0.30, 0.12, 0.06, 0.02])[0]
        selected = random.sample(product_active_ids, min(items_count, len(product_active_ids)))
        order_total = 0

        for product_id in selected:
            quantity = random.randint(1, 3)
            unit_price = price_lookup[product_id]
            discount_amount = round(unit_price * (order['discount_percent'] / 100) * quantity, 2)
            line_total = round((unit_price * quantity) - discount_amount, 2)
            order_total += line_total

            rows.append((item_id, order['order_id'], product_id, quantity,
                         unit_price, discount_amount, line_total))
            item_id += 1

        order_totals[order['order_id']] = round(order_total + order['shipping_cost'], 2)

        if (idx + 1) % 10000 == 0:
            print(f"    Оброблено {idx + 1}/{len(order_meta)} замовлень...")

    return columns, rows, order_totals


def generate_marketing_campaigns(n=150):
    print(f"  Генерація {n} маркетингових кампаній...")
    campaign_types = ['Email', 'Social Media', 'Google Ads', 'Banner', 'SMS']
    targets = ['Всі клієнти', 'Premium', 'Standard', 'Budget', 'Нові клієнти']

    columns = ['campaign_id', 'campaign_name', 'campaign_type', 'start_date', 'end_date',
               'budget', 'target_audience', 'impressions', 'clicks', 'conversions',
               'revenue', 'is_active']
    rows = []

    for i in range(1, n + 1):
        start_date_dt = START_DATE + timedelta(days=random.randint(0, (END_DATE - START_DATE).days))
        duration = random.randint(7, 30)
        end_date_dt = start_date_dt + timedelta(days=duration)

        budget = random.randint(5000, 50000)
        impressions = random.randint(10000, 500000)
        clicks = int(impressions * random.uniform(0.01, 0.08))
        conversions = int(clicks * random.uniform(0.02, 0.15))
        revenue = round(conversions * random.uniform(3000, 15000), 2)

        campaign_name = f"Кампанія {i} - {random.choice(['Розпродаж', 'Новинки', 'Знижки', 'Акція'])}"

        rows.append((
            i, campaign_name, random.choice(campaign_types),
            start_date_dt.strftime('%Y-%m-%d'), end_date_dt.strftime('%Y-%m-%d'),
            budget, random.choice(targets), impressions, clicks, conversions, revenue,
            end_date_dt > datetime.now()
        ))

    return columns, rows


def generate_customer_support(customer_ids, n=5000):
    print(f"  Генерація {n} звернень в підтримку...")
    issue_types = ['Технічна проблема', 'Питання про товар', 'Повернення', 'Доставка',
                   'Оплата', 'Гарантія', 'Інше']
    statuses = ['Закрито', 'Відкрито', 'В обробці', 'Очікує відповіді клієнта']
    channels = ['Email', 'Phone', 'Chat', 'Viber', 'Telegram']
    priorities = ['Низький', 'Середній', 'Високий', 'Критичний']

    columns = ['ticket_id', 'customer_id', 'created_date', 'issue_type', 'priority',
               'channel', 'status', 'response_time_minutes', 'resolution_time_minutes',
               'customer_rating']
    rows = []

    for i in range(1, n + 1):
        created_date = random_date(with_time=True)
        status = random.choices(statuses, weights=[0.75, 0.10, 0.10, 0.05])[0]
        response_time = random.randint(10, 240) if status != 'Відкрито' else None
        resolution_time = random.randint(30, 1440) if status == 'Закрито' else None
        rating = random.randint(1, 5) if status == 'Закрито' else None

        rows.append((
            i, random.choice(customer_ids), created_date,
            random.choice(issue_types),
            random.choices(priorities, weights=[0.40, 0.35, 0.20, 0.05])[0],
            random.choice(channels), status,
            response_time, resolution_time, rating
        ))

    return columns, rows


def generate_website_traffic(n=500000):
    print(f"  Генерація {n} записів трафіку...")
    pages = ['Головна', 'Каталог', 'Товар', 'Кошик', 'Оформлення', 'Профіль', 'Контакти']
    sources = ['Direct', 'Google', 'Facebook', 'Instagram', 'Email', 'Referral']
    devices = ['Desktop', 'Mobile', 'Tablet']
    browsers = ['Chrome', 'Safari', 'Firefox', 'Edge', 'Opera']

    columns = ['session_id', 'visit_date', 'page', 'traffic_source', 'device_type',
               'browser', 'session_duration_seconds', 'pages_viewed', 'bounce', 'conversion']
    rows = []

    for i in range(1, n + 1):
        visit_date = random_date(with_time=True)
        session_duration = random.randint(10, 1800)
        pages_viewed = random.randint(1, 20)

        rows.append((
            i, visit_date, random.choice(pages),
            random.choices(sources, weights=[0.25, 0.30, 0.15, 0.15, 0.10, 0.05])[0],
            random.choices(devices, weights=[0.45, 0.45, 0.10])[0],
            random.choice(browsers), session_duration, pages_viewed,
            pages_viewed == 1,
            random.random() < 0.03
        ))

        if i % 50000 == 0:
            print(f"    Оброблено {i}/{n} записів...")

    return columns, rows


def generate_product_reviews(customer_ids, product_ids, delivered_order_ids, n=12000):
    print(f"  Генерація {n} відгуків...")
    review_texts_positive = [
        'Чудовий товар, рекомендую!',
        'Все чудово, швидка доставка',
        'Якість відмінна, дякую',
        'Дуже задоволений покупкою',
        'Все як на фото, супер!'
    ]
    review_texts_negative = [
        'Не відповідає опису',
        'Якість не дуже',
        'Довго йшла доставка',
        'Очікував кращого',
        'Є нарікання'
    ]

    columns = ['review_id', 'product_id', 'customer_id', 'order_id', 'rating',
               'review_text', 'review_date', 'is_verified_purchase', 'helpful_votes']
    rows = []

    for i in range(1, n + 1):
        rating = random.choices([1, 2, 3, 4, 5], weights=[0.05, 0.08, 0.15, 0.35, 0.37])[0]
        review_text = random.choice(review_texts_positive if rating >= 4 else review_texts_negative)
        review_date = random_date()

        rows.append((
            i, random.choice(product_ids), random.choice(customer_ids),
            random.choice(delivered_order_ids) if delivered_order_ids else None,
            rating, review_text, review_date,
            random.random() < 0.85,
            random.randint(0, 50)
        ))

    return columns, rows


def main():
    print("=" * 60)
    print("ГЕНЕРАЦІЯ SQL-ФАЙЛУ ДЛЯ TECHSTORE")
    print("=" * 60)

    output_file = 'techstore_database.sql'

    # Generate all data
    cust_cols, cust_rows = generate_customers(15000)
    customer_ids = [r[0] for r in cust_rows]

    supp_cols, supp_rows = generate_suppliers(30)

    prod_cols, prod_rows = generate_products(500)
    product_ids = [r[0] for r in prod_rows]
    product_active_ids = [r[0] for r in prod_rows if r[9]]  # is_active == True

    loc_cols, loc_rows = generate_pickup_locations()

    ord_cols, ord_rows, order_meta = generate_orders(customer_ids, 80000)

    oi_cols, oi_rows, order_totals = generate_order_items(order_meta, prod_rows, product_active_ids)

    # Update order total_amount
    updated_ord_rows = []
    for row in ord_rows:
        order_id = row[0]
        total = order_totals.get(order_id, 0)
        updated_ord_rows.append(row[:11] + (total,))
    ord_rows = updated_ord_rows

    camp_cols, camp_rows = generate_marketing_campaigns(150)

    supp_ticket_cols, supp_ticket_rows = generate_customer_support(customer_ids, 5000)

    traffic_cols, traffic_rows = generate_website_traffic(500000)

    delivered_order_ids = [m['order_id'] for m in order_meta if m['status'] == 'Delivered']
    rev_cols, rev_rows = generate_product_reviews(customer_ids, product_ids, delivered_order_ids, 12000)

    # Write SQL file
    print(f"\n  Запис у файл {output_file}...")

    with open(output_file, 'w', encoding='utf-8') as f:
        write_header(f)
        write_create_tables(f)

        f.write("-- ============================================\n")
        f.write("-- ЗАПОВНЕННЯ ДАНИМИ\n")
        f.write("-- ============================================\n\n")

        print("  Запис клієнтів...")
        f.write("-- Клієнти\n")
        write_batch_insert(f, 'customers', cust_cols, cust_rows)

        print("  Запис постачальників...")
        f.write("-- Постачальники\n")
        write_batch_insert(f, 'suppliers', supp_cols, supp_rows)

        print("  Запис товарів...")
        f.write("-- Товари\n")
        write_batch_insert(f, 'products', prod_cols, prod_rows)

        print("  Запис пунктів видачі...")
        f.write("-- Пункти видачі\n")
        write_batch_insert(f, 'pickup_locations', loc_cols, loc_rows)

        print("  Запис замовлень...")
        f.write("-- Замовлення\n")
        write_batch_insert(f, 'orders', ord_cols, ord_rows)

        print("  Запис позицій замовлень...")
        f.write("-- Позиції замовлень\n")
        write_batch_insert(f, 'order_items', oi_cols, oi_rows)

        print("  Запис маркетингових кампаній...")
        f.write("-- Маркетингові кампанії\n")
        write_batch_insert(f, 'marketing_campaigns', camp_cols, camp_rows)

        print("  Запис звернень в підтримку...")
        f.write("-- Звернення в підтримку\n")
        write_batch_insert(f, 'customer_support', supp_ticket_cols, supp_ticket_rows)

        print("  Запис трафіку сайту...")
        f.write("-- Трафік сайту\n")
        write_batch_insert(f, 'website_traffic', traffic_cols, traffic_rows)

        print("  Запис відгуків...")
        f.write("-- Відгуки на товари\n")
        write_batch_insert(f, 'product_reviews', rev_cols, rev_rows)

        f.write("SET FOREIGN_KEY_CHECKS = 1;\n\n")
        f.write("-- ============================================\n")
        f.write("-- ГОТОВО!\n")
        f.write("-- ============================================\n")

    # Stats
    print("\n" + "=" * 60)
    print("СТАТИСТИКА")
    print("=" * 60)
    print(f"Клієнти:                {len(cust_rows):,}")
    print(f"Товари:                 {len(prod_rows):,}")
    print(f"Постачальники:          {len(supp_rows):,}")
    print(f"Пункти видачі:          {len(loc_rows):,}")
    print(f"Замовлення:             {len(ord_rows):,}")
    print(f"Позиції замовлень:      {len(oi_rows):,}")
    print(f"Маркетингові кампанії:  {len(camp_rows):,}")
    print(f"Звернення в підтримку:  {len(supp_ticket_rows):,}")
    print(f"Записи трафіку:         {len(traffic_rows):,}")
    print(f"Відгуки на товари:      {len(rev_rows):,}")
    print("=" * 60)
    print(f"\nФайл збережено: {output_file}")
    print("Генерація завершена успішно!")


if __name__ == "__main__":
    main()
