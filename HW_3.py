# Task 5

items = {
    "milk15": {"name": "молоко 1.5%", "count": 34, "price": 89.9},
    "cheese": {"name": "сыр молочный 1 кг.", "count": 12, "price": 990.9},
    "sausage": {"name": "колбаса 1 кг.", "count": 122, "price": 1990.9},
}

# Dict comprehension: проверяем поле 'count' на условие < 20
price_less_20 = {key: value["count"] < 20 for key, value in items.items()}

print(price_less_20)
