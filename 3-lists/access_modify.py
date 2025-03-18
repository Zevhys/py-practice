"""
! category : easy
TODO : Create a program that performs access and modification on a list containing a shopping list. You will use various list access and modification methods to complete simple tasks commonly encountered when working with lists. Start with the following shopping list: shopping_list = ["apple", "eggs", "bread", "milk", "sugar"]. Your tasks are: 1. Display initial shopping list, 2. Show first and last items, 3. Add "coffee" to list, 4. Insert "cheese" at index 2, 5. Replace "sugar" with "honey", 6. Remove "eggs" from list, 7. Sort list alphabetically, 8. Reverse list order, 9. Display final list with item count.
"""

shop_list = ["apple", "egg", "bread", "milk", "sugar"]

print(f"display initial shopping list: {shop_list[0:]}")
print(f"show first and last items: {[shop_list[n] for n in (0, -1)]}")

shop_list.append("coffee")
print(f"add 'coffee' to the shopping list: {shop_list}")

shop_list.insert(2, "cheese")
print(f"insert 'cheese' at index 2: {shop_list}")

sugar_index = shop_list.index("sugar")
shop_list[sugar_index] = "honey"
print(f"Replace 'sugar' with 'honey': {shop_list}")

shop_list.remove("egg")
print(f"remove 'eggs' from list: {shop_list}")

shop_list.sort()
print(f"sort list alphabetically: {shop_list}")

shop_list.reverse()
print(f"reverse list order: {shop_list}")

print(f"display final list with item count: {shop_list}, {len(shop_list)}\n")

"""
! category : medium
TODO : Create a program that manages product data using lists and performs several access and modification operations on that data. Initial data: # Product data in format [name, price, stock] product_list = [ ["Laptop", 8000000, 5], ["Mouse", 150000, 15], ["Keyboard", 300000, 10], ["Monitor", 2500000, 7]]. Your tasks are: 1. Display all product data in format: "Product Name - Rp Price - Stock: quantity", 2. Add new product: ["Headset", 350000, 8], 3. Update Keyboard stock quantity to 12, 4. Reduce Mouse price by 15%, 5. Display product with highest stock, 6. Sort product list by price from cheapest to most expensive, 7. Remove products with stock <= 8.
"""

product_list = [
    ["Laptop", 8000000, 5],
    ["Mouse", 150000, 15],
    ["Keyboard", 300000, 10],
    ["Monitor", 2500000, 7],
]


def print_products(title, products):
    print(f"\n{title}")
    for product in products:
        print(f"{product[0]} - Rp {product[1]} - Stock: {product[2]}")


print_products("display all product data in format:", product_list)

product_list.append(["Headset", 350000, 8])
print_products("add new product:", product_list)

for product in product_list:
    if product[0] == "Keyboard":
        product[2] = 12
        break
print_products("update keyboard stock quantity to 12:", product_list)

for product in product_list:
    if product[0] == "Mouse":
        product[1] = int(product[1] * 0.85)
        break
print_products("reduce mouse price by 15%:", product_list)

highest_stock_product = max(product_list, key=lambda x: x[2])
print(
    f"\ndisplay product with highest stock: {highest_stock_product[0]} - Stock: {highest_stock_product[2]}"
)

product_list.sort(key=lambda x: x[1])
print_products("sort product list by price:", product_list)

product_list = [product for product in product_list if product[2] >= 8]
print_products("Remove products with stock <= 8:", product_list)
