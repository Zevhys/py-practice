"""
! Category: Easy
Todo: Create a program that manages a music playlist using various list methods. This program will help you understand the use of common list methods for processing data in list form. Start with the following playlist: playlist = ["Shape of You", "Despacito", "Blinding Lights", "Dance Monkey", "Uptown Funk"]. Your tasks are: 1. Display the initial playlist, 2. Add the song "Watermelon Sugar" to the playlist, 3. Insert the song "Believer" at the third position (index 2), 4. Add multiple songs at once: ["Bad Guy", "Levitating"], 5. Remove the song "Despacito" from the playlist, 6. Remove and display the last song from the playlist, 7. Find the position of the song "Blinding Lights", 8. Count how many times the song "Dance Monkey" appears in the playlist, 9. Sort the playlist alphabetically, 10. Reverse the playlist order,11. Create a copy of the playlist, 12. Remove all songs from the original playlist (not the copy).
"""

playlist = [
    "Shape of You",
    "Despacito",
    "Blinding Lights",
    "Dance Monkey",
    "Uptown Funk",
]

print("initial playlist:", playlist)

playlist.append("Watermelon Sugar")
print("\nadd the song 'Watermelon Sugar':", playlist)

playlist.insert(2, "Believer")
print("\ninsert 'Believer' at index 2:", playlist)

playlist.extend(["Bad Guy", "Levitating"])
print("\nadd multiple songs 'Bad Guy', 'Levitating':", playlist)

playlist.remove("Despacito")
print("\nremove the song 'Despacito':", playlist)

playlist.pop()
print("\nremove and display last song:", playlist)

print("\nfind position of 'Blinding Lights':", playlist.index("Blinding Lights"))

print("\ncount occurrences of 'Dance Monkey':", playlist.count("Dance Monkey"))

playlist.sort()
print("\nsort alphabetically:", playlist)

playlist.reverse()
print("\nreverse order:", playlist)

copy = playlist.copy()
print("\ncreate copy:", copy)

playlist.clear()
print("\nclear original playlist:", playlist)

"""
! Category: Medium
Todo: Create a program that processes monthly sales data using various list methods. This program will help you understand the use of list methods for simple data analysis. Initial data: sales_data = [["January", 150, 15000000], ["February", 200, 20000000], ["March", 180, 18000000], ["April", 210, 21000000], ["May", 190, 19500000]], best_selling_products = [["Gaming Laptop", 45], ["Smartphone", 80], ["Headphone", 65]], additional_data = [["July", 240, 24000000], ["August", 220, 22000000]]. Your tasks are: 1. Display initial data, 2. Add June data: ["June", 230, 23500000], 3. Insert between March-April: ["March (Revised)", 195, 19800000], 4. Find "May" position, 5. Add from additional_data list to sales_data, 6. Copy best_selling_products, 7. Add to copy: ["Bluetooth Speaker", 50], 8. Sort by products sold (highest-lowest), 9. Calculate total revenue.
"""

sales_data = [
    ["January", 150, 15000000],
    ["February", 200, 20000000],
    ["March", 180, 18000000],
    ["April", 210, 21000000],
    ["May", 190, 19500000],
]

best_selling_products = [["Gaming Laptop", 45], ["Smartphone", 80], ["Headphone", 65]]


def print_products(month, number):
    print(f"\n{month}")
    for product in number:
        print(f"{product[0]} - {product[1]} Product - Rp {product[2]}")


def print_best(name, quantity):
    print(f"\n{name}")
    for product in quantity:
        print(f"{product[0]} - {product[1]} unit")


print_products("initial data:", sales_data)

sales_data.append(["June", 230, 23500000])
print_products("add June data:", sales_data)

sales_data.insert(3, ["March (Revised)", 195, 19800000])
print_products("insert between March-April:", sales_data)

may_index = None
for i, data in enumerate(sales_data):
    if data[0] == "May":
        may_index = i
        break

print("\nfind 'May' position:", may_index)

additional_data = [["July", 240, 24000000], ["August", 220, 22000000]]
sales_data.extend(additional_data)
print_products("insert between March-April:", sales_data)

copy = best_selling_products.copy()
print_best("copy best selling products:", copy)

copy.append(["Speaker Bluetooth", 50])
print_best("add to copy 'Bluetooth Speaker', 50:", copy)

sales_data.sort(key=lambda x: x[1], reverse=True)
print_products("sort by products sold (highest-lowest):", sales_data)

total_revenue = 0
for data in sales_data:
    total_revenue += data[2]

print(f"\ncalculate total revenue: Rp", total_revenue)
