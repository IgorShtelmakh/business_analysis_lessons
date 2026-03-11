# МЕТОДИЧНІ МАТЕРІАЛИ ДЛЯ ПРАКТИЧНИХ РОБІТ
## Курс "Технології бізнес-аналітики"

---

## ОПИС ТЕСТОВИХ ДАНИХ

### Загальна концепція

Для виконання всіх практичних робіт використовується єдиний набір даних, що імітує діяльність **інтернет-магазину електроніки "TechStore"**. Компанія працює в Україні, має онлайн-платформу та мережу пунктів видачі.

### Структура бізнесу TechStore:

- **Період діяльності**: 2022-2024 роки (3 роки історії)
- **Географія**: 5 регіонів України (Київська, Львівська, Харківська, Дніпропетровська, Одеська області)
- **Асортимент**: 5 категорій товарів (Смартфони, Ноутбуки, Планшети, Аксесуари, Побутова техніка)
- **Канали продажу**: Веб-сайт, Мобільний додаток, Партнерські магазини
- **Пункти видачі**: 12 локацій
- **Клієнтська база**: ~15,000 унікальних клієнтів
- **Обсяг транзакцій**: ~80,000 замовлень за 3 роки

---

## НАБІР ФАЙЛІВ ДАНИХ

### 1. **customers.csv** (Клієнти)
```
customer_id, registration_date, full_name, email, phone, city, region, age, gender, customer_segment
1, 2022-01-15, Іваненко Олег Петрович, ivanov@gmail.com, +380501234567, Київ, Київська, 34, М, Premium
2, 2022-01-18, Коваленко Марія Іванівна, kovalenko@ukr.net, +380672345678, Львів, Львівська, 28, Ж, Standard
...
```

**Поля:**
- customer_id (INTEGER) - унікальний ID клієнта
- registration_date (DATE) - дата реєстрації
- full_name (TEXT) - ПІБ
- email (TEXT) - електронна пошта
- phone (TEXT) - телефон
- city (TEXT) - місто
- region (TEXT) - область
- age (INTEGER) - вік
- gender (TEXT) - стать (М/Ж)
- customer_segment (TEXT) - сегмент (Premium/Standard/Budget)

**Обсяг:** ~15,000 записів

---

### 2. **products.csv** (Товари)
```
product_id, product_name, category, subcategory, brand, unit_price, cost_price, supplier_id, in_stock, is_active
1, iPhone 14 Pro 256GB, Смартфони, Apple, Apple, 42999, 35000, 101, 45, TRUE
2, Samsung Galaxy S23, Смартфони, Samsung, Samsung, 32999, 27000, 102, 23, TRUE
...
```

**Поля:**
- product_id (INTEGER) - ID товару
- product_name (TEXT) - назва товару
- category (TEXT) - категорія
- subcategory (TEXT) - підкатегорія
- brand (TEXT) - бренд
- unit_price (DECIMAL) - ціна продажу
- cost_price (DECIMAL) - собівартість
- supplier_id (INTEGER) - ID постачальника
- in_stock (INTEGER) - залишок на складі
- is_active (BOOLEAN) - чи активний товар

**Обсяг:** ~500 унікальних товарів

---

### 3. **orders.csv** (Замовлення)
```
order_id, customer_id, order_date, shipping_date, delivery_date, order_status, channel, pickup_location_id, payment_method, discount_percent, shipping_cost, total_amount
1, 234, 2022-01-16 14:23:11, 2022-01-17 09:00:00, 2022-01-19 16:45:00, Delivered, Website, 5, Card, 5, 50, 8250
2, 567, 2022-01-16 18:12:33, 2022-01-18 10:30:00, NULL, Cancelled, Mobile App, NULL, Cash, 0, 0, 0
...
```

**Поля:**
- order_id (INTEGER) - ID замовлення
- customer_id (INTEGER) - ID клієнта
- order_date (DATETIME) - дата/час створення
- shipping_date (DATETIME) - дата відправлення
- delivery_date (DATETIME) - дата отримання
- order_status (TEXT) - статус (Pending/Shipped/Delivered/Cancelled/Returned)
- channel (TEXT) - канал (Website/Mobile App/Partner Store)
- pickup_location_id (INTEGER) - пункт видачі
- payment_method (TEXT) - спосіб оплати (Card/Cash/Online)
- discount_percent (DECIMAL) - знижка %
- shipping_cost (DECIMAL) - вартість доставки
- total_amount (DECIMAL) - загальна сума

**Обсяг:** ~80,000 замовлень

---

### 4. **order_items.csv** (Позиції замовлень)
```
order_item_id, order_id, product_id, quantity, unit_price_at_sale, discount_amount, line_total
1, 1, 45, 2, 3999, 200, 7798
2, 1, 128, 1, 499, 25, 474
...
```

**Поля:**
- order_item_id (INTEGER) - ID позиції
- order_id (INTEGER) - ID замовлення
- product_id (INTEGER) - ID товару
- quantity (INTEGER) - кількість
- unit_price_at_sale (DECIMAL) - ціна на момент продажу
- discount_amount (DECIMAL) - знижка в грн
- line_total (DECIMAL) - сума позиції

**Обсяг:** ~120,000 позицій (в середньому 1.5 товари на замовлення)

---

### 5. **suppliers.csv** (Постачальники)
```
supplier_id, supplier_name, country, contact_person, email, phone, rating, is_active
101, TechDirect Ltd, Україна, Петренко О.В., tech@direct.ua, +380443456789, 4.5, TRUE
102, GlobalTech Inc, Польща, Jan Kowalski, info@globaltech.pl, +48221234567, 4.8, TRUE
...
```

**Поля:**
- supplier_id (INTEGER)
- supplier_name (TEXT)
- country (TEXT)
- contact_person (TEXT)
- email (TEXT)
- phone (TEXT)
- rating (DECIMAL) - рейтинг від 1 до 5
- is_active (BOOLEAN)

**Обсяг:** ~30 постачальників

---

### 6. **pickup_locations.csv** (Пункти видачі)
```
location_id, location_name, city, region, address, open_date, is_active, staff_count
1, Київ Центр, Київ, Київська, вул. Хрещатик 22, 2022-01-01, TRUE, 5
2, Львів Площа Ринок, Львів, Львівська, пл. Ринок 1, 2022-02-15, TRUE, 3
...
```

**Обсяг:** 12 локацій

---

### 7. **marketing_campaigns.csv** (Маркетингові кампанії)
```
campaign_id, campaign_name, start_date, end_date, channel, budget, impressions, clicks, conversions
1, Новорічний розпродаж 2023, 2022-12-15, 2023-01-10, Facebook, 50000, 450000, 12500, 890
2, Весняні знижки, 2023-03-01, 2023-03-31, Google Ads, 35000, 320000, 8900, 534
...
```

**Обсяг:** ~40 кампаній за 3 роки

---

### 8. **customer_support.csv** (Звернення в підтримку)
```
ticket_id, customer_id, order_id, created_date, closed_date, category, priority, status, resolution_time_hours
1, 234, 1205, 2022-02-15 10:30:00, 2022-02-15 14:20:00, Доставка, High, Closed, 3.83
2, 567, 3421, 2022-02-16 09:15:00, NULL, Товар, Medium, Open, NULL
...
```

**Категорії:** Доставка, Товар, Оплата, Повернення, Технічна підтримка, Інше

**Обсяг:** ~5,000 звернень

---

### 9. **website_traffic.csv** (Трафік сайту - агрегований по днях)
```
date, sessions, users, pageviews, bounce_rate, avg_session_duration_sec, conversions, source
2022-01-16, 3450, 2890, 15670, 42.5, 185, 89, Organic
2022-01-16, 1230, 1100, 4560, 38.2, 220, 45, Paid Search
...
```

**Source:** Organic, Paid Search, Social, Direct, Referral, Email

**Обсяг:** ~5,000 записів (3 роки × 365 днів × різні джерела)

---

### 10. **product_reviews.csv** (Відгуки на товари)
```
review_id, product_id, customer_id, order_id, review_date, rating, review_text, is_verified_purchase
1, 45, 234, 1205, 2022-01-25, 5, Чудовий телефон! Швидкий і якісний., TRUE
2, 128, 567, 3421, 2022-02-10, 4, Хороші навушники за свої гроші., TRUE
...
```

**Обсяг:** ~8,000 відгуків

---

## СКРИПТ ГЕНЕРАЦІЇ ТЕСТОВИХ ДАНИХ

Нижче наведено Python-скрипт для генерації всіх файлів CSV:

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Налаштування
random.seed(42)
np.random.seed(42)

# Константи
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2024, 12, 31)
REGIONS = ['Київська', 'Львівська', 'Харківська', 'Дніпропетровська', 'Одеська']
CITIES = {
    'Київська': ['Київ', 'Бровари', 'Біла Церква'],
    'Львівська': ['Львів', 'Дрогобич', 'Стрий'],
    'Харківська': ['Харків', 'Лозова', 'Ізюм'],
    'Дніпропетровська': ['Дніпро', 'Кривий Ріг', 'Нікополь'],
    'Одеська': ['Одеса', 'Чорноморськ', 'Южне']
}

# 1. Генерація клієнтів
def generate_customers(n=15000):
    first_names = ['Олександр', 'Марія', 'Іван', 'Олена', 'Петро', 'Наталія', 'Дмитро', 'Анна', 
                   'Сергій', 'Тетяна', 'Андрій', 'Катерина', 'Володимир', 'Світлана', 'Максим']
    last_names = ['Іваненко', 'Коваленко', 'Петренко', 'Шевченко', 'Ткаченко', 'Бондаренко', 
                  'Мельник', 'Кравченко', 'Василенко', 'Клименко']
    
    customers = []
    for i in range(1, n+1):
        region = random.choice(REGIONS)
        city = random.choice(CITIES[region])
        gender = random.choice(['М', 'Ж'])
        
        customers.append({
            'customer_id': i,
            'registration_date': START_DATE + timedelta(days=random.randint(0, (END_DATE-START_DATE).days)),
            'full_name': f"{random.choice(last_names)} {random.choice(first_names)}",
            'email': f"user{i}@{'gmail.com' if i%2==0 else 'ukr.net'}",
            'phone': f"+38050{random.randint(1000000, 9999999)}",
            'city': city,
            'region': region,
            'age': random.randint(18, 65),
            'gender': gender,
            'customer_segment': random.choices(['Premium', 'Standard', 'Budget'], 
                                              weights=[0.15, 0.60, 0.25])[0]
        })
    
    return pd.DataFrame(customers)

# 2. Генерація товарів
def generate_products(n=500):
    categories = {
        'Смартфони': ['Apple', 'Samsung', 'Xiaomi', 'Google', 'OnePlus'],
        'Ноутбуки': ['Apple', 'Dell', 'HP', 'Lenovo', 'ASUS'],
        'Планшети': ['Apple', 'Samsung', 'Lenovo', 'Xiaomi'],
        'Аксесуари': ['Anker', 'Belkin', 'JBL', 'Sony', 'Logitech'],
        'Побутова техніка': ['Samsung', 'LG', 'Bosch', 'Philips', 'Xiaomi']
    }
    
    products = []
    product_id = 1
    
    for category, brands in categories.items():
        items_per_category = n // len(categories)
        for _ in range(items_per_category):
            brand = random.choice(brands)
            
            # Ціноутворення
            if category == 'Смартфони':
                price = random.randint(5000, 50000)
            elif category == 'Ноутбуки':
                price = random.randint(15000, 70000)
            elif category == 'Планшети':
                price = random.randint(8000, 40000)
            elif category == 'Аксесуари':
                price = random.randint(200, 5000)
            else:
                price = random.randint(3000, 30000)
            
            cost_price = int(price * random.uniform(0.65, 0.85))
            
            products.append({
                'product_id': product_id,
                'product_name': f"{brand} {category[:-1]} Model-{random.randint(100, 999)}",
                'category': category,
                'subcategory': brand,
                'brand': brand,
                'unit_price': price,
                'cost_price': cost_price,
                'supplier_id': random.randint(101, 130),
                'in_stock': random.randint(0, 100),
                'is_active': random.choice([True, True, True, False])  # 75% активні
            })
            product_id += 1
    
    return pd.DataFrame(products)

# 3. Генерація замовлень
def generate_orders(customers_df, n=80000):
    orders = []
    channels = ['Website', 'Mobile App', 'Partner Store']
    statuses = ['Delivered', 'Shipped', 'Pending', 'Cancelled', 'Returned']
    payment_methods = ['Card', 'Cash', 'Online']
    
    for i in range(1, n+1):
        customer_id = random.choice(customers_df['customer_id'].tolist())
        order_date = START_DATE + timedelta(days=random.randint(0, (END_DATE-START_DATE).days),
                                           hours=random.randint(0, 23),
                                           minutes=random.randint(0, 59))
        
        status = random.choices(statuses, weights=[0.65, 0.15, 0.08, 0.10, 0.02])[0]
        
        shipping_date = None
        delivery_date = None
        
        if status in ['Delivered', 'Shipped']:
            shipping_date = order_date + timedelta(days=random.randint(1, 3))
            if status == 'Delivered':
                delivery_date = shipping_date + timedelta(days=random.randint(1, 5))
        
        orders.append({
            'order_id': i,
            'customer_id': customer_id,
            'order_date': order_date,
            'shipping_date': shipping_date,
            'delivery_date': delivery_date,
            'order_status': status,
            'channel': random.choice(channels),
            'pickup_location_id': random.randint(1, 12) if status != 'Cancelled' else None,
            'payment_method': random.choice(payment_methods),
            'discount_percent': random.choices([0, 5, 10, 15, 20], weights=[0.5, 0.25, 0.15, 0.07, 0.03])[0],
            'shipping_cost': random.choice([0, 50, 70, 100]),
            'total_amount': 0  # Буде розраховано пізніше
        })
    
    return pd.DataFrame(orders)

# 4. Генерація позицій замовлень
def generate_order_items(orders_df, products_df):
    order_items = []
    item_id = 1
    
    for _, order in orders_df.iterrows():
        if order['order_status'] == 'Cancelled':
            continue
        
        # Кількість товарів у замовленні
        items_count = random.choices([1, 2, 3, 4], weights=[0.5, 0.3, 0.15, 0.05])[0]
        
        selected_products = products_df.sample(n=items_count)
        order_total = 0
        
        for _, product in selected_products.iterrows():
            quantity = random.randint(1, 3)
            unit_price = product['unit_price']
            discount_amount = unit_price * (order['discount_percent'] / 100) * quantity
            line_total = (unit_price * quantity) - discount_amount
            order_total += line_total
            
            order_items.append({
                'order_item_id': item_id,
                'order_id': order['order_id'],
                'product_id': product['product_id'],
                'quantity': quantity,
                'unit_price_at_sale': unit_price,
                'discount_amount': discount_amount,
                'line_total': line_total
            })
            item_id += 1
        
        # Оновлення total_amount
        orders_df.loc[orders_df['order_id'] == order['order_id'], 'total_amount'] = order_total + order['shipping_cost']
    
    return pd.DataFrame(order_items), orders_df

