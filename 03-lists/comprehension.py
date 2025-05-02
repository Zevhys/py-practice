"""
! Category: Easy
Todo: You have a list containing student data in the form of dictionaries. Each dictionary contains information about the student's name and score. Initial Data: students = [{"name": "John", "score": 85}, {"name": "Alice", "score": 72}, {"name": "Bob", "score": 58}, {"name": "Carol", "score": 95}, {"name": "David", "score": 69}, {"name": "Emma", "score": 81}]. Create a program that uses list comprehension to: 1. Create a new list containing only the names of students with scores above 70, 2. Create a new list containing the pass/fail status for each student (pass if score ≥ 60), 3. Create a new list containing uppercase names for students with scores above 80.
"""

students = [
    {"name": "John", "score": 85},
    {"name": "Alice", "score": 72},
    {"name": "Bob", "score": 58},
    {"name": "Carol", "score": 95},
    {"name": "David", "score": 69},
    {"name": "Emma", "score": 81},
]

over_seventy = [s["name"] for s in students if s["score"] > 70]
print("names with scores > 70:", over_seventy)

pass_status = ["Pass" if s["score"] >= 60 else "Not Pass" for s in students]
print("\npass/fail status (pass if score ≥ 60):", pass_status)

over_eighty = [s["name"].upper() for s in students if s["score"] > 80]
print("\nuppercase names for students with scores > 80:", over_eighty)

"""
! Category: Medium
Todo: You have a list containing product data in the form of tuples. Each tuple contains information about the product name, category, price, and stock. Initial Data: products = [("Laptop", "Electronics", 15000000, 5), ("Smartphone", "Electronics", 8000000, 10), ("T-shirt", "Clothing", 45000, 20), ("Coffee Maker", "Kitchen", 850000, 3), ("Jeans", "Clothing", 150000, 0), ("Headphones", "Electronics", 350000, 8), ("Mug", "Kitchen", 25000, 15), ("Socks", "Clothing", 15000, 25)]. Create a program that uses list comprehension to: 1. Create list of product names, 2. Create list of (product_name, price) tuples, 3. Create list of names for available products (stock > 0) with price < 50000, 4. Create list of total inventory values (price × stock), 5. Create nested list grouping product names by category.
"""

products = [
    ("Laptop", "Electronics", 15000000, 5),
    ("Smartphone", "Electronics", 8000000, 10),
    ("T-shirt", "Clothing", 45000, 20),
    ("Coffee Maker", "Kitchen", 850000, 3),
    ("Jeans", "Clothing", 150000, 0),
    ("Headphones", "Electronics", 350000, 8),
    ("Mug", "Kitchen", 25000, 15),
    ("Socks", "Clothing", 15000, 25),
]

products_name = [p[0] for p in products]
print("\nproduct names:", products_name)

name_price = [(p[0], p[2]) for p in products]
print("\ncontaining tuples (product_name, price) for all products:", name_price)

stock_price = [p[0] for p in products if p[3] > 0 and p[2] < 50000]
print("\navailable products (stock > 0) with price < 50000:", stock_price)

total_inventory = [p[2] * p[3] for p in products]
print("\ntotal inventory values (price × stock):", total_inventory)

categories = list(set(p[1] for p in products))
product_by_category = [
    [p[0] for p in products if p[1] == category] for category in categories
]
print("\ngrouping product names by category:", product_by_category)
