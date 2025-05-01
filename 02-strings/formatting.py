"""
! Category: Easy
Todo: Create a program that displays simple personal data information using string formatting. Input Data: ‣name = "Zevhys", ‣age = 28, ‣height = 175.5, Tasks: 1. Display personal data with the following format: ‣Name: ZEVHYS (in capital letters), ‣Age: 28 years, ‣Height: 175.50 cm (with 2 decimal places), 2. Use three different string formatting methods: ‣Using the % operator (old-style), ‣Using the str.format() method, ‣Using f-strings.
"""

name = "Zevhys"
age = 28
height = 175.5

print("---- with operator % ----")
print("name: %s" % name.upper())
print("age: %d years" % age)
print("height: %.2f cm" % height)

print("\n---- with operator str.format() ----")
print("name: {}".format(name.upper()))
print("age: {} years".format(age))
print("height: {0:.2f} cm".format(height))

print("\n---- with operator f-string ----")
print(f"name: {name.upper()}")
print(f"age: {age}")
print(f"height: {height:.2f} cm")

"""
! Category: Medium
Todo: Create a program that displays a list of products with prices in a neat format using string formatting. Input Data: ‣produk = [{"name": "Laptop", "price": 8500000}, {"name": "Smartphone", "price": 4250000}, {"name": "Headphone", "price": 750000}], Tasks: 1. Display the product list in a simple table format with: ‣Title "PRODUCT LIST" at the top, ‣Columns for number, product name, and price, ‣Price formatted with Rupiah currency (Rp) and thousand separators, ‣Neat table format with appropriate column widths, 2. Implement the table using a string formatting method of your choice (%, format, or f-string), 3. At the bottom of the table, display the total price of all products.
"""

product = [
    {"name": "Laptop", "price": 8500000},
    {"name": "Smartphone", "price": 4250000},
    {"name": "Headphone", "price": 750000},
]

print("\n======== product list ========")
print("no | product    | price        ")
print("------------------------------")
for i, item in enumerate(product, 1):
    print(f"{i:<2} | {item['name']:<10} | rp {item['price']:>9,}")
print("------------------------------")
print(f"total: rp {sum(item['price'] for item in product):,}")