# 5. Генерація постачальників
def generate_suppliers(n=30):
    suppliers = []
    countries = ['Україна', 'Польща', 'Німеччина', 'Китай', 'США']
    
    for i in range(101, 101+n):
        suppliers.append({
            'supplier_id': i,
            'supplier_name': f"TechSupply-{i}",
            'country': random.choice(countries),
            'contact_person': f"Contact Person {i}",
            'email': f"supplier{i}@tech.com",
            'phone': f"+48{random.randint(100000000, 999999999)}",
            'rating': round(random.uniform(3.5, 5.0), 1),
            'is_active': random.choice([True, True, True, False])
        })
    
    return pd.DataFrame(suppliers)

# 6. Пункти видачі
def generate_pickup_locations():
    locations = [
        {'location_id': 1, 'location_name': 'Київ Центр', 'city': 'Київ', 'region': 'Київська', 
         'address': 'вул. Хрещатик 22', 'open_date': '2022-01-01', 'is_active': True, 'staff_count': 5},
        {'location_id': 2, 'location_name': 'Київ Позняки', 'city': 'Київ', 'region': 'Київська', 
         'address': 'просп. Бажана 10', 'open_date': '2022-03-15', 'is_active': True, 'staff_count': 4},
        {'location_id': 3, 'location_name': 'Львів Площа Ринок', 'city': 'Львів', 'region': 'Львівська', 
         'address': 'пл. Ринок 1', 'open_date': '2022-02-01', 'is_active': True, 'staff_count': 3},
        {'location_id': 4, 'location_name': 'Львів Сихів', 'city': 'Львів', 'region': 'Львівська', 
         'address': 'вул. Наукова 5', 'open_date': '2022-06-10', 'is_active': True, 'staff_count': 3},
        {'location_id': 5, 'location_name': 'Харків Центр', 'city': 'Харків', 'region': 'Харківська', 
         'address': 'вул. Сумська 45', 'open_date': '2022-01-20', 'is_active': True, 'staff_count': 4},
        {'location_id': 6, 'location_name': 'Харків Салтівка', 'city': 'Харків', 'region': 'Харківська', 
         'address': 'просп. Героїв Харкова 150', 'open_date': '2022-08-01', 'is_active': True, 'staff_count': 3},
        {'location_id': 7, 'location_name': 'Дніпро Центр', 'city': 'Дніпро', 'region': 'Дніпропетровська', 
         'address': 'просп. Яворницького 23', 'open_date': '2022-02-15', 'is_active': True, 'staff_count': 4},
        {'location_id': 8, 'location_name': 'Дніпро Сокол', 'city': 'Дніпро', 'region': 'Дніпропетровська', 
         'address': 'вул. Титова 1', 'open_date': '2022-09-01', 'is_active': True, 'staff_count': 2},
        {'location_id': 9, 'location_name': 'Одеса Дерибасівська', 'city': 'Одеса', 'region': 'Одеська', 
         'address': 'вул. Дерибасівська 15', 'open_date': '2022-03-01', 'is_active': True, 'staff_count': 3},
        {'location_id': 10, 'location_name': 'Одеса Аркадія', 'city': 'Одеса', 'region': 'Одеська', 
         'address': 'Французький бульвар 60', 'open_date': '2022-07-15', 'is_active': True, 'staff_count': 2},
        {'location_id': 11, 'location_name': 'Кривий Ріг', 'city': 'Кривий Ріг', 'region': 'Дніпропетровська', 
         'address': 'просп. Миру 15', 'open_date': '2023-01-10', 'is_active': True, 'staff_count': 2},
        {'location_id': 12, 'location_name': 'Біла Церква', 'city': 'Біла Церква', 'region': 'Київська', 
         'address': 'пл. Соборна 3', 'open_date': '2023-05-01', 'is_active': True, 'staff_count': 2}
    ]
    
    return pd.DataFrame(locations)

# Генерація всіх датасетів
print("Генерація даних...")
customers = generate_customers(15000)
products = generate_products(500)
suppliers = generate_suppliers(30)
locations = generate_pickup_locations()
orders = generate_orders(customers, 80000)
order_items, orders = generate_order_items(orders, products)

# Збереження у CSV
print("Збереження файлів...")
customers.to_csv('customers.csv', index=False, encoding='utf-8-sig')
products.to_csv('products.csv', index=False, encoding='utf-8-sig')
suppliers.to_csv('suppliers.csv', index=False, encoding='utf-8-sig')
locations.to_csv('pickup_locations.csv', index=False, encoding='utf-8-sig')
orders.to_csv('orders.csv', index=False, encoding='utf-8-sig')
order_items.to_csv('order_items.csv', index=False, encoding='utf-8-sig')

