"""
! category : easy
TODO : Create a program that displays simple personal data information using string formatting. Input Data: name = "Zevhys", age = 28, height = 175.5. Tasks: (1). Display personal data with the following format: Name: ZEVHYS (in capital letters), Age: 28 years, Height: 175.50 cm (with 2 decimal places). (2). Use three different string formatting methods: Using the % operator (old-style), Using the str.format() method, Using f-strings.
"""

name = "Zevhys"
age = 28
height = 175.5

print("---- with operator % ----")
print("Name: %s" % name.upper())
print("Age: %d years" % age)
print("Height: %.2f cm" % height)

print("\n---- with operator str.format() ----")
print("Name: {}".format(name.upper()))
print("Age: {} years".format(age))
print("Height: {0:.2f} cm".format(height))

print("\n---- with operator f-string ----")
print(f"Name: {name.upper()}")
print(f"Age: {age}")
print(f"Height: {height:.2f} cm")

"""
! category : medium
TODO : Create a program that displays a list of products with prices in a neat format using string formatting. Input Data: produk = [{"nama": "Laptop", "harga": 8500000}, {"nama": "Smartphone", "harga": 4250000}, {"nama": "Headphone", "harga": 750000}]. Tasks: (1). Display the product list in a simple table format with: Title "PRODUCT LIST" at the top, Columns for number, product name, and price, Price formatted with Rupiah currency (Rp) and thousand separators, Neat table format with appropriate column widths. (2). Implement the table using a string formatting method of your choice (%, format, or f-string). (3). At the bottom of the table, display the total price of all products.
"""

product = [
    {"name": "Laptop", "price": 8500000},
    {"name": "Smartphone", "price": 4250000},
    {"name": "Headphone", "price": 750000},
]

print("\n======== PRODUCT LIST ========")
print("No | Product    | Price        ")
print("------------------------------")
for i, item in enumerate(product, 1):
    print(f"{i:<2} | {item['name']:<10} | Rp {item['price']:>9,}")
print("------------------------------")
print(f"Total: Rp {sum(item['price'] for item in product):,}")
