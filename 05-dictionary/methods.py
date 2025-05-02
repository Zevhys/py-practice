"""
! Category: Easy
Todo: 1. Display all subject names in the dictionary, 2. Display all exam scores in the dictionary, 3. Display each subject along with its score in the form of (key, value).
"""

subjects = {"Math": 90, "Language": 75, "Chemistry": 100}

print(f"all subject names: {subjects.keys()}")
print(f"all exam scores: {subjects.values()}")
print(f"each subject along with its score in the form: {subjects.items()}")

"""
! Category: Medium
Todo: 1. Check if a product with a specific name exists in the dictionary or not using a dictionary method, 2. If the product exists, display its price, 3. If the product is not found, add that product along with its price, 4. Finally, print the updated dictionary.
"""

products = {"Laptop": 9000000, "Keyboard": 1000000}
name_products = "Handphone"
price_products = 2000000

if name_products in products:
    result = products.get(name_products)
    print(f"\nprice {name_products}: {result}")
else:
    products.setdefault(name_products, price_products)
    print(f"\n{name_products} not found, {name_products} added")


print(f"dictionary after being updated: {products}")
