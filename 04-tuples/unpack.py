"""
! Category: Easy
Todo: 1. Use tuple unpacking to print information for each student in the format: "Name: [name], Student ID: [student_id], Score: [score]", 2. Use a for loop to access each tuple in the list and perform tuple unpacking within that loop, student_data = [("Budi", "A001", 85), ("Ani", "A002", 90), ("Dodi", "A003", 75), ("Rina", "A004", 88)].
"""

student_data = [
    ("Budi", "A001", 85),
    ("Ani", "A002", 90),
    ("Dodi", "A003", 75),
    ("Rina", "A004", 88),
]

for name, student_id, score in student_data:
    print(f"name: {name}, student id: {student_id}, score: {score}")

"""
! Category: Medium
Todo: 1. Create a function find_cheapest_and_most_expensive() that takes a list of products, 2. The function should use tuple unpacking to find the cheapest and most expensive products based on price, 3. The function should return a tuple containing two values: ‣(cheapest_product, most_expensive_product), ‣where each is a tuple of (name, price, stock), 4. Call the function with the products list and print the results in an easy-to-read format. products = [("Book", 50000, 10), ("Pencil", 5000, 50), ("Bag", 150000, 5), ("Eraser", 3000, 100)].
"""

products = [
    ("Book", 50000, 10),
    ("Pencil", 5000, 50),
    ("Bag", 150000, 5),
    ("Eraser", 3000, 100),
]


def find_cheapest_and_most_expensive(product_list):
    cheapest = most_expensive = product_list[0]

    for product in product_list:
        name, price, stock = product
        cheapest_name, cheapest_price, cheapest_stock = cheapest
        expensive_name, expensive_price, expensive_stock = most_expensive

        if price < cheapest_price:
            cheapest = product

        if price > expensive_price:
            most_expensive = product

    return (cheapest, most_expensive)


cheap, expensive = find_cheapest_and_most_expensive(products)
print(f"\ncheapest:\nname: {cheap[0]}, price: {cheap[1]}, stock: {cheap[2]}")
print(f"\ncostly:\nname: {expensive[0]}, price: {expensive[1]}, stock: {expensive[2]}")
