"""
! category : easy
TODO : 1. Create a student_data tuple containing 5 tuples. Each tuple should contain student information in the format (name, student_ID, score), 2. Name is a string, student_ID is a string, and score is an integer (0-100), 3. Display how many students received a particular score (the score is provided in the template code), 4. Find the position of the first student with a specific name (the name is provided in the template code). Code Template: score_to_find = 85, name_to_find = "Budi"
"""

data_students = (
    ("Budi", "0001", 85),
    ("Smith", "0002", 70),
    ("Jane", "0003", 80),
    ("Kirito", "0004", 85),
    ("Yeri", "0005", 80),
)

find_score = sum((score.count(85) for score in data_students))
print("how many students received a particular score:", find_score)

name = tuple((name[0] for name in data_students))
find_name = name.index("Budi")
print(f"\nstudent named {name[0]} is in the position:", find_name)

"""
! category : medium
TODO :  1. Use the `transactions` tuple containing several tuples. Each tuple is in the format (transaction_ID, product, quantity, unit_price), 2. transaction_ID is a string, product is a string, quantity is an integer, and unit_price is an integer, 3. Implement a function `find_transaction` that takes a tuple of transactions and the product name to search for as parameters, 4. Within the function: • Find the index of the first transaction that sells the specified product. • Count how many times the product appears in the transaction list. • Calculate the total sales by summing the quantity of items from each transaction that sells the specified product. • Return a tuple containing (first_index, occurrence_count, total_sales). 5. Demonstrate the usage of the function by searching for the product data "Book" and "Pencil".
"""

transaction = (
    ("T001", "Book", 3, 50000),
    ("T002", "Pencil", 10, 5000),
    ("T003", "Eraser", 5, 3000),
    ("T004", "Book", 2, 50000),
    ("T005", "Pencil", 5, 5000),
)


def find_transaction(data_transaction, product):
    product_names = tuple(name[1] for name in transaction)
    first_index = product_names.index(product)
    occurrence_count = product_names.count(product)
    total_sales = sum(qty for _, name, qty, _ in data_transaction if name == product)

    return (first_index, occurrence_count, total_sales)


result_book = find_transaction(transaction, "Book")
result_pencil = find_transaction(transaction, "Pencil")

print("\ndata transaction book")
print(
    f"index = {result_book[0]}, total transaction = {result_book[1]}, total sales = {result_book[2]}"
)

print("\ndata transaction pencil")
print(
    f"index = {result_pencil[0]}, total transaction = {result_pencil[1]}, total sales = {result_pencil[2]}"
)
