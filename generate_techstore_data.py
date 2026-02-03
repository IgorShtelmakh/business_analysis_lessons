"""
Скрипт генерації тестових даних для курсу "Технології бізнес-аналітики"
Компанія: TechStore (інтернет-магазин електроніки)
Період: 2022-2024
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Налаштування
random.seed(42)
np.random.seed(42)

print("=" * 60)
print("ГЕНЕРАЦІЯ ТЕСТОВИХ ДАНИХ ДЛЯ TECHSTORE")
print("=" * 60)

# Константи
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2024, 12, 31)

REGIONS = ['Київська', 'Львівська', 'Харківська', 'Дніпропетровська', 'Одеська']
CITIES = {
    'Київська': ['Київ', 'Бровари', 'Біла Церква', 'Вишневе'],
    'Львівська': ['Львів', 'Дрогобич', 'Стрий', 'Червоноград'],
    'Харківська': ['Харків', 'Лозова', 'Ізюм', 'Куп\'янськ'],
    'Дніпропетровська': ['Дніпро', 'Кривий Ріг', 'Нікополь', 'Павлоград'],
    'Одеська': ['Одеса', 'Чорноморськ', 'Южне', 'Білгород-Дністровський']
}

# 1. Генерація клієнтів
def generate_customers(n=15000):
    print(f"\n1️⃣  Генерація {n} клієнтів...")
    
    first_names_male = ['Олександр', 'Іван', 'Петро', 'Дмитро', 'Сергій', 'Андрій', 
                        'Володимир', 'Максим', 'Віктор', 'Олег', 'Юрій', 'Роман']
    first_names_female = ['Марія', 'Олена', 'Наталія', 'Анна', 'Тетяна', 'Катерина', 
                          'Світлана', 'Ірина', 'Оксана', 'Людмила', 'Вікторія', 'Юлія']
    last_names = ['Іваненко', 'Коваленко', 'Петренко', 'Шевченко', 'Ткаченко', 
                  'Бондаренко', 'Мельник', 'Кравченко', 'Василенко', 'Клименко',
                  'Павленко', 'Кузьменко', 'Савченко', 'Литвиненко', 'Семенченко']
    patronymics_male = ['Олександрович', 'Іванович', 'Петрович', 'Володимирович', 'Сергійович']
    patronymics_female = ['Олександрівна', 'Іванівна', 'Петрівна', 'Володимирівна', 'Сергіївна']
    
    customers = []
    for i in range(1, n+1):
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
        
        reg_date = START_DATE + timedelta(days=random.randint(0, (END_DATE-START_DATE).days))
        
        customers.append({
            'customer_id': i,
            'registration_date': reg_date.strftime('%Y-%m-%d'),
            'full_name': full_name,
            'email': f"user{i}@{'gmail.com' if i%2==0 else 'ukr.net'}",
            'phone': f"+38050{random.randint(1000000, 9999999)}",
            'city': city,
            'region': region,
            'age': random.randint(18, 65),
            'gender': gender,
            'customer_segment': random.choices(['Premium', 'Standard', 'Budget'], 
                                              weights=[0.15, 0.60, 0.25])[0]
        })
    
    df = pd.DataFrame(customers)
    print(f"   ✅ Створено {len(df)} клієнтів")
    return df

# 2. Генерація товарів
def generate_products(n=500):
    print(f"\n2️⃣  Генерація {n} товарів...")
    
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
    
    products = []
    product_id = 1
    
    items_per_category = n // len(categories)
    
    for category, config in categories.items():
        for _ in range(items_per_category):
            brand = random.choice(config['brands'])
            model = random.choice(config['models'])
            
            price = random.randint(config['price_range'][0], config['price_range'][1])
            cost_price = int(price * random.uniform(0.65, 0.85))
            
            products.append({
                'product_id': product_id,
                'product_name': f"{brand} {category[:-1]} {model}-{random.randint(100, 999)}",
                'category': category,
                'subcategory': brand,
                'brand': brand,
                'unit_price': price,
                'cost_price': cost_price,
                'supplier_id': random.randint(101, 130),
                'in_stock': random.randint(0, 100),
                'is_active': random.choices([True, False], weights=[0.85, 0.15])[0]
            })
            product_id += 1
    
    df = pd.DataFrame(products)
    print(f"   ✅ Створено {len(df)} товарів")
    return df

# 3. Генерація постачальників
def generate_suppliers(n=30):
    print(f"\n3️⃣  Генерація {n} постачальників...")
    
    countries = ['Україна', 'Польща', 'Німеччина', 'Китай', 'США', 'Чехія']
    company_types = ['Ltd', 'Inc', 'GmbH', 'Corp', 'SA', 'UAB']
    
    suppliers = []
    for i in range(101, 101+n):
        country = random.choice(countries)
        company_type = random.choice(company_types)
        
        suppliers.append({
            'supplier_id': i,
            'supplier_name': f"TechSupply-{i} {company_type}",
            'country': country,
            'contact_person': f"Contact Person {i}",
            'email': f"supplier{i}@tech.com",
            'phone': f"+{random.choice([48, 49, 86, 380])}{random.randint(100000000, 999999999)}",
            'rating': round(random.uniform(3.5, 5.0), 1),
            'is_active': random.choices([True, False], weights=[0.85, 0.15])[0]
        })
    
    df = pd.DataFrame(suppliers)
    print(f"   ✅ Створено {len(df)} постачальників")
    return df

# 4. Пункти видачі
def generate_pickup_locations():
    print(f"\n4️⃣  Генерація пунктів видачі...")
    
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
    
    df = pd.DataFrame(locations)
    print(f"   ✅ Створено {len(df)} пунктів видачі")
    return df

# 5. Генерація замовлень
def generate_orders(customers_df, n=80000):
    print(f"\n5️⃣  Генерація {n} замовлень...")
    
    channels = ['Website', 'Mobile App', 'Partner Store']
    statuses = ['Delivered', 'Shipped', 'Pending', 'Cancelled', 'Returned']
    payment_methods = ['Card', 'Cash', 'Online']
    
    orders = []
    for i in range(1, n+1):
        customer_id = random.choice(customers_df['customer_id'].tolist())
        
        order_date = START_DATE + timedelta(
            days=random.randint(0, (END_DATE-START_DATE).days),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59)
        )
        
        status = random.choices(statuses, weights=[0.70, 0.12, 0.05, 0.10, 0.03])[0]
        
        shipping_date = None
        delivery_date = None
        
        if status in ['Delivered', 'Shipped', 'Returned']:
            shipping_date = order_date + timedelta(days=random.randint(1, 3))
            if status in ['Delivered', 'Returned']:
                delivery_date = shipping_date + timedelta(days=random.randint(1, 7))
        
        orders.append({
            'order_id': i,
            'customer_id': customer_id,
            'order_date': order_date.strftime('%Y-%m-%d %H:%M:%S'),
            'shipping_date': shipping_date.strftime('%Y-%m-%d %H:%M:%S') if shipping_date else None,
            'delivery_date': delivery_date.strftime('%Y-%m-%d %H:%M:%S') if delivery_date else None,
            'order_status': status,
            'channel': random.choice(channels),
            'pickup_location_id': random.randint(1, 12) if status != 'Cancelled' else None,
            'payment_method': random.choice(payment_methods),
            'discount_percent': random.choices([0, 5, 10, 15, 20], weights=[0.5, 0.25, 0.15, 0.07, 0.03])[0],
            'shipping_cost': random.choice([0, 50, 70, 100]),
            'total_amount': 0  # Буде розраховано після order_items
        })
        
        if i % 10000 == 0:
            print(f"   ⏳ Оброблено {i}/{n} замовлень...")
    
    df = pd.DataFrame(orders)
    print(f"   ✅ Створено {len(df)} замовлень")
    return df

# 6. Генерація позицій замовлень
def generate_order_items(orders_df, products_df):
    print(f"\n6️⃣  Генерація позицій замовлень...")
    
    order_items = []
    item_id = 1
    order_totals = {}
    
    active_products = products_df[products_df['is_active'] == True].copy()
    
    for idx, order in orders_df.iterrows():
        if order['order_status'] == 'Cancelled':
            order_totals[order['order_id']] = 0
            continue
        
        items_count = random.choices([1, 2, 3, 4, 5], weights=[0.50, 0.30, 0.12, 0.06, 0.02])[0]
        
        selected_products = active_products.sample(n=min(items_count, len(active_products)))
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
                'discount_amount': round(discount_amount, 2),
                'line_total': round(line_total, 2)
            })
            item_id += 1
        
        order_totals[order['order_id']] = round(order_total + order['shipping_cost'], 2)
        
        if (idx + 1) % 10000 == 0:
            print(f"   ⏳ Оброблено {idx + 1}/{len(orders_df)} замовлень...")
    
    # Оновлення total_amount
    orders_df['total_amount'] = orders_df['order_id'].map(order_totals).fillna(0)
    
    df = pd.DataFrame(order_items)
    print(f"   ✅ Створено {len(df)} позицій замовлень")
    return df, orders_df

# Головна функція
def main():
    print("\n🚀 Початок генерації даних...\n")
    
    # Генерація
    customers = generate_customers(15000)
    products = generate_products(500)
    suppliers = generate_suppliers(30)
    locations = generate_pickup_locations()
    orders = generate_orders(customers, 80000)
    order_items, orders = generate_order_items(orders, products)
    
    # Збереження
    print("\n💾 Збереження файлів...")
    os.makedirs('data', exist_ok=True)

    customers.to_csv('data/customers.csv', index=False, encoding='utf-8-sig')
    print("   ✅ data/customers.csv")

    products.to_csv('data/products.csv', index=False, encoding='utf-8-sig')
    print("   ✅ data/products.csv")

    suppliers.to_csv('data/suppliers.csv', index=False, encoding='utf-8-sig')
    print("   ✅ data/suppliers.csv")

    locations.to_csv('data/pickup_locations.csv', index=False, encoding='utf-8-sig')
    print("   ✅ data/pickup_locations.csv")

    orders.to_csv('data/orders.csv', index=False, encoding='utf-8-sig')
    print("   ✅ data/orders.csv")

    order_items.to_csv('data/order_items.csv', index=False, encoding='utf-8-sig')
    print("   ✅ data/order_items.csv")
    
    # Статистика
    print("\n" + "=" * 60)
    print("📊 СТАТИСТИКА ЗГЕНЕРОВАНИХ ДАНИХ")
    print("=" * 60)
    print(f"Клієнти:              {len(customers):,}")
    print(f"Товари:               {len(products):,}")
    print(f"Постачальники:        {len(suppliers):,}")
    print(f"Пункти видачі:        {len(locations):,}")
    print(f"Замовлення:           {len(orders):,}")
    print(f"Позиції замовлень:    {len(order_items):,}")
    print(f"\nЗагальна виручка:     {orders['total_amount'].sum():,.2f} грн")
    print(f"Середній чек:         {orders[orders['total_amount'] > 0]['total_amount'].mean():,.2f} грн")
    print("=" * 60)
    print("\n✅ Генерація завершена успішно!")
    print("📁 Файли збережено в папці data/\n")

if __name__ == "__main__":
    main()