print("✅ Генерація завершена!")
print(f"Клієнти: {len(customers)}")
print(f"Товари: {len(products)}")
print(f"Замовлення: {len(orders)}")
print(f"Позиції замовлень: {len(order_items)}")
```

---

# ДЕТАЛЬНІ ОПИСИ ПРАКТИЧНИХ РОБІТ

---

## ПРАКТИЧНА РОБОТА №1
### Тема: Підготовка даних (Power Query як ETL)

**Мета:** Навчитися імпортувати дані з різних джерел та виконувати базові трансформації в Power Query.

**Тривалість:** 4 години (2 пари)

---

### Теоретична частина (30 хв)

**Основні поняття:**
- ETL (Extract, Transform, Load) vs ELT
- Power Query як інструмент підготовки даних
- Типи джерел даних (CSV, Excel, бази даних, API)
- Основні операції трансформації
- Query Folding та оптимізація

**Інтерфейс Power Query:**
- Ribbon меню та групи команд
- Applied Steps (історія трансформацій)
- Formula Bar (M-код)
- Query Dependencies (залежності запитів)

---

### Практична частина (3 год 30 хв)

#### **Завдання 1: Імпорт та очищення даних клієнтів (45 хв)**

**Крок 1:** Завантажте файл `customers.csv`
- Home → Get Data → Text/CSV
- Перегляньте дані у вікні попереднього перегляду
- Натисніть "Transform Data"

**Крок 2:** Очистіть дані
```
Операції:
1. Видалити дублікати по полю email
2. Видалити рядки з NULL в полях full_name або email
3. Розділити full_name на три колонки (прізвище, ім'я, по-батькові)
   - Transform → Split Column → By Delimiter (пробіл)
   - Rename: last_name, first_name, patronymic
4. Стандартизувати формат телефону
   - Replace Values: видалити всі символи крім цифр
   - Transform → Format → Add Prefix: "+"
5. Перевірити діапазони значень age (18-65)
   - Filter → Number Filters → Between
6. Змінити тип даних registration_date на Date
```

**Очікуваний результат:** 
- Таблиця без дубл��катів та NULL
- ПІБ розділене на 3 колонки
- Стандартизовані телефони
- Коректні типи даних

---

#### **Завдання 2: Трансформація даних товарів (45 хв)**

**Крок 1:** Завантажте `products.csv`

**Крок 2:** Додайте розраховані колонки
```
Операції:
1. Розрахувати маржу (margin):
   - Add Column → Custom Column
   - Формула: [unit_price] - [cost_price]
   - Rename: margin

2. Розрахувати маржу % (margin_percent):
   - Custom Column
   - Формула: ([unit_price] - [cost_price]) / [unit_price] * 100
   - Change Type → Decimal Number
   - Format → Round → 2 decimal places

3. Створити ціновий сегмент (price_segment):
   - Conditional Column
   - IF unit_price < 5000 THEN "Бюджетний"
   - ELSE IF unit_price < 20000 THEN "Середній"
   - ELSE "Преміум"

4. Фільтр активних товарів:
   - Filter is_active = TRUE
```

**Очікуваний результат:** 
- Додані колонки margin, margin_percent, price_segment
- Тільки активні товари

---

#### **Завдання 3: Об'єднання таблиць Orders та OrderItems (60 хв)**

**Крок 1:** Завантажте `orders.csv` та `order_items.csv`

**Крок 2:** Зробіть Merge
```
Операції:
1. У таблиці orders:
   - Home → Merge Queries → Merge Queries as New
   - Join Kind: Left Outer
   - Key: order_id = order_id
   
2. Розгорніть колонки з order_items:
   - Expand → Select: product_id, quantity, line_total
   
3. Знову Merge з products:
   - Merge on product_id
   - Expand: product_name, category, unit_price

4. Додайте розраховану колонку revenue_per_item:
   - line_total - (cost_price * quantity)
```

**Очікуваний результат:**
- Єдина таблиця з даними замовлень, товарів та клієнтів
- Розрахована виручка по кожній позиції

---

#### **Завдання 4: Агрегація даних (45 хв)**

**Створіть зведену таблицю продажів по категоріях:**

```
1. Дублюйте запит orders_detailed
2. Group By:
   - Group by: category
   - New column name: total_orders
   - Operation: Count Rows
   
3. Додайте агрегації:
   - total_revenue: Sum of line_total
   - avg_order_value: Average of line_total
   - total_quantity: Sum of quantity

4. Сортування:
   - Sort Descending by total_revenue
```

---

#### **Завдання 5: Робота з датами (45 хв)**

**Створіть календарну таблицю (Date Dimension):**

```M
let
    StartDate = #date(2022, 1, 1),
    EndDate = #date(2024, 12, 31),
    NumberOfDays = Duration.Days(EndDate - StartDate) + 1,
    Dates = List.Dates(StartDate, NumberOfDays, #duration(1, 0, 0, 0)),
    TableFromList = Table.FromList(Dates, Splitter.SplitByNothing(), {"Date"}),
    ChangedType = Table.TransformColumnTypes(TableFromList, {{"Date", type date}}),
    
    // Додати колонки
    AddYear = Table.AddColumn(ChangedType, "Year", each Date.Year([Date]), Int64.Type),
    AddMonth = Table.AddColumn(AddYear, "Month", each Date.Month([Date]), Int64.Type),
    AddMonthName = Table.AddColumn(AddMonth, "MonthName", each Date.MonthName([Date]), type text),
    AddQuarter = Table.AddColumn(AddMonthName, "Quarter", each "Q" & Text.From(Date.QuarterOfYear([Date])), type text),
    AddDayOfWeek = Table.AddColumn(AddQuarter, "DayOfWeek", each Date.DayOfWeek([Date], Day.Monday) + 1, Int64.Type),
    AddDayName = Table.AddColumn(AddDayOfWeek, "DayName", each Date.DayOfWeekName([Date]), type text),
    AddWeekOfYear = Table.AddColumn(AddDayName, "WeekOfYear", each Date.WeekOfYear([Date]), Int64.Type)
in
    AddWeekOfYear
```

**Додаткові колонки:**
- IsWeekend (BOOLEAN)
- FiscalYear (якщо фінансовий рік починається з липня)
- YearMonth (TEXT): "2022-01"

---

### Контрольні питання

1. У чому різниця між Merge та Append в Power Query?
2. Що таке Query Folding і чому це важливо?
3. Як створити параметр в Power Query і де його використовувати?
4. Яка різниця між Remove Duplicates та Remove Blank Rows?
5. Що таке M-мова і коли потрібно писати код вручну?

---

### Критерії оцінювання

| Критерій | Бали |
|----------|------|
| Коректний імпорт всіх файлів | 10 |
| Очищення та стандартизація даних | 20 |
| Розраховані колонки створені правильно | 20 |
| Merge виконано з правильними Join типами | 20 |
| Агрегація та Group By | 15 |
| Календарна таблиця створена | 10 |
| Документування кроків (коментарі) | 5 |
| **ВСЬОГО** | **100** |

---

### Додаткові завдання (для сильних студентів)

1. **Завдання на параметри:**
   - Створіть параметр для фільтрації по регіону
   - Створіть функцію для конвертації валют

2. **Завдання на складні трансформації:**
   - Unpivot таблиці продажів по місяцях
   - Pivot категорій товарів

3. **Завдання на помилки:**
   - Додайте обробку помилок (try...otherwise)
   - Створіть кастомну функцію валідації email

---

## ПРАКТИЧНА РОБОТА №2
### Тема: Проєктування моделі даних

**Мета:** Створити оптимальну модель даних за схемою "зірка" для аналітики продажів.

**Тривалість:** 4 години

---

### Теоретична частина (40 хв)

**Основні концепції:**
- Схема "зірка" vs "сніжинка"
- Таблиці фактів (Fact Tables)
- Таблиці вимірів (Dimension Tables)
- Зв'язки (Relationships): One-to-Many, Many-to-Many
- Кардинальність та Cross-Filter Direction
- Slowly Changing Dimensions (SCD Type 1, 2, 3)

**Принципи моделювання:**
- Normalization vs Denormalization
- Surrogate Keys vs Natural Keys
- Role-Playing Dimensions (напр., календар)
- Degenerate Dimensions
- Junk Dimensions

---

### Практична частина (3 год 20 хв)

#### **Завдання 1: Аналіз вимог та проєктування схеми (30 хв)**

**Бізнес-вимоги для TechStore:**

Керівництво хоче аналізувати:
1. **Продажі:**
   - По категоріях товарів
   - По регіонах
   - По каналах продажу
   - В розрізі часу (день/тиждень/місяць/квартал/рік)

2. **Клієнти:**
   - Сегментація клієнтів
   - География клієнтів
   - Вікові групи

3. **Товари:**
   - Категорії та бренди
   - Цінові сегменти
   - Маржинальність

**Завдання:**
Накресліть схему моделі даних на папері або у draw.io:
- Визначте таблиці фактів (мінімум 1)
- Визначте таблиці вимірів (мінімум 5)
- Позначте зв'язки та їх кардинальність

**Очікувана схема:**

```
        DimDate
           |
           | (1:M)
           |
        FactSales -----(M:1)---- DimProduct
           |
           |-----(M:1)---- DimCustomer
           |
           |-----(M:1)---- DimLocation
           |
           |-----(M:1)---- DimChannel
```

---

#### **Завдання 2: Створення таблиць вимірів (90 хв)**

**2.1. DimDate (Календар)**

Використайте код з Практичної №1 або створіть вручну:

```
Обов'язкові поля:
- DateKey (INT): 20220101, 20220102... (Primary Key)
- Date (DATE)
- Year (INT)
- Quarter (TEXT): Q1, Q2, Q3, Q4
- Month (INT): 1-12
- MonthName (TEXT): Січень, Лютий...
- MonthNameShort (TEXT): Січ, Лют...
- WeekOfYear (INT)
- DayOfMonth (INT)
- DayOfWeek (INT): 1-7
- DayName (TEXT): Понеділок, Вівторок...
- IsWeekend (BOOLEAN)
- IsHoliday (BOOLEAN) - додайте українські свята
```

**Свята для України:**
```M
let
    Holidays = {
        #date(2022,1,1), #date(2022,1,7), #date(2022,5,1), 
        #date(2022,5,9), #date(2022,6,28), #date(2022,8,24),
        // ... додайте всі свята для 2022-2024
    },
    AddIsHoliday = Table.AddColumn(PreviousStep, "IsHoliday", 
        each List.Contains(Holidays, [Date]), type logical)
in
    AddIsHoliday
```

---

**2.2. DimProduct (Товари)**

```
Структура:
- ProductKey (INT) - Surrogate Key
- ProductID (INT) - Natural Key з джерела
- ProductName (TEXT)
- Category (TEXT)
- Subcategory (TEXT)
- Brand (TEXT)
- UnitPrice (DECIMAL)
- CostPrice (DECIMAL)
- PriceSegment (TEXT): Бюджетний/Середній/Преміум
- IsActive (BOOLEAN)

Додаткові розраховані поля (в Power Query):
- Margin = UnitPrice - CostPrice
- MarginPercent = (UnitPrice - CostPrice) / UnitPrice * 100
```

**Трансформації:**
1. Додайте Surrogate Key (Index Column, start at 1)
2. Rename: ProductID → ProductID_Source
3. Rename: Index → ProductKey
4. Reorder columns: ProductKey, ProductID_Source, ...

---

**2.3. DimCustomer (Клієнти)**

```
Структура:
- CustomerKey (INT)
- CustomerID (INT)
- FullName (TEXT)
- FirstName (TEXT)
- LastName (TEXT)
- Email (TEXT)
- Phone (TEXT)
- Age (INT)
- AgeGroup (TEXT): 18-25, 26-35, 36-45, 46-55, 56-65, 65+
- Gender (TEXT)
- CustomerSegment (TEXT)
- City (TEXT)
- Region (TEXT)
- RegistrationDate (DATE)

Додайте колонку AgeGroup:
```M
= Table.AddColumn(PreviousStep, "AgeGroup", 
    each if [Age] <= 25 then "18-25"
    else if [Age] <= 35 then "26-35"
    else if [Age] <= 45 then "36-45"
    else if [Age] <= 55 then "46-55"
    else if [Age] <= 65 then "56-65"
    else "65+", type text)
```

---

**2.4. DimLocation (Пункти видачі)**

```
Структура:
- LocationKey (INT)
- LocationID (INT)
- LocationName (TEXT)
- City (TEXT)
- Region (TEXT)
- Address (TEXT)
- OpenDate (DATE)
- IsActive (BOOLEAN)
- StaffCount (INT)
```

---

**2.5. DimChannel (Канали продажу)**

Створіть вручну невелику таблицю:

| ChannelKey | ChannelName | ChannelType | CommissionRate |
|------------|-------------|-------------|----------------|
| 1 | Website | Online | 0.00 |
| 2 | Mobile App | Online | 0.00 |
| 3 | Partner Store | Offline | 0.05 |

---

#### **Завдання 3: Створення таблиці фактів (60 хв)**

**FactSales (Факти продажів)**

```
Базова структура:
- OrderID (INT)
- OrderItemID (INT) - можливо Degenerate Dimension
- DateKey (INT) - FK до DimDate
- CustomerKey (INT) - FK до DimCustomer
- ProductKey (INT) - FK до DimProduct
- LocationKey (INT) - FK до DimLocation
- ChannelKey (INT) - FK до DimChannel

Показники (Measures):
- Quantity (INT) - кількість
- UnitPrice (DECIMAL) - ціна на момент продажу
- CostPrice (DECIMAL) - собівартість
- DiscountAmount (DECIMAL) - знижка
- ShippingCost (DECIMAL) - доставка
- LineTotal (DECIMAL) - сума позиції
- Revenue (DECIMAL) - виручка (LineTotal - знижка)
- Cost (DECIMAL) - собівартість (CostPrice * Quantity)
- Profit (DECIMAL) - прибуток (Revenue - Cost)
```

**Крок за кроком:**

1. **Почніть з order_items:**
```M
let
    Source = OrderItems,
    // Merge з Orders для отримання дат та клієнтів
    MergeOrders = Table.NestedJoin(Source, {"order_id"}, Orders, {"order_id"}, "Orders", JoinKind.Inner),
    ExpandOrders = Table.ExpandTableColumn(MergeOrders, "Orders", 
        {"order_date", "customer_id", "channel", "pickup_location_id", "shipping_cost"}),
    
    // Merge з Products для собівартості
    MergeProducts = Table.NestedJoin(ExpandOrders, {"product_id"}, Products, {"product_id"}, "Products", JoinKind.Inner),
    ExpandProducts = Table.ExpandTableColumn(MergeProducts, "Products", {"cost_price"}),
    
    // Створити DateKey
    AddDateKey = Table.AddColumn(ExpandProducts, "DateKey", 
        each Date.Year([order_date]) * 10000 + Date.Month([order_date]) * 100 + Date.Day([order_date]), Int64.Type),
    
    // Замінити природні ключі на Surrogate Keys через Merge
    // ... (продовження в наступних кроках)
in
    AddDateKey
```

2. **Додайте Surrogate Keys:**
   - Merge з DimProduct по product_id → отримати ProductKey
   - Merge з DimCustomer по customer_id → отримати CustomerKey
   - Merge з DimLocation по pickup_location_id → отримати LocationKey
   - Merge з DimChannel по channel → отримати ChannelKey

3. **Додайте розраховані поля:**
```M
AddRevenue = Table.AddColumn(PreviousStep, "Revenue", each [line_total]),
AddCost = Table.AddColumn(AddRevenue, "Cost", each [cost_price] * [quantity]),
AddProfit = Table.AddColumn(AddCost, "Profit", each [Revenue] - [Cost])
```

4. **Видаліть зайві колонки:**
   - Залиште тільки Keys та Measures
   - Remove: product_id, customer_id, channel, order_date, product_name...

**Фінальна структура FactSales:**
```
OrderID, OrderItemID, DateKey, CustomerKey, ProductKey, LocationKey, ChannelKey,
Quantity, UnitPrice, CostPrice, DiscountAmount, ShippingCost, LineTotal, Revenue, Cost, Profit
```

---

#### **Завдання 4: Створення зв'язків (Relationships) (30 хв)**

**Перейдіть до Model View в Power BI:**

1. **Зв'язок FactSales → DimDate:**
   - Перетягніть DateKey з FactSales на DateKey у DimDate
   - Cardinality: Many-to-One (*:1)
   - Cross-filter direction: Single (від DimDate до FactSales)
   - Make this relationship active: ✓

2. **Зв'язок FactSales → DimProduct:**
   - ProductKey (*:1)
   - Single direction

3. **Зв'язок FactSales → DimCustomer:**
   - CustomerKey (*:1)
   - Single direction

4. **Зв'язок FactSales → DimLocation:**
   - LocationKey (*:1)
   - Single direction

5. **Зв'язок FactSales → DimChannel:**
   - ChannelKey (*:1)
   - Single direction

**Перевірка моделі:**
- Усі зв'язки повинні бути One-to-Many (від Dimension до Fact)
- Немає Many-to-Many зв'язків
- Немає циклічних залежностей
- Cross-filter direction: Single (за замовчуванням)

---

#### **Завдання 5: Тестування моделі (30 хв)**

**Створіть тестовий звіт:**

1. **Таблиця 1: Продажі по категоріях**
   - Rows: DimProduct[Category]
   - Values: 
     - Sum(FactSales[Revenue])
     - Sum(FactSales[Profit])
     - Count(FactSales[OrderID])

2. **Таблиця 2: Продажі по місяцях**
   - Rows: DimDate[Year], DimDate[MonthName]
   - Values: Sum(FactSales[Revenue])

3. **Таблиця 3: Продажі по регіонах**
   - Rows: DimCustomer[Region]
   - Values: Sum(FactSales[Revenue])

**Перевірте:**
- Чи коректно фільтрується таблиця фактів при виборі значень з вимірів
- Чи сумарні показники збігаються з очікуваними
- Чи працює drill-down (розгортання ієрархій)

---

### Контрольні питання

1. У чому різниця між схемою "зірка" і "сніжинка"? Коли використовувати кожну?
2. Що таке Surrogate Key і навіщо він потрібен?
3. Чому в таблиці фактів зберігаються тільки ключі (FK), а не всі атрибути?
4. Що таке Slowly Changing Dimension Type 2? Наведіть приклад.
5. Як працює Cross-Filter Direction і коли використовувати Both?

---

### Критерії оцінювання

| Критерій | Бали |
|----------|------|
| Схема моделі накреслена правильно | 10 |
| DimDate створена з усіма полями | 10 |
| DimProduct, DimCustomer, DimLocation, DimChannel | 20 |
| FactSales створена правильно | 25 |
| Surrogate Keys використані коректно | 10 |
| Relationships налаштовані правильно | 15 |
| Тестування моделі виконане | 10 |
| **ВСЬОГО** | **100** |

---

### Додаткові завдання

1. **Розширення моделі:**
   - Додайте DimSupplier (постачальники)
   - Створіть FactPurchases (закупівлі)

2. **Складніші виміри:**
   - Створіть Parent-Child ієрархію для категорій товарів
   - Реалізуйте SCD Type 2 для DimCustomer (відстеження зміни сегменту)

3. **Many-to-Many:**
   - Створіть DimPromotion (акції)
   - Зв'яжіть з FactSales через Bridge Table

---

## ПРАКТИЧНА РОБОТА №3
### Тема: Power BI - Створення звітів (частина 1)

**Мета:** Навчитися створювати базові візуалізації та інтерактивні звіти в Power BI.

**Тривалість:** 4 години

---

### Теоретична частина (30 хв)

**Типи візуалізацій:**
- Таблиці та матриці
- Стовпчикові та стрічкові діаграми
- Лінійні графіки
- Кругові та кільцеві діаграми
- Карти (географічні)
- KPI та Gauge
- Waterfall, Funnel

**Принципи ефективної візуалізації:**
- Вибір правильного типу діаграми для даних
- Колірні схеми та контрастність
- Підписи та легенди
- Whitespace та композиція

**Інтерактивність:**
- Фільтри (Report, Page, Visual level)
- Slicers (слайсери)
- Cross-highlighting та Cross-filtering
- Drill-down та Drill-through
- Tooltips (підказки)

---

### Практична частина (3 год 30 хв)

#### **Завдання 1: Створення Dashboard "Огляд продажів" (90 хв)**

**Створіть нову сторінку звіту "Sales Overview"**

**1.1. KPI Cards (15 хв)**

Додайте 4 картки зверху сторінки:

```
Card 1: Total Revenue
- Visual: Card
- Field: Sum of FactSales[Revenue]
- Формат: Currency (грн), 0 decimal places
- Назва: "Загальна виручка"

Card 2: Total Orders
- Visual: Card  
- Field: DistinctCount of FactSales[OrderID]
- Формат: Whole number
- Назва: "Кількість замовлень"

Card 3: Average Order Value
- Visual: Card
- Field: [створіть міру] Average Order Value = 
    DIVIDE(SUM(FactSales[Revenue]), DISTINCTCOUNT(FactSales[OrderID]))
- Формат: Currency (грн), 0 decimal places
- Назва: "Середній чек"

Card 4: Profit Margin %
- Visual: Card
- Field: [створіть міру] Profit Margin % = 
    DIVIDE(SUM(FactSales[Profit]), SUM(FactSales[Revenue])) * 100
- Формат: Percentage, 1 decimal place
- Назва: "Маржа, %"
```

**Формат Cards:**
- Background: Світло-сірий (#F5F5F5)
- Data label size: 32pt
- Category label size: 12pt
- Alignment: Center

---

**1.2. Стовпчикова діаграма "Продажі по категоріях" (20 хв)**

```
Visual: Clustered Column Chart
Axis: DimProduct[Category]
Values: 
  - Sum of FactSales[Revenue]
  - Sum of FactSales[Profit]
Legend: Автоматично (Revenue/Profit)

Форматування:
- Title: "Виручка та прибуток по категоріях товарів"
- Data labels: On
- X-axis title: Off
- Y-axis title: "Сума, грн"
- Colors: 
  - Revenue: #0078D4 (синій)
  - Profit: #107C10 (зелений)
```

**Додайте Average Line:**
- Analytics → Average line → Add
- Line style: Dashed
- Color: Gray

---

**1.3. Лінійний графік "Тренд продажів" (20 хв)**

```
Visual: Line Chart
Axis: DimDate[Date] (встановіть ієрархію: Year → Quarter → Month → Date)
Values: Sum of FactSales[Revenue]
Legend: None

Форматування:
- Title: "Динаміка продажів 2022-2024"
- Data labels: Off
- Markers: On
- Line width: 3px
- Color: #0078D4

Додайте Forecast:
- Analytics → Forecast → Add
- Forecast length: 30 days
- Confidence interval: 95%
- Seasonality: Auto-detect
```

---

**1.4. Карта "Продажі по регіонах" (20 хв)**

```
Visual: Map (Filled Map)
Location: DimCustomer[Region]
Legend: Sum of FactSales[Revenue]
Tooltips: 
  - DimCustomer[Region]
  - Sum of FactSales[Revenue]
  - Count of FactSales[OrderID]

Форматування:
- Title: "Географія продажів"
- Color scale: Sequential
  - Minimum: Білий
  - Maximum: #0078D4
- Default color: Light gray
```

**Якщо Map не працює (координати):**
- Використайте Stacked Bar Chart
- Axis: DimCustomer[Region]
- Values: Sum of FactSales[Revenue]
- Sort Descending

---

**1.5. Таблиця "Топ-10 товарів" (15 хв)**

```
Visual: Table
Columns:
  - DimProduct[ProductName]
  - Sum of FactSales[Quantity] (назва: "Продано шт.")
  - Sum of FactSales[Revenue] (назва: "Виручка")
  - Sum of FactSales[Profit] (назва: "Прибуток")

Filters on this visual:
- Top N filter: 
  - Show items: Top 10
  - By value: Sum of FactSales[Revenue]

Форматування:
- Title: "Топ-10 товарів за виручкою"
- Grid: Horizontal lines only
- Text size: 10pt
- Conditional formatting на Profit:
  - Data bars: Green for positive, Red for negative
```

---

#### **Завдання 2: Додавання інтерактивності (60 хв)**

**2.1. Slicers (Фільтри) (30 хв)**

Додайте 4 слайсери зліва від Dashboard:

```
Slicer 1: Період
- Visual: Slicer
- Field: DimDate[Year]
- Slicer type: Dropdown
- Multi-select: Enabled
- Select All: Enabled
- Title: "Рік"

Slicer 2: Категорія
- Visual: Slicer
- Field: DimProduct[Category]
- Slicer type: List
- Multi-select: Enabled
- Title: "Категорія товару"

Slicer 3: Регіон
- Visual: Slicer
- Field: DimCustomer[Region]
- Slicer type: Dropdown
- Multi-select: Enabled
- Title: "Регіон"

Slicer 4: Канал продажу
- Visual: Slicer
- Field: DimChannel[ChannelName]
- Slicer type: Tile (кнопки)
- Multi-select: Single
- Title: "Канал продажу"
```

**Форматування Slicers:**
- Background: White
- Border: 1px, Light gray
- Title font size: 12pt, Bold

---

**2.2. Cross-Filtering (15 хв)**

**Налаштуйте взаємодію візуалів:**

1. Format → Edit interactions
2. Виберіть Stacked Column Chart (Продажі по категоріях)
3. Для інших візуалів встановіть:
   - Line Chart: Filter (фільтрувати)
   - Map: Filter
   - Table: Filter
   - Cards: None (не фільтрувати KPI)

**Протестуйте:**
- Клікніть на категорію "Смартфони" → всі візуали повинні відфільтруватись
- Перевірте що Cards НЕ фільтруються

---

**2.3. Tooltips (Підказки) (15 хв)**

**Створіть кастомний Tooltip для Line Chart:**

1. Створіть нову сторінку "Tooltip - Sales Details"
2. Page settings:
   - Page type: Tooltip
   - Canvas size: Tooltip

3. Додайте на Tooltip page:
```
Table:
- Rows: DimDate[MonthName]
- Values:
  - Sum of FactSales[Revenue]
  - Sum of FactSales[Profit]
  - Count of FactSales[OrderID]

Форматування:
- Background: Semi-transparent white
- Border: 1px Blue
- Font size: 9pt
```

4. Повернутся до "Sales Overview"
5. Виберіть Line Chart → Format → Tooltips
6. Type: Report page
7. Page: Tooltip - Sales Details

---

#### **Завдання 3: Створення сторінки "Аналіз клієнтів" (60 хв)**

**Створіть нову сторінку "Customer Analysis"**

**3.1. Donut Chart "Розподіл клієнтів за сегментами" (15 хв)**

```
Visual: Donut Chart
Legend: DimCustomer[CustomerSegment]
Values: DistinctCount of DimCustomer[CustomerID]

Форматування:
- Title: "Розподіл клієнтів за сегментами"
- Data labels: Percentage
- Colors:
  - Premium: Gold (#FFD700)
  - Standard: Blue (#0078D4)
  - Budget: Gray (#808080)
```

---

**3.2. Stacked Bar Chart "Виручка по віковим групам" (15 хв)**

```
Visual: Stacked Bar Chart
Axis: DimCustomer[AgeGroup]
Values: Sum of FactSales[Revenue]
Legend: DimCustomer[Gender]

Форматування:
- Title: "Виручка по віковим групам та статі"
- Data labels: On
- Sort by: AgeGroup (ascending)
- Colors:
  - М: Blue (#0078D4)
  - Ж: Pink (#E3008C)
```

---

**3.3. Matrix "Продажі по регіонах та каналах" (20 хв)**

```
Visual: Matrix
Rows: DimCustomer[Region]
Columns: DimChannel[ChannelName]
Values: Sum of FactSales[Revenue]

Форматування:
- Title: "Виручка: Регіон × Канал"
- Row subtotals: On (Bottom)
- Column subtotals: On (Right)
- Grand totals: On
- Conditional formatting:
  - Background color: Color scale
    - Minimum: White
    - Maximum: Blue
```

---

**3.4. Scatter Chart "Кількість vs Вартість замовлень" (10 хв)**

```
Visual: Scatter Chart
X-axis: Count of FactSales[OrderID] (по клієнтах)
Y-axis: Sum of FactSales[Revenue] (по клієнтах)
Legend: DimCustomer[CustomerSegment]
Size: Sum of FactSales[Profit]

Для створення потрібно:
1. Створити таблицю з агрегацією по CustomerKey
2. Або використати DAX міри
```

---

#### **Завдання 4: Налаштування форматування звіту (40 хв)**

**4.1. Тема звіту (15 хв)**

1. View → Themes → Customize current theme

```
Colors:
- Primary: #0078D4
- Secondary: #107C10
- Accent 1: #FFB900
- Accent 2: #E81123
- Background: #FFFFFF
- Foreground: #252525

Typography:
- Title font: Segoe UI, Bold, 14pt
- Header font: Segoe UI, Semibold, 12pt
- Body font: Segoe UI, Regular, 10pt
```

2. Save theme as "TechStore_Theme.json"

---

**4.2. Макет сторінки (15 хв)**

**Для "Sales Overview":**
- Canvas size: 16:9 (1280 × 720)
- Grid:
  - Snap to grid: On
  - Grid spacing: 10px

**Розташування:**
```
+------------------------------------------+
|  [Year] [Category] [Region] [Channel]   |  ← Slicers (top 80px)
+------------------------------------------+
|  [Revenue] [Orders] [AOV] [Margin]      |  ← KPI Cards (80px)
+------------------------------------------+
|  [Column Chart]  |  [Line Chart]        |  ← Charts (300px)
+------------------------------------------+
|  [Map]           |  [Table Top-10]      |  ← Bottom row (260px)
+------------------------------------------+
```

**Вирівнювання:**
- Format → Align → Distribute horizontally
- Format → Align → Align top (для KPI cards)

---

**4.3. Navigation (10 хв)**

**Додайте кнопки навігації:**

1. Insert → Buttons → Navigator → Page navigator
2. Position: Left side (vertical)
3. Button text:
   - "📊 Огляд продажів"
   - "👥 Клієнти"
   - "📦 Товари" (якщо є додаткові сторінки)

**Форматування кнопок:**
- Background: Transparent
- On hover: Light blue
- Active page: Blue background

---

### Контрольні питання

1. Коли використовувати Stacked Bar Chart замість Clustered Column Chart?
2. У чому різниця між Table та Matrix?
3. Як працює Cross-filtering і як його вимкнути?
4. Що таке Drill-down і як його налаштувати?
5. Які правила вибору кольорів для візуалізацій?

---

### Критерії оцінювання

| Критерій | Бали |
|----------|------|
| KPI Cards створені з мірами | 15 |
| Базові візуалізації (Chart, Graph, Map) | 25 |
| Таблиця з Top N фільтром | 10 |
| Slicers налаштовані коректно | 15 |
| Cross-filtering працює | 10 |
| Custom Tooltips | 10 |
| Форматування та дизайн | 10 |
| Додаткова сторінка "Клієнти" | 5 |
| **ВСЬОГО** | **100** |

---

### Додаткові завдання

1. **Drill-through:**
   - Створіть детальну сторінку для аналізу окремого товару
   - Налаштуйте drill-through з таблиці Top-10

2. **Bookmarks:**
   - Створіть 3 bookmarks з різними фільтрами
   - Додайте кнопки для перемикання між ними

3. **Conditional Formatting:**
   - Додайте іконки (Icons) в таблицю на основі Profit
   - Налаштуйте Data bars для Revenue

---

(Продовження з іншими практичними роботами...)# ПРАКТИЧНІ РОБОТИ 4-8 (ПРОДОВЖЕННЯ)

## ПРАКТИЧНА РОБОТА №4
### Тема: Power BI - Аналітика і DAX (частина 2)

**Мета:** Навчитися створювати складні DAX-міри для бізнес-аналітики.

**Тривалість:** 4 години

---

### Теоретична частина (45 хв)

**Основи DAX:**
- Типи обчислень: Calculated Columns vs Measures
- Контекст обчислень: Row Context vs Filter Context
- Функції агрегації: SUM, AVERAGE, COUNT, MIN, MAX
- Функції фільтрації: CALCULATE, FILTER, ALL, ALLEXCEPT
- Функції навігації: RELATED, RELATEDTABLE
- Часові функції: DATEADD, TOTALYTD, SAMEPERIODLASTYEAR

**Принципи написання ефективного DAX:**
- Уникайте Calculated Columns де можливо (краще Measures)
- Використовуйте змінні (VAR) для читабельності
- Variables також кешують результати
- Оптимізація через SUMMARIZE/SUMMARIZECOLUMNS

---

### Практична частина (3 год 15 хв)

#### **Завдання 1: Базові міри (30 хв)**

**1.1. Створіть міри для ключових показників:**

```DAX
// 1. Загальна виручка
Total Revenue = SUM(FactSales[Revenue])

// 2. Загальний прибуток  
Total Profit = SUM(FactSales[Profit])

// 3. Кількість замовлень
Total Orders = DISTINCTCOUNT(FactSales[OrderID])

// 4. Кількість проданих одиниць
Total Quantity = SUM(FactSales[Quantity])

// 5. Середній чек
Average Order Value = 
DIVIDE(
    [Total Revenue],
    [Total Orders],
    0
)

// 6. Маржа %
Profit Margin % = 
DIVIDE(
    [Total Profit],
    [Total Revenue],
    0
) * 100

// 7. Середня ціна продажу
Average Unit Price = 
DIVIDE(
    [Total Revenue],
    [Total Quantity],
    0
)

// 8. Кількість активних клієнтів
Active Customers = DISTINCTCOUNT(FactSales[CustomerKey])
```

**Організація:**
- Створіть папку (Display Folder): "📊 Основні показники"
- Додайте всі міри в цю папку
- Встановіть формат для кожної міри (Currency, Percentage, Whole Number)

---

#### **Завдання 2: Часові розрахунки (Time Intelligence) (60 хв)**

**2.1. Міри для порівняння періодів:**

```DAX
// 1. Виручка за попередній рік (Year-over-Year)
Revenue PY = 
CALCULATE(
    [Total Revenue],
    SAMEPERIODLASTYEAR(DimDate[Date])
)

// 2. Зміна виручки рік-до-року
Revenue YoY Change = [Total Revenue] - [Revenue PY]

// 3. Зміна виручки YoY у %
Revenue YoY % = 
DIVIDE(
    [Revenue YoY Change],
    [Revenue PY],
    0
) * 100

// 4. Виручка за попередній місяць
Revenue PM = 
CALCULATE(
    [Total Revenue],
    DATEADD(DimDate[Date], -1, MONTH)
)

// 5. Зміна MoM %
Revenue MoM % = 
DIVIDE(
    [Total Revenue] - [Revenue PM],
    [Revenue PM],
    0
) * 100
```

---

**2.2. Накопичувальні підсумки (Cumulative/YTD):**

```DAX
// 1. Виручка з початку року (Year-to-Date)
Revenue YTD = 
TOTALYTD(
    [Total Revenue],
    DimDate[Date]
)

// 2. Виручка з початку року минулого року
Revenue YTD PY = 
CALCULATE(
    [Revenue YTD],
    SAMEPERIODLASTYEAR(DimDate[Date])
)

// 3. Зміна YTD рік-до-року
Revenue YTD vs PY = [Revenue YTD] - [Revenue YTD PY]

// 4. Зміна YTD у %
Revenue YTD % = 
DIVIDE(
    [Revenue YTD vs PY],
    [Revenue YTD PY],
    0
) * 100

// 5. Виручка з початку місяця (Month-to-Date)
Revenue MTD = 
TOTALMTD(
    [Total Revenue],
    DimDate[Date]
)

// 6. Виручка з початку кварталу (Quarter-to-Date)
Revenue QTD = 
TOTALQTD(
    [Total Revenue],
    DimDate[Date]
)
```

---

**2.3. Rolling/Moving averages:**

```DAX
// 1. Виручка за останні 7 днів
Revenue Last 7 Days = 
CALCULATE(
    [Total Revenue],
    DATESINPERIOD(
        DimDate[Date],
        LASTDATE(DimDate[Date]),
        -7,
        DAY
    )
)

// 2. Середня виручка за останні 30 днів
Revenue Avg 30D = 
VAR Last30Days = 
    CALCULATE(
        [Total Revenue],
        DATESINPERIOD(
            DimDate[Date],
            LASTDATE(DimDate[Date]),
            -30,
            DAY
        )
    )
RETURN
    DIVIDE(Last30Days, 30, 0)

// 3. Moving Average (3 місяці)
Revenue MA 3M = 
CALCULATE(
    [Total Revenue],
    DATESINPERIOD(
        DimDate[Date],
        LASTDATE(DimDate[Date]),
        -3,
        MONTH
    )
) / 3
```

**Організація:**
- Display Folder: "📅 Часові розрахунки"

---

#### **Завдання 3: Складні розрахунки з CALCULATE (45 хв)**

**3.1. Фільтрація та контекст:**

```DAX
// 1. Виручка тільки від Premium клієнтів
Revenue Premium = 
CALCULATE(
    [Total Revenue],
    DimCustomer[CustomerSegment] = "Premium"
)

// 2. Виручка від онлайн-каналів
Revenue Online = 
CALCULATE(
    [Total Revenue],
    DimChannel[ChannelType] = "Online"
)

// 3. Виручка від смартфонів
Revenue Smartphones = 
CALCULATE(
    [Total Revenue],
    DimProduct[Category] = "Смартфони"
)

// 4. Частка виручки від категорії
Category Revenue % = 
DIVIDE(
    [Total Revenue],
    CALCULATE(
        [Total Revenue],
        ALL(DimProduct[Category])
    ),
    0
) * 100

// 5. Виручка за вихідні дні
Revenue Weekends = 
CALCULATE(
    [Total Revenue],
    DimDate[IsWeekend] = TRUE
)

// 6. Виручка за робочі дні
Revenue Weekdays = 
CALCULATE(
    [Total Revenue],
    DimDate[IsWeekend] = FALSE
)
```

---

**3.2. Top N та ранжування:**

```DAX
// 1. Виручка від Топ-10 клієнтів
Revenue Top 10 Customers = 
CALCULATE(
    [Total Revenue],
    TOPN(
        10,
        ALL(DimCustomer[CustomerKey]),
        [Total Revenue],
        DESC
    )
)

// 2. Ранг клієнта за виручкою
Customer Revenue Rank = 
RANKX(
    ALL(DimCustomer[FullName]),
    [Total Revenue],
    ,
    DESC,
    DENSE
)

// 3. Виручка від Топ-5 товарів
Revenue Top 5 Products = 
CALCULATE(
    [Total Revenue],
    TOPN(
        5,
        ALL(DimProduct[ProductName]),
        [Total Revenue],
        DESC
    )
)

// 4. Чи товар входить в Топ-10?
Is Top 10 Product = 
VAR ProductRank = 
    RANKX(
        ALL(DimProduct[ProductName]),
        [Total Revenue],
        ,
        DESC
    )
RETURN
    IF(ProductRank <= 10, "Топ-10", "Інші")
```

---

**3.3. Парето аналіз (80/20):**

```DAX
// 1. Накопичувальна виручка по клієнтах
Cumulative Revenue = 
VAR CurrentCustomer = MAX(DimCustomer[CustomerKey])
RETURN
CALCULATE(
    [Total Revenue],
    FILTER(
        ALL(DimCustomer[CustomerKey]),
        CALCULATE([Total Revenue]) >= 
        CALCULATE([Total Revenue], DimCustomer[CustomerKey] = CurrentCustomer)
    )
)

// 2. Накопичувальний % виручки
Cumulative Revenue % = 
DIVIDE(
    [Cumulative Revenue],
    CALCULATE([Total Revenue], ALL(DimCustomer)),
    0
)

// 3. ABC класифікація
Customer ABC Class = 
VAR CumPct = [Cumulative Revenue %]
RETURN
    SWITCH(
        TRUE(),
        CumPct <= 0.80, "A - Топ 80%",
        CumPct <= 0.95, "B - Наступні 15%",
        "C - Останні 5%"
    )
```

---

#### **Завдання 4: Calculated Columns vs Measures (30 хв)**

**4.1. Коли використовувати Calculated Columns:**

```DAX
// ✅ ПРАВИЛЬНО: Calculated Column
// Використовуйте для статичних атрибутів

// В таблиці DimProduct:
Product Price Range = 
SWITCH(
    TRUE(),
    DimProduct[UnitPrice] < 5000, "Бюджетний (< 5000)",
    DimProduct[UnitPrice] < 20000, "Середній (5000-20000)",
    "Преміум (> 20000)"
)

// В таблиці FactSales:
Order Total Items = 
CALCULATE(
    COUNT(FactSales[OrderItemID]),
    ALLEXCEPT(FactSales, FactSales[OrderID])
)
```

**4.2. Коли використовувати Measures:**

```DAX
// ✅ ПРАВИЛЬНО: Measure
// Використовуйте для динамічних розрахунків

Total Revenue with Filter = 
CALCULATE(
    SUM(FactSales[Revenue]),
    // Динамічно змінюється залежно від фільтрів
)

// ❌ НЕПРАВИЛЬНО: Calculated Column для агрегацій
// НЕ робіть так:
// Total Revenue CC = SUM(FactSales[Revenue])
// Це створить однакове значення в кожному рядку!
```

---

#### **Завдання 5: Створення аналітичного звіту з DAX (45 хв)**

**Створіть нову сторінку "Time Intelligence Analysis"**

**5.1. Matrix - YoY аналіз по місяцях:**

```
Visual: Matrix
Rows: DimDate[Year], DimDate[MonthName]
Values:
  - [Total Revenue]
  - [Revenue PY]
  - [Revenue YoY Change]
  - [Revenue YoY %]

Conditional Formatting на [Revenue YoY %]:
- Data bars: Green (positive) / Red (negative)
- Font color: Green > 0, Red < 0
```

---

**5.2. Line Chart - YTD порівняння:**

```
Visual: Line Chart
Axis: DimDate[MonthName]
Values:
  - [Revenue YTD] (синя лінія)
  - [Revenue YTD PY] (сіра пунктирна)
Legend: Auto

Title: "Накопичувальна виручка: поточний рік vs минулий"
```

---

**5.3. KPI Visual - Головні показники:**

```
Visual: KPI
Indicator: [Total Revenue]
Trend axis: DimDate[MonthName]
Target goals: [Revenue PY] * 1.1  // +10% від минулого року

Formatting:
- Good color: Green
- Bad color: Red
- Distance from goal: Percentage
```

---

**5.4. Cards з Time Intelligence:**

```
4 Cards у рядок:

Card 1: Revenue YTD
- Value: [Revenue YTD]
- Trend: [Revenue YTD %]

Card 2: Revenue MTD
- Value: [Revenue MTD]
- Trend: [Revenue MoM %]

Card 3: Revenue Last 7D
- Value: [Revenue Last 7 Days]

Card 4: Average Daily Revenue
- Value: DIVIDE([Total Revenue], COUNTROWS(DimDate))
```

---

#### **Завдання 6: Оптимізація DAX (15 хв)**

**6.1. Використання змінних для продуктивності:**

```DAX
// ❌ БЕЗ змінних (обчислює двічі):
Revenue Growth = 
DIVIDE(
    [Total Revenue] - CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DimDate[Date])),
    CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DimDate[Date]))
)

// ✅ З змінними (обчислює один раз):
Revenue Growth Optimized = 
VAR CurrentRevenue = [Total Revenue]
VAR PriorRevenue = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DimDate[Date]))
RETURN
    DIVIDE(
        CurrentRevenue - PriorRevenue,
        PriorRevenue,
        0
    )
```

---

**6.2. Уникайте Calculated Columns де можливо:**

```DAX
// ❌ ПОВІЛЬНО: Calculated Column
Order Year = YEAR(FactSales[OrderDate])

// ✅ ШВИДКО: Використовуйте зв'язок з DimDate
// Просто використовуйте DimDate[Year] через зв'язок
```

---

### Контрольні питання

1. У чому різниця між Calculated Column та Measure?
2. Що таке Filter Context і Row Context?
3. Навіщо потрібна функція CALCULATE?
4. Як працює SAMEPERIODLASTYEAR?
5. Коли використовувати SUMX замість SUM?

---

### Критерії оцінювання

| Критерій | Бали |
|----------|------|
| Базові міри створені коректно | 15 |
| Time Intelligence міри (YoY, MTD, YTD) | 25 |
| CALCULATE використаний правильно | 20 |
| Top N та ранжування | 15 |
| Аналітичний звіт створено | 15 |
| Використання змінних та оптимізація | 10 |
| **ВСЬОГО** | **100** |

---

## ПРАКТИЧНА РОБОТА №5
### Тема: Power BI - Публікація і безпека (частина 3)

**Мета:** Навчитися публікувати звіти в Power BI Service та налаштовувати Row-Level Security.

**Тривалість:** 4 години

---

### Теоретична частина (40 хв)

**Power BI Service:**
- Workspace (робочі області)
- Datasets vs Reports vs Dashboards
- Refresh (оновлення даних)
- Gateway (шлюзи для on-premise даних)
- Sharing та Permissions

**Security:**
- Row-Level Security (RLS)
- Object-Level Security (OLS)
- App audiences
- Sensitivity labels

**Performance:**
- Performance Analyzer
- Query diagnostics
- Aggregations
- Incremental refresh

---

### Практична частина (3 год 20 хв)

#### **Завдання 1: Row-Level Security (RLS) (90 хв)**

**Сценарій:** Регіональні менеджери повинні бачити тільки дані свого регіону.

**1.1. Створення таблиці користувачів (30 хв)**

**В Power Query створіть таблицю UserSecurity:**

```M
let
    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i45WMlTSUQKz...", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Email = _t, Region = _t]),
    
    // Або просто ручний ввід:
    Source = Table.FromRecords({
        [Email = "manager.kyiv@techstore.ua", Region = "Київська", Role = "Regional Manager"],
        [Email = "manager.lviv@techstore.ua", Region = "Львівська", Role = "Regional Manager"],
        [Email = "manager.kharkiv@techstore.ua", Region = "Харківська", Role = "Regional Manager"],
        [Email = "manager.dnipro@techstore.ua", Region = "Дніпропетровська", Role = "Regional Manager"],
        [Email = "manager.odesa@techstore.ua", Region = "Одеська", Role = "Regional Manager"],
        [Email = "director@techstore.ua", Region = "All", Role = "Director"],
        [Email = "analyst@techstore.ua", Region = "All", Role = "Analyst"]
    }),
    
    ChangedType = Table.TransformColumnTypes(Source,{
        {"Email", type text}, 
        {"Region", type text},
        {"Role", type text}
    })
in
    ChangedType
```

**НЕ створюйте зв'язків** між UserSecurity та іншими таблицями!

---

**1.2. Створення ролей RLS (30 хв)**

**В Power BI Desktop:**

1. Modeling → Manage Roles → Create

**Роль 1: Regional Manager**
```DAX
// Table: DimCustomer
[Region] = LOOKUPVALUE(
    UserSecurity[Region],
    UserSecurity[Email],
    USERPRINCIPALNAME()
)

// Пояснення:
// USERPRINCIPALNAME() - email поточного користувача
// Шукаємо регіон цього користувача в UserSecurity
// Фільтруємо DimCustomer щоб показати тільки цей регіон
```

**Роль 2: Director (Повний доступ)**
```DAX
// Table: UserSecurity
[Role] = "Director" && 
LOOKUPVALUE(
    UserSecurity[Email],
    UserSecurity[Email],
    USERPRINCIPALNAME()
) <> BLANK()

// Директори бачать все (фільтр завжди TRUE для них)
```

**Альтернативний підхід - через Many-to-Many:**

1. Створіть зв'язок: UserSecurity[Region] ←→ DimCustomer[Region]
2. Relationship: Many-to-Many
3. Cross-filter direction: Both

**Роль: RLS via Relationship**
```DAX
// Table: UserSecurity
[Email] = USERPRINCIPALNAME()
```

---

**1.3. Тестування RLS (30 хв)**

**В Power BI Desktop:**

1. Modeling → View as Roles
2. Виберіть Role: Regional Manager
3. Other user: manager.kyiv@techstore.ua

**Перевірте:**
- Чи відображаються тільки дані Київської області?
- Чи працюють всі візуали коректно?
- Чи KPI cards показують правильні суми?

**Створіть тестову сторінку "RLS Test":**

```
Visual: Table
Columns:
  - DimCustomer[Region]
  - DimCustomer[CustomerID] (Count)
  - FactSales[Revenue] (Sum)

Slicer:
  - DimCustomer[Region]

Card:
  - Total Revenue (повинна змінюватись для різних ролей)
```

**Протестуйте для кожної ролі:**
- Regional Manager (Київ) → тільки Київська
- Regional Manager (Львів) → тільки Львівська  
- Director → всі регіони

---

#### **Завдання 2: Performance Analyzer (45 хв)**

**2.1. Аналіз продуктивності звіту (30 хв)**

1. View → Performance Analyzer → Start Recording

2. Refresh Visuals (оновіть всі візуали)

3. Проаналізуйте результати:

```
Metrics для кожного візуала:
- DAX Query (час виконання DAX)
- Visual Display (час відображення)
- Other (інше)

🔴 Проблемні візуали: Total time > 1000 ms
🟡 Повільні: 500-1000 ms
🟢 Швидкі: < 500 ms
```

**Знайдіть TOP-3 найповільніші візуали**

---

**2.2. Оптимізація (15 хв)**

**Для повільних візуалів:**

1. **Перевірте DAX:**
   - Чи є Calculated Columns? Замініть на Measures
   - Чи є вкладені CALCULATE? Оптимізуйте
   - Використовуйте змінні (VAR)

2. **Перевірте візуал:**
   - Чи занадто багато точок даних? Додайте агрегацію
   - Чи потрібні всі колонки? Видаліть зайві
   - Чи налаштовані формати? Вимкніть зайві

3. **Приклад оптимізації:**

```DAX
// ❌ ПОВІЛЬНО
Sales by Date = 
CALCULATE(
    SUM(FactSales[Revenue]),
    FILTER(
        ALL(DimDate),
        DimDate[Date] <= MAX(DimDate[Date])
    )
)

// ✅ ШВИДКО
Sales by Date Optimized = 
VAR MaxDate = MAX(DimDate[Date])
RETURN
CALCULATE(
    SUM(FactSales[Revenue]),
    DimDate[Date] <= MaxDate
)
```

**Повторіть Performance Analyzer після оптимізації**

---

#### **Завдання 3: Публікація в Power BI Service (60 хв)**

**3.1. Підготовка до публікації (15 хв)**

**Чек-ліст перед публікацією:**

✅ Модель даних оптимізована
✅ DAX міри перевірені
✅ RLS налаштовано і протестовано
✅ Візуали відформатовані
✅ Немає помилок у запитах
✅ Файл збережено

**Optimization:**
1. File → Options → Data Load
   - ❌ Import relationships from data sources on first load
   - ✅ Update or delete relationships when refreshing data

2. Transform Data → Close & Apply
   - Видаліть невикористані запити
   - Видаліть непотрібні колонки

---

**3.2. Публікація (15 хв)**

1. **Sign in to Power BI Service:**
   - Home → Sign in
   - Використайте організаційний email

2. **Publish:**
   - Home → Publish
   - Select destination: "My Workspace" (або створіть новий)
   - Зачекайте завершення публікації

3. **Після публікації:**
   - Натисніть "Open [filename] in Power BI"
   - Відкриється у браузері

---

**3.3. Налаштування Dataset (30 хв)**

**В Power BI Service:**

1. **Settings → Datasets → [ваш dataset]**

**3.3.1. Налаштування Refresh:**

```
Gateway connection:
- [Якщо дані on-premise] Configure gateway
- [Якщо дані в хмарі] Skip

Credentials:
- Source credentials → Edit credentials
- Privacy level: Organizational
- Sign in (якщо потрібно)

Scheduled refresh:
- Keep your data up to date: ON
- Refresh frequency: Daily
- Time: 06:00, 18:00
- Send refresh failure notification: ON
- Email: your@email.com
```

**3.3.2. Parameters (якщо є):**

```
Parameters:
- [якщо є параметри] Edit values
- DataSourcePath = "C:\Data\" → змініть на хмарний шлях
```

---

#### **Завдання 4: Налаштування безпеки в Service (45 хв)**

**4.1. Призначення ролей RLS (25 хв)**

1. **Settings → Datasets → Security**

2. **Row-Level Security:**

```
Role: Regional Manager
Members: 
  - manager.kyiv@techstore.ua
  - manager.lviv@techstore.ua
  - manager.kharkiv@techstore.ua
  - manager.dnipro@techstore.ua
  - manager.odesa@techstore.ua

Role: Director
Members:
  - director@techstore.ua
  - ceo@techstore.ua
```

3. **Save**

---

**4.2. Тестування RLS в Service (10 хв)**

1. **Settings → Datasets → Security**
2. **Test as role:**
   - Role: Regional Manager
   - User: manager.kyiv@techstore.ua
   - Test

**Відкриється звіт у режимі тестування**

Перевірте чи працює фільтрація коректно

---

**4.3. Sharing (10 хв)**

**Варіант 1: Direct Share**
1. Відкрийте звіт
2. Share → Get a link
3. Link settings:
   - People in your organization
   - Can view
   - ✅ Allow recipients to share
   - ❌ Allow recipients to build content
4. Apply → Copy link

**Варіант 2: App**
1. Workspace → Create app
2. Setup:
   - Name: "TechStore Analytics"
   - Description: "Аналітика продажів TechStore"
   - Logo: [завантажте логотип]
3. Content:
   - ✅ Sales Overview
   - ✅ Customer Analysis
   - ✅ Time Intelligence
4. Audience:
   - Specific individuals: analyst@techstore.ua
   - Or: Entire organization
5. Permissions:
   - ✅ Viewers can share this app
   - ❌ Allow users to make a copy of the reports
6. Publish app

---

#### **Завдання 5: Mobile Layout (Optional, 20 хв)**

**5.1. Створення Mobile View (20 хв)**

1. View → Mobile Layout

2. **Phone Layout для "Sales Overview":**

```
Vertical layout (9:16):
+------------------+
|  [Year Filter]   |
|  [Category]      |
+------------------+
|  [Revenue Card]  |
|  [Orders Card]   |
+------------------+
|  [Chart 1]       |
|  (Column Chart)  |
+------------------+
|  [Chart 2]       |
|  (Line Chart)    |
+------------------+
|  [Table]         |
+------------------+
```

**Drag & Drop візуали з Desktop canvas на Phone canvas**

**Resize:**
- Cards: 2 в ряд
- Charts: 1 на весь екран
- Table: прокручувана

3. **Publish** (перепублікуйте)

4. **Test:**
   - Відкрийте на телефоні через Power BI Mobile app
   - Або: F12 в браузері → Mobile view

---

### Контрольні питання

1. У чому різниця між Static RLS та Dynamic RLS?
2. Що таке Gateway і коли він потрібен?
3. Чи можна змінити RLS після публікації?
4. Як налаштувати Incremental Refresh?
5. У чому різниця між Share Report та Publish App?

---

### Критерії оцінювання

| Критерій | Бали |
|----------|------|
| RLS налаштовано коректно | 25 |
| RLS протестовано в Desktop та Service | 15 |
| Performance Analyzer використано | 10 |
| Звіт опубліковано успішно | 15 |
| Dataset налаштовано (credentials, refresh) | 15 |
| RLS призначено в Service | 10 |
| Sharing налаштовано | 5 |
| Mobile Layout (bonus) | 5 |
| **ВСЬОГО** | **100** |

---

(Продовження наступних практичних...)# ПРАКТИЧНІ РОБОТИ 6-8 (ЗАВЕРШЕННЯ)

## ПРАКТИЧНА РОБОТА №6
### Тема: Прогнозування і сценарії

**Мета:** Навчитися будувати прогнози продажів та створювати What-If сценарії.

**Тривалість:** 4 години

---

### Теоретична частина (40 хв)

**Методи прогнозування:**
- Часові ряди (Time Series)
- Exponential Smoothing
- Moving Averages
- Linear Regression
- Сезонність і тренд

**Power BI Forecasting:**
- Вбудований Forecast в Line Chart
- DAX для прогнозування
- Python/R integration

**What-If параметри:**
- Створення параметрів
- Scenarios modeling
- Sensitivity analysis

---

### Практична частина (3 год 20 хв)

#### **Завдання 1: Прогнозування продажів (90 хв)**

**1.1. Підготовка даних для прогнозу (30 хв)**

**Створіть агреговану таблицю продажів по днях:**

```M
// В Power Query
let
    Source = FactSales,
    MergeDate = Table.NestedJoin(Source, {"DateKey"}, DimDate, {"DateKey"}, "Date", JoinKind.Inner),
    ExpandDate = Table.ExpandTableColumn(MergeDate, "Date", {"Date"}),
    
    GroupByDate = Table.Group(
        ExpandDate, 
        {"Date"}, 
        {
            {"Total Revenue", each List.Sum([Revenue]), type number},
            {"Total Orders", each List.Count([OrderID]), Int64.Type},
            {"Total Quantity", each List.Sum([Quantity]), type number}
        }
    ),
    
    SortedByDate = Table.Sort(GroupByDate, {{"Date", Order.Ascending}}),
    ChangedType = Table.TransformColumnTypes(SortedByDate, {{"Date", type date}})
in
    ChangedType
```

**Назва таблиці:** DailySales

---

**1.2. Візуальний прогноз в Line Chart (20 хв)**

**Створіть новусторінку "Forecasting"**

**Line Chart з прогнозом:**

```
Visual: Line Chart
Axis: DailySales[Date]
Values: DailySales[Total Revenue]

Analytics → Forecast:
- Forecast length: 90 days (3 місяці)
- Ignore last: 0 points
- Seasonality: Auto-detect
- Confidence interval: 95%
- Style: Solid line
- Color: Orange

Formatting:
- Title: "Прогноз продажів на 90 днів"
- Data labels: Off
- Line style:
  - Actual: Blue, solid, 3px
  - Forecast: Orange, dashed, 2px
- Confidence interval: Light orange fill
```

**Додайте Trend Line:**
- Analytics → Trend Line → Add
- Style: Linear
- Color: Red, dotted

---

**1.3. DAX-прогноз (40 хв)**

**Створіть міри для простого лінійного прогнозу:**

```DAX
// 1. Базова міра - середня виручка за період
Average Daily Revenue = 
AVERAGE(DailySales[Total Revenue])

// 2. Розрахунок тренду (slope)
Sales Trend Slope = 
VAR MinDate = MIN(DimDate[Date])
VAR MaxDate = MAX(DimDate[Date])
VAR DateRange = MaxDate - MinDate + 1
VAR SumX = 
    SUMX(
        DimDate,
        (DimDate[Date] - MinDate) + 1
    )
VAR SumY = SUM(DailySales[Total Revenue])
VAR SumXY = 
    SUMX(
        DimDate,
        ((DimDate[Date] - MinDate) + 1) * 
        RELATED(DailySales[Total Revenue])
    )
VAR SumXX = 
    SUMX(
        DimDate,
        POWER((DimDate[Date] - MinDate) + 1, 2)
    )
VAR N = COUNTROWS(DimDate)
RETURN
    DIVIDE(
        (N * SumXY) - (SumX * SumY),
        (N * SumXX) - POWER(SumX, 2),
        0
    )

// 3. Intercept
Sales Trend Intercept = 
VAR Slope = [Sales Trend Slope]
VAR AvgX = 
    AVERAGE(
        SELECTCOLUMNS(
            DimDate,
            "DayNumber",
            (DimDate[Date] - MIN(DimDate[Date])) + 1
        )
    )
VAR AvgY = [Average Daily Revenue]
RETURN
    AvgY - (Slope * AvgX)

// 4. Прогноз на основі тренду
Revenue Forecast = 
VAR MinDate = CALCULATE(MIN(DimDate[Date]), ALL(DimDate))
VAR CurrentDate = MAX(DimDate[Date])
VAR DayNumber = (CurrentDate - MinDate) + 1
VAR Slope = [Sales Trend Slope]
VAR Intercept = [Sales Trend Intercept]
RETURN
    Intercept + (Slope * DayNumber)

// 5. Фактичне або прогноз
Revenue Actual or Forecast = 
IF(
    ISBLANK([Total Revenue]),
    [Revenue Forecast],
    [Total Revenue]
)

// 6. Помилка прогнозу (MAPE - Mean Absolute Percentage Error)
Forecast Error MAPE = 
VAR Actual = [Total Revenue]
VAR Forecast = [Revenue Forecast]
RETURN
    ABS(DIVIDE(Actual - Forecast, Actual)) * 100
```

---

**Створіть візуал для порівняння:**

```
Visual: Line Chart
Axis: DimDate[Date]
Values:
  - [Total Revenue] (фактичні дані, синя лінія)
  - [Revenue Forecast] (прогноз, помаранчева лінія)

Visual: Card
Value: [Forecast Error MAPE]
Format: Percentage, 2 decimal
Title: "Точність прогнозу (MAPE)"
```

---

#### **Завдання 2: Сезонний аналіз (45 хв)**

**2.1. Виявлення сезонності (25 хв)**

**Створіть міри для аналізу сезонності:**

```DAX
// 1. Індекс сезонності по місяцях
Seasonality Index = 
VAR OverallAvg = 
    CALCULATE(
        AVERAGE(DailySales[Total Revenue]),
        ALL(DimDate)
    )
VAR MonthAvg = 
    CALCULATE(
        AVERAGE(DailySales[Total Revenue]),
        ALLEXCEPT(DimDate, DimDate[Month])
    )
RETURN
    DIVIDE(MonthAvg, OverallAvg, 1)

// 2. Виручка без сезонності
Revenue Deseasonalized = 
DIVIDE(
    [Total Revenue],
    [Seasonality Index],
    0
)

// 3. Прогноз з урахуванням сезонності
Revenue Forecast Seasonal = 
[Revenue Forecast] * [Seasonality Index]
```

**Візуалізація:**

```
Visual: Clustered Column Chart
Axis: DimDate[MonthName]
Values:
  - [Seasonality Index]

Sort by: DimDate[Month]
Data labels: ON, 2 decimal places
Reference line: Value = 1.0 (середній рівень)

Title: "Індекс сезонності по місяцях"
```

---

**2.2. Heatmap сезонності (20 хв)**

**Створіть Matrix:**

```
Visual: Matrix
Rows: DimDate[Year]
Columns: DimDate[MonthName]
Values: [Total Revenue]

Conditional Formatting:
- Background color: Color scale
  - Minimum: White
  - Center: Yellow
  - Maximum: Red
  
Sort columns: DimDate[Month]

Title: "Теплова карта продажів: Рік × Місяць"
```

**Додайте міру для виділення пікових місяців:**

```DAX
Peak Month Indicator = 
VAR CurrentMonthRevenue = [Total Revenue]
VAR MaxMonthRevenue = 
    MAXX(
        ALL(DimDate[MonthName]),
        [Total Revenue]
    )
RETURN
    IF(
        CurrentMonthRevenue = MaxMonthRevenue,
        "🔥 Пік",
        ""
    )
```

---

#### **Завдання 3: What-If параметри (75 хв)**

**3.1. Створення What-If параметрів (30 хв)**

**Параметр 1: Зростання цін (%)**

1. Modeling → New Parameter

```
Name: Price Increase %
Data type: Decimal number
Minimum: -20
Maximum: 50
Increment: 5
Default: 0
Format: Percentage
Add slicer to this page: ✅
```

**Параметр 2: Зростання попиту (%)**

```
Name: Demand Growth %
Minimum: -30
Maximum: 100
Increment: 10
Default: 10
```

**Параметр 3: Маркетинговий бюджет (грн)**

```
Name: Marketing Budget
Data type: Whole number
Minimum: 0
Maximum: 500000
Increment: 50000
Default: 100000
Format: Currency
```

---

**3.2. Сценарне моделювання (45 хв)**

**Створіть міри для сценаріїв:**

```DAX
// 1. Нова ціна з урахуванням параметру
New Price = 
VAR CurrentPrice = AVERAGE(DimProduct[UnitPrice])
VAR PriceAdjustment = SELECTEDVALUE('Price Increase %'[Price Increase %], 0)
RETURN
    CurrentPrice * (1 + PriceAdjustment)

// 2. Новий попит (еластичність попиту = -0.5)
New Demand Quantity = 
VAR CurrentQuantity = SUM(FactSales[Quantity])
VAR PriceChange = SELECTEDVALUE('Price Increase %'[Price Increase %], 0)
VAR DemandGrowth = SELECTEDVALUE('Demand Growth %'[Demand Growth %], 0)
VAR PriceElasticity = -0.5
RETURN
    CurrentQuantity * 
    (1 + DemandGrowth) * 
    (1 + (PriceChange * PriceElasticity))

// 3. Прогнозована виручка
Projected Revenue = 
[New Price] * [New Demand Quantity]

// 4. Зміна виручки vs базовий сценарій
Revenue Change vs Base = 
[Projected Revenue] - [Total Revenue]

// 5. Зміна у %
Revenue Change % = 
DIVIDE(
    [Revenue Change vs Base],
    [Total Revenue],
    0
) * 100

// 6. ROI від маркетингу (припускаємо 15% конверсія)
Marketing ROI = 
VAR Budget = SELECTEDVALUE('Marketing Budget'[Marketing Budget], 0)
VAR AdditionalRevenue = Budget * 0.15
VAR Profit = AdditionalRevenue * 0.25  // 25% маржа
RETURN
    DIVIDE(Profit, Budget, 0) * 100
```

---

**Створіть Dashboard "Scenario Planning":**

**Layout:**

```
+--------------------------------------------+
|  What-If Parameters (Slicers)              |
|  [Price Increase %] [Demand Growth %]      |
|  [Marketing Budget]                        |
+--------------------------------------------+
|  KPI Cards:                                |
|  [Projected Revenue] [Revenue Change %]    |
|  [Marketing ROI]                           |
+--------------------------------------------+
|  Waterfall Chart: Revenue Components       |
|  (Base → Price → Demand → Marketing)       |
+--------------------------------------------+
|  Sensitivity Table:                        |
|  Price × Demand matrix                     |
+--------------------------------------------+
```

---

**Waterfall Chart:**

```
Visual: Waterfall Chart
Category:
  - "Базова виручка"
  - "Вплив ціни"
  - "Вплив попиту"
  - "Вплив маркетингу"
  - "Прогнозована виручка"

Y Axis:
  - Міри для кожної категорії

Formatting:
- Increase bars: Green
- Decrease bars: Red
- Total bars: Blue
```

---

**Sensitivity Analysis Matrix:**

```
Visual: Matrix
Rows: Price Increase % (-20%, -10%, 0%, 10%, 20%)
Columns: Demand Growth % (-20%, 0%, 20%, 40%, 60%)
Values: [Projected Revenue]

Створіть Calculated Table:
SensitivityMatrix = 
CROSSJOIN(
    VALUES('Price Increase %'[Price Increase %]),
    VALUES('Demand Growth %'[Demand Growth %])
)

Conditional Formatting:
- Green: Revenue increase > 20%
- Yellow: Revenue increase 0-20%
- Red: Revenue decrease
```

---

#### **Завдання 4: Оптимізація сценаріїв (30 хв)**

**Знайдіть оптимальну комбінацію параметрів:**

**Створіть таблицю оптимізації:**

```DAX
Optimization Score = 
VAR RevenueWeight = 0.5
VAR ROIWeight = 0.3
VAR RiskWeight = 0.2

VAR RevenueScore = 
    DIVIDE([Revenue Change %], 100, 0)
    
VAR ROIScore = 
    DIVIDE([Marketing ROI], 100, 0)
    
VAR RiskScore = 
    1 - ABS(SELECTEDVALUE('Price Increase %'[Price Increase %], 0))

RETURN
    (RevenueScore * RevenueWeight) +
    (ROIScore * ROIWeight) +
    (RiskScore * RiskWeight)
```

**Візуал:**

```
Visual: Table
Columns:
  - Price Increase %
  - Demand Growth %
  - Marketing Budget
  - Projected Revenue
  - Revenue Change %
  - Marketing ROI
  - Optimization Score

Sort by: Optimization Score (Descending)
Top N filter: 10 scenarios

Conditional Formatting:
- Optimization Score: Data bars (green)
```

---

### Контрольні питання

1. Які методи прогнозування ви знаєте?
2. Що таке сезонність і як її врахувати в прогнозі?
3. Навіщо потрібні What-If параметри?
4. Що таке еластичність попиту за ціною?
5. Як оцінити точність прогнозу?

---

### Критерії оцінювання

| Критерій | Бали |
|----------|------|
| Підготовка даних для прогнозу | 10 |
| Візуальний прогноз у Line Chart | 15 |
| DAX-прогноз створено | 20 |
| Аналіз сезонності виконано | 15 |
| What-If параметри створені | 15 |
| Сценарне моделювання працює | 15 |
| Optimization analysis | 10 |
| **ВСЬОГО** | **100** |

---

## ПРАКТИЧНА РОБОТА №7
### Тема: Аналіз ефективності бізнесу за KPI

**Мета:** Розробити систему KPI та візуалізувати показники ефективності.

**Тривалість:** 4 години

---

### Теоретична частина (40 хв)

**KPI (Key Performance Indicators):**
- Фінансові KPI
- Операційні KPI
- Клієнтські KPI
- SMART критерії для KPI

**Balanced Scorecard:**
- Фінансова перспектива
- Клієнтська перспектива
- Внутрішні процеси
- Навчання і розвиток

**Метрики e-commerce:**
- CAC (Customer Acquisition Cost)
- LTV (Lifetime Value)
- Churn Rate
- AOV (Average Order Value)
- Conversion Rate

---

### Практична частина (3 год 20 хв)

#### **Завдання 1: Визначення KPI для TechStore (40 хв)**

**1.1. Фінансові KPI (15 хв)**

```DAX
// 1. Виручка
KPI Revenue = [Total Revenue]

// 2. Прибуток
KPI Profit = [Total Profit]

// 3. Маржинальність
KPI Profit Margin = [Profit Margin %]

// 4. EBITDA (спрощена)
KPI EBITDA = 
VAR GrossProfit = [Total Profit]
VAR OperatingExpenses = [Total Revenue] * 0.15  // 15% від виручки
RETURN
    GrossProfit - OperatingExpenses

// 5. ROI
KPI ROI = 
DIVIDE([Total Profit], [Total Revenue], 0) * 100

// 6. Темп зростання виручки YoY
KPI Revenue Growth YoY = [Revenue YoY %]
```

---

**1.2. Клієнтські KPI (25 хв)**

```DAX
// 1. CAC (Customer Acquisition Cost)
KPI CAC = 
VAR MarketingCost = SUMX(MarketingCampaigns, [budget])
VAR NewCustomers = 
    CALCULATE(
        DISTINCTCOUNT(FactSales[CustomerKey]),
        DimDate[Year] = YEAR(TODAY())
    )
RETURN
    DIVIDE(MarketingCost, NewCustomers, 0)

// 2. LTV (Customer Lifetime Value) - спрощений
KPI LTV = 
VAR AvgOrderValue = [Average Order Value]
VAR AvgOrdersPerYear = 
    DIVIDE(
        COUNTROWS(FactSales),
        DISTINCTCOUNT(FactSales[CustomerKey]) * 3,  // 3 роки історії
        0
    )
VAR AvgCustomerLifetime = 3  // роки
VAR ProfitMargin = [Profit Margin %] / 100
RETURN
    AvgOrderValue * AvgOrdersPerYear * AvgCustomerLifetime * ProfitMargin

// 3. LTV/CAC Ratio
KPI LTV to CAC = 
DIVIDE([KPI LTV], [KPI CAC], 0)

// 4. Churn Rate (% клієнтів без покупок >6 міс)
KPI Churn Rate = 
VAR TotalCustomers = DISTINCTCOUNT(DimCustomer[CustomerKey])
VAR InactiveCustomers = 
    CALCULATE(
        COUNTROWS(
            FILTER(
                DimCustomer,
                CALCULATE(
                    MAX(FactSales[OrderDate]),
                    RELATEDTABLE(FactSales)
                ) < TODAY() - 180  // 6 місяців
            )
        )
    )
RETURN
    DIVIDE(InactiveCustomers, TotalCustomers, 0) * 100

// 5. Customer Retention Rate
KPI Retention Rate = 100 - [KPI Churn Rate]

// 6. NPS (Net Promoter Score) - з відгуків
KPI NPS = 
VAR Promoters = 
    CALCULATE(
        COUNT(ProductReviews[review_id]),
        ProductReviews[rating] >= 4.5
    )
VAR Detractors = 
    CALCULATE(
        COUNT(ProductReviews[review_id]),
        ProductReviews[rating] <= 3
    )
VAR TotalResponses = COUNT(ProductReviews[review_id])
RETURN
    DIVIDE(Promoters - Detractors, TotalResponses, 0) * 100

// 7. Average Customer Rating
KPI Avg Rating = AVERAGE(ProductReviews[rating])

// 8. Repeat Customer Rate
KPI Repeat Rate = 
VAR CustomersWithMultipleOrders = 
    COUNTROWS(
        FILTER(
            SUMMARIZE(
                FactSales,
                FactSales[CustomerKey],
                "OrderCount", DISTINCTCOUNT(FactSales[OrderID])
            ),
            [OrderCount] > 1
        )
    )
VAR TotalCustomers = DISTINCTCOUNT(FactSales[CustomerKey])
RETURN
    DIVIDE(CustomersWithMultipleOrders, TotalCustomers, 0) * 100
```

---

#### **Завдання 2: Операційні KPI (40 хв)**

**2.1. Логістика та виконання (20 хв)**

```DAX
// 1. Середній час доставки (днів)
KPI Avg Delivery Time = 
AVERAGEX(
    FILTER(FactSales, NOT(ISBLANK(FactSales[DeliveryDate]))),
    FactSales[DeliveryDate] - FactSales[ShippingDate]
)

// 2. On-Time Delivery Rate
KPI On Time Delivery = 
VAR OnTimeOrders = 
    CALCULATE(
        COUNT(FactSales[OrderID]),
        FactSales[DeliveryDate] - FactSales[ShippingDate] <= 5  // 5 днів SLA
    )
VAR TotalDelivered = 
    CALCULATE(
        COUNT(FactSales[OrderID]),
        NOT(ISBLANK(FactSales[DeliveryDate]))
    )
RETURN
    DIVIDE(OnTimeOrders, TotalDelivered, 0) * 100

// 3. Order Fulfillment Rate
KPI Order Fulfillment = 
VAR Delivered = 
    CALCULATE(
        COUNT(FactSales[OrderID]),
        FactSales[OrderStatus] = "Delivered"
    )
VAR TotalOrders = COUNT(FactSales[OrderID])
RETURN
    DIVIDE(Delivered, TotalOrders, 0) * 100

// 4. Cancellation Rate
KPI Cancellation Rate = 
DIVIDE(
    CALCULATE(COUNT(FactSales[OrderID]), FactSales[OrderStatus] = "Cancelled"),
    COUNT(FactSales[OrderID]),
    0
) * 100

// 5. Return Rate
KPI Return Rate = 
DIVIDE(
    CALCULATE(COUNT(FactSales[OrderID]), FactSales[OrderStatus] = "Returned"),
    CALCULATE(COUNT(FactSales[OrderID]), FactSales[OrderStatus] = "Delivered"),
    0
) * 100
```

---

**2.2. Інвентаризація (20 хв)**

```DAX
// 1. Inventory Turnover (оборотність запасів)
KPI Inventory Turnover = 
VAR COGS = SUM(FactSales[Cost])
VAR AvgInventoryValue = AVERAGE(DimProduct[CostPrice]) * AVERAGE(DimProduct[InStock])
RETURN
    DIVIDE(COGS, AvgInventoryValue, 0)

// 2. Days Inventory Outstanding (DIO)
KPI Days Inventory = 
DIVIDE(365, [KPI Inventory Turnover], 0)

// 3. Stock-Out Rate
KPI Stock Out Rate = 
VAR OutOfStock = 
    COUNTROWS(
        FILTER(DimProduct, DimProduct[InStock] = 0)
    )
VAR TotalProducts = COUNTROWS(DimProduct)
RETURN
    DIVIDE(OutOfStock, TotalProducts, 0) * 100

// 4. Sell-Through Rate
KPI Sell Through = 
VAR Sold = SUM(FactSales[Quantity])
VAR Available = SUM(DimProduct[InStock]) + Sold
RETURN
    DIVIDE(Sold, Available, 0) * 100
```

---

#### **Завдання 3: Створення Balanced Scorecard (90 хв)**

**Створіть нову сторінку "Balanced Scorecard"**

**3.1. Layout (4 квадранти) (30 хв)**

```
+----------------------+----------------------+
|   ФІНАНСОВА          |   КЛІЄНТСЬКА         |
|   ПЕРСПЕКТИВА        |   ПЕРСПЕКТИВА        |
|                      |                      |
|  💰 Revenue          |  👥 CAC              |
|  📈 Profit Margin    |  💝 LTV/CAC          |
|  📊 Revenue Growth   |  ⭐ NPS              |
|                      |  🔄 Retention        |
+----------------------+----------------------+
|   ВНУТРІШНІ          |   НАВЧАННЯ &         |
|   ПРОЦЕСИ            |   РОЗВИТОК           |
|                      |                      |
|  🚚 On-Time Delivery |  📚 Training Hours   |
|  📦 Order Fulfillment|  👨‍💼 Employee Sat    |
|  🔄 Inventory Turn   |  💡 Innovation       |
|                      |                      |
+----------------------+----------------------+
```

---

**3.2. Фінансова перспектива (15 хв)**

```
Visual: Multi-row Card
Values:
  - KPI Revenue (format: K грн)
  - KPI Profit (format: K грн)
  - KPI Profit Margin (format: %)
  - KPI Revenue Growth YoY (format: %)

Visual: Gauge
Value: KPI Revenue
Target: [KPI Revenue] * 1.2  // +20% target
Maximum: [KPI Revenue] * 1.5

Visual: Line Chart (Trend)
Axis: DimDate[MonthName]
Values:
  - KPI Revenue (current year)
  - Revenue PY

Title: "💰 Фінансова перспектива"
Background: Light blue (#E3F2FD)
```

---

**3.3. Клієнтська перспектива (15 хв)**

```
Visual: Multi-row Card
Values:
  - KPI CAC (format: K грн)
  - KPI LTV (format: K грн)
  - KPI LTV to CAC (format: ratio, 1 decimal)
  - KPI NPS (format: whole number)
  - KPI Retention Rate (format: %)

Visual: Donut Chart
Legend: Customer Segment
Values: Active Customers count

Visual: KPI Card
Indicator: KPI NPS
Target: 50 (good NPS)
Trend axis: DimDate[Quarter]

Title: "👥 Клієнтська перспектива"
Background: Light green (#E8F5E9)
```

---

**3.4. Внутрішні процеси (15 хв)**

```
Visual: Multi-row Card
Values:
  - KPI On Time Delivery (format: %)
  - KPI Order Fulfillment (format: %)
  - KPI Cancellation Rate (format: %)
  - KPI Return Rate (format: %)
  - KPI Inventory Turnover (format: 1 decimal)

Visual: Clustered Column Chart
Axis: DimLocation[LocationName]
Values:
  - KPI On Time Delivery
  - KPI Order Fulfillment

Sort by: KPI On Time Delivery (Desc)

Title: "🔧 Внутрішні процеси"
Background: Light orange (#FFF3E0)
```

---

**3.5. Навчання & Розвиток (15 хв)**

```
// Створіть міри (якщо є дані про співробітників):

KPI Employee Satisfaction = 75  // Приклад

KPI Training Hours per Employee = 40  // Приклад

KPI Innovation Projects = 5  // Приклад

Visual: Multi-row Card
Values:
  - KPI Employee Satisfaction
  - KPI Training Hours per Employee
  - KPI Innovation Projects

Visual: Card with Image
- Icon: 📚
- Value: "Continuous Learning"

Title: "📈 Навчання & Розвиток"
Background: Light purple (#F3E5F5)
```

---

#### **Завдання 4: Dashboard KPI з цільовими показниками (50 хв)**

**Створіть сторінку "KPI Dashboard"**

**4.1. Таблиця KPI з цілями (30 хв)**

**Створіть таблицю цільових показників:**

```DAX
// Calculated Table
KPI Targets = 
{
    ("Revenue", 10000000, "грн", "Фінансова"),
    ("Profit Margin", 25, "%", "Фінансова"),
    ("CAC", 500, "грн", "Клієнтська"),
    ("LTV/CAC", 3, "ratio", "Клієнтська"),
    ("NPS", 50, "score", "Клієнтська"),
    ("Retention Rate", 80, "%", "Клієнтська"),
    ("On-Time Delivery", 95, "%", "Процеси"),
    ("Order Fulfillment", 98, "%", "Процеси"),
    ("Inventory Turnover", 8, "times", "Процеси")
}

// Columns: KPI Name, Target Value, Unit, Category
```

**Створіть міру для порівняння:**

```DAX
KPI Actual Value = 
SWITCH(
    SELECTEDVALUE(KPI_Targets[KPI Name]),
    "Revenue", [KPI Revenue],
    "Profit Margin", [KPI Profit Margin],
    "CAC", [KPI CAC],
    "LTV/CAC", [KPI LTV to CAC],
    "NPS", [KPI NPS],
    "Retention Rate", [KPI Retention Rate],
    "On-Time Delivery", [KPI On Time Delivery],
    "Order Fulfillment", [KPI Order Fulfillment],
    "Inventory Turnover", [KPI Inventory Turnover],
    BLANK()
)

KPI Achievement % = 
DIVIDE(
    [KPI Actual Value],
    SELECTEDVALUE(KPI_Targets[Target Value]),
    0
) * 100

KPI Status = 
VAR Achievement = [KPI Achievement %]
RETURN
    SWITCH(
        TRUE(),
        Achievement >= 100, "🟢 Досягнуто",
        Achievement >= 80, "🟡 В процесі",
        "🔴 Відстає"
    )
```

---

**4.2. Візуалізація KPI Table (20 хв)**

```
Visual: Table
Columns:
  - KPI Targets[Category]
  - KPI Targets[KPI Name]
  - [KPI Actual Value]
  - KPI Targets[Target Value]
  - [KPI Achievement %]
  - [KPI Status]

Group by: Category

Conditional Formatting:
- KPI Achievement %:
  - >=100%: Green background
  - 80-100%: Yellow background
  - <80%: Red background

- Data bars на KPI Achievement %

Sort by: Category, then KPI Name

Title: "📊 KPI Dashboard - Огляд досягнення цілей"
```

---

### Контрольні питання

1. Що таке KPI і як їх правильно визначати?
2. Що таке Balanced Scorecard?
3. У чому різниця між leading та lagging indicators?
4. Як розрахувати LTV та CAC?
5. Що таке NPS і як його інтерпретувати?

---

### Критерії оцінювання

| Критерій | Бали |
|----------|------|
| Фінансові KPI створені | 15 |
| Клієнтські KPI (CAC, LTV, NPS, Retention) | 20 |
| Операційні KPI (Delivery, Fulfillment) | 15 |
| Balanced Scorecard з 4 квадрантами | 25 |
| KPI Dashboard з цілями | 15 |
| Conditional Formatting та статуси | 10 |
| **ВСЬОГО** | **100** |

---

## ПРАКТИЧНА РОБОТА №8
### Тема: Наскрізний проєкт з бізнес-аналітики

**Мета:** Створити комплексне BI-рішення від бізнес-задачі до готового дашборду.

**Тривалість:** 4 години (фінальний проєкт)

---

### Структура проєкту

#### Етап 1: Постановка бізнес-задачі (30 хв)

**Сценарій:**

TechStore планує **відкрити новий пункт видачі** в одному з міст та хоче вибрати найкращу локацію на основі даних.

**Бізнес-питання:**
1. В якому регіоні найбільший потенціал зростання?
2. Які категорії товарів найпопулярніші в різних регіонах?
3. Який профіль клієнтів у кожному регіоні?
4. Яка прогнозована виручка від нового пункту?
5. Який ROI від відкриття нового пункту?

**Завдання студентів:**
- Визначити ключові метрики для прийняття рішення
- Створити BPMN-схему процесу аналізу
- Окреслити необхідні дані

---

#### Етап 2: BPMN-схема процесу (30 хв)**

**Створіть BPMN-діаграму процесу аналізу:**

```
[Початок] 
    ↓
[Збір даних про регіони]
    ↓
[Аналіз поточних продажів]
    ↓
<Є потенціал?>  → НІ → [Аналіз бар'єрів]
    ↓ ТАК
[Аналіз конкуренції]
    ↓
[Прогнозування попиту]
    ↓
[Розрахунок ROI]
    ↓
<ROI > 20%?>  → НІ → [Відхилити]
    ↓ ТАК
[Рекомендація локації]
    ↓
[Кінець]
```

**Tools:** draw.io, Lucidchart, або PowerPoint

---

#### Етап 3: Моделювання даних (40 хв)

**3.1. Розширення моделі (20 хв)**

**Додайте нові таблиці:**

```
DimCompetitors (Конкуренти)
- CompetitorID
- CompetitorName
- City
- Region
- EstimatedRevenue
- StoreCount
- Rating

DimPotentialLocations (Потенційні локації)
- LocationID
- City
- Region
- Population
- AvgIncome
- CompetitorCount
- RentCost (грн/м²)
- TrafficIndex (1-10)
```

**Створіть дані вручну або згенеруйте:**

```M
DimPotentialLocations = 
Table.FromRecords({
    [LocationID = 1, City = "Вінниця", Region = "Вінницька", Population = 370000, AvgIncome = 15000, CompetitorCount = 3, RentCost = 400, TrafficIndex = 7],
    [LocationID = 2, City = "Полтава", Region = "Полтавська", Population = 280000, AvgIncome = 14000, CompetitorCount = 2, RentCost = 350, TrafficIndex = 6],
    [LocationID = 3, City = "Чернівці", Region = "Чернівецька", Population = 265000, AvgIncome = 13000, CompetitorCount = 1, RentCost = 300, TrafficIndex = 5],
    [LocationID = 4, City = "Житомир", Region = "Житомирська", Population = 260000, AvgIncome = 13500, CompetitorCount = 2, RentCost = 320, TrafficIndex = 6]
})
```

---

**3.2. Оновлення зв'язків (20 хв)**

- DimPotentialLocations не зв'язується з FactSales (це нові локації)
- Використовуйте DAX для прогнозних розрахунків

---

#### Етап 4: DAX-міри для аналізу (60 хв)

**4.1. Аналіз поточних регіонів (25 хв)**

```DAX
// 1. Виручка на душу населення
Revenue per Capita = 
DIVIDE(
    [Total Revenue],
    RELATED(DimPotentialLocations[Population]),
    0
)

// 2. Середній чек по регіонах
Avg Order Value by Region = 
CALCULATE(
    [Average Order Value],
    ALLEXCEPT(DimCustomer, DimCustomer[Region])
)

// 3. Проникнення ринку (Market Penetration)
Market Penetration % = 
VAR ActiveCustomers = [Active Customers]
VAR TotalPopulation = SUM(DimPotentialLocations[Population])
RETURN
    DIVIDE(ActiveCustomers, TotalPopulation, 0) * 100

// 4. Частка в категорії
Category Share % = 
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALLEXCEPT(DimProduct, DimProduct[Category])),
    0
) * 100

// 5. Індекс конкуренції
Competition Index = 
VAR CompCount = RELATED(DimPotentialLocations[CompetitorCount])
RETURN
    SWITCH(
        TRUE(),
        CompCount = 0, "Низька",
        CompCount <= 2, "Середня",
        "Висока"
    )
```

---

**4.2. Прогнозування для нових локацій (35 хв)**

```DAX
// 1. Estimated Market Size
Estimated Market Size = 
VAR Population = SELECTEDVALUE(DimPotentialLocations[Population])
VAR AvgIncome = SELECTEDVALUE(DimPotentialLocations[AvgIncome])
VAR CategorySpendRate = 0.05  // 5% доходу на електроніку
RETURN
    Population * AvgIncome * CategorySpendRate * 12  // річний потенціал

// 2. Прогнозована частка ринку
Projected Market Share = 
VAR TrafficIndex = SELECTEDVALUE(DimPotentialLocations[TrafficIndex])
VAR CompetitorCount = SELECTEDVALUE(DimPotentialLocations[CompetitorCount])
VAR BaseShare = 0.15  // 15% базова частка
VAR TrafficBonus = TrafficIndex * 0.01
VAR CompPenalty = CompetitorCount * 0.02
RETURN
    BaseShare + TrafficBonus - CompPenalty

// 3. Projected Revenue (1st year)
Projected Revenue Year 1 = 
[Estimated Market Size] * [Projected Market Share]

// 4. Projected Revenue (Year 2-3 with growth)
Projected Revenue Year 2 = 
[Projected Revenue Year 1] * 1.20  // +20% growth

Projected Revenue Year 3 = 
[Projected Revenue Year 2] * 1.15  // +15% growth

// 5. Total 3-Year Revenue
Projected Revenue 3Y Total = 
[Projected Revenue Year 1] + 
[Projected Revenue Year 2] + 
[Projected Revenue Year 3]

// 6. Operating Costs
Estimated Operating Costs = 
VAR RentCost = SELECTEDVALUE(DimPotentialLocations[RentCost])
VAR StoreSize = 100  // м²
VAR StaffCost = 5  // співробітники × 20000 грн
VAR UtilitiesCost = 10000
VAR AnnualRent = RentCost * StoreSize * 12
VAR AnnualStaff = StaffCost * 20000 * 12
VAR AnnualUtilities = UtilitiesCost * 12
RETURN
    AnnualRent + AnnualStaff + AnnualUtilities

// 7. Initial Investment
Initial Investment = 
200000 +  // Обладнання
50000 +   // Ремонт
30000     // Маркетинг відкриття

// 8. ROI (3 years)
ROI 3 Years = 
VAR TotalRevenue = [Projected Revenue 3Y Total]
VAR TotalCosts = [Estimated Operating Costs] * 3 + [Initial Investment]
VAR Profit = TotalRevenue * 0.25  // 25% маржа
RETURN
    DIVIDE(Profit - TotalCosts, TotalCosts, 0) * 100

// 9. Payback Period (місяці)
Payback Period Months = 
VAR MonthlyRevenue = [Projected Revenue Year 1] / 12
VAR MonthlyProfit = MonthlyRevenue * 0.25
VAR MonthlyCosts = [Estimated Operating Costs] / 12
VAR MonthlyNetProfit = MonthlyProfit - MonthlyCosts
RETURN
    DIVIDE([Initial Investment], MonthlyNetProfit, 0)

// 10. Location Score (0-100)
Location Score = 
VAR Revenue = [Projected Revenue Year 1]
VAR ROI = [ROI 3 Years]
VAR Traffic = SELECTEDVALUE(DimPotentialLocations[TrafficIndex])
VAR Competition = 10 - SELECTEDVALUE(DimPotentialLocations[CompetitorCount]) * 2
VAR RevenueScore = MIN(Revenue / 1000000 * 25, 25)  // Max 25 points
VAR ROIScore = MIN(ROI / 2, 25)  // Max 25 points
VAR TrafficScore = Traffic * 2.5  // Max 25
VAR CompScore = Competition * 2.5  // Max 25
RETURN
    RevenueScore + ROIScore + TrafficScore + CompScore
```

---

#### Етап 5: Візуалізація та Dashboard (80 хв)

**Створіть сторінку "New Location Analysis"**

**5.1. Map + Selection (15 хв)**

```
Visual: Filled Map
Location: DimPotentialLocations[City]
Color saturation: [Location Score]
Tooltips:
  - City
  - Region
  - Population
  - Projected Revenue Year 1
  - ROI 3 Years
  - Location Score

Slicer: DimPotentialLocations[City]
Type: Tile
Single select
```

---

**5.2. Financial Projection (25 хв)**

```
Visual: Clustered Column Chart
Axis: "Year 1", "Year 2", "Year 3"
Values:
  - Projected Revenue (bars)
  - Estimated Operating Costs (line)

Visual: Waterfall Chart
Categories:
  - Initial Investment (negative, red)
  - Year 1 Profit
  - Year 2 Profit
  - Year 3 Profit
  - Total ROI (positive, green)

Visual: Gauge
Value: [ROI 3 Years]
Target: 20%
Maximum: 50%
Colors:
  - <10%: Red
  - 10-20%: Yellow
  - >20%: Green
```

---

**5.3. Comparison Table (20 хв)**

```
Visual: Matrix
Rows: DimPotentialLocations[City]
Values:
  - Population
  - Avg Income
  - Competitor Count
  - Projected Revenue Year 1
  - ROI 3 Years %
  - Payback Period Months
  - Location Score

Sort by: Location Score (Descending)

Conditional Formatting:
- Location Score: Color scale (white → green)
- ROI 3 Years: Data bars
- Payback Period: Traffic lights
  - <12 months: Green
  - 12-24: Yellow
  - >24: Red
```

---

**5.4. Detailed Analysis (20 хв)**

```
Visual: Scatter Chart
X-axis: Projected Revenue Year 1
Y-axis: ROI 3 Years
Size: Population
Legend: DimPotentialLocations[City]
Labels: City names

Ideal zone: High Revenue + High ROI

Visual: Table - Top Products by Region
(Які товари продаються в схожих регіонах)
Rows:
  - DimProduct[Category]
  - DimProduct[ProductName]
Values:
  - Total Revenue (поточні регіони)
  - Recommended Stock Level
```

---

#### Етап 6: Висновки та Рекомендації (20 хв)

**Створіть Text Box з висновками:**

```markdown
## 📊 Аналіз локацій для нового пункту видачі

### 🏆 Рекомендована локація: [Найкраще місто]

**Обґрунтування:**
- Location Score: [значення]/100
- Прогнозована виручка (Рік 1): [значення] грн
- ROI (3 роки): [значення]%
- Період окупності: [значення] місяців

### 📈 Ключові фактори:
1. **Населення:** [значення] - достатній розмір ринку
2. **Конкуренція:** [Низька/Середня/Висока]
3. **Трафік:** [значення]/10 - [оцінка]

### ⚠️ Ризики:
- [Ризик 1]
- [Ризик 2]

### ✅ Наступні кроки:
1. Пошук приміщення в [місто]
2. Детальний аналіз конкурентів
3. Маркетингова кампанія до відкриття
4. Підготовка асортименту з урахуванням регіональних переваг
```

---

### Критерії оцінювання фінального проєкту

| Критерій | Бали |
|----------|------|
| Постановка бізнес-задачі | 10 |
| BPMN-схема процесу | 10 |
| Розширення моделі даних | 10 |
| DAX-міри для прогнозування | 25 |
| Візуалізація (Map, Charts, Tables) | 20 |
| Comparison та Scoring | 10 |
| Висновки та рекомендації | 10 |
| Якість презентації проєкту | 5 |
| **ВСЬОГО** | **100** |

---

### Захист проєкту (Презентація 10-15 хв)

**Структура презентації:**

1. **Вступ (2 хв)**
   - Бізнес-задача
   - Мета аналізу

2. **Методологія (3 хв)**
   - BPMN-процес
   - Модель даних
   - Ключові припущення

3. **Результати аналізу (5 хв)**
   - Демонстрація Dashboard
   - Порівняння локацій
   - Прогнози

4. **Рекомендації (3 хв)**
   - Обрана локація
   - Обґрунтування
   - План впровадження

5. **Питання (2-3 хв)**

---

**🎉 ВІТАЄМО! ВИ ЗАВЕРШИЛИ КУРС "ТЕХНОЛОГІЇ БІЗНЕС-АНАЛІТИКИ"!**

