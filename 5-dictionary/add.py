"""
! category : easy
TODO : 1. Create an empty dictionary named student_scores, 2. Add data for 3 students with names as keys and scores as values, 3. Display the dictionary after each data addition, 4. Use 3 different methods to add data to the dictionary.
"""

student_scores = {}

student_scores["andy"] = 85
print("first addition:", student_scores)

student_scores.update({"chris": 90})
print("second addition:", student_scores)

print("third addition:", student_scores | {"wendy": 1000}, "\n")

"""
! category : medium
TODO : 1. Create an inventory dictionary with several initial items (at least 2 items) - Format: item_name (string) as key, and a dictionary containing 'quantity' (integer) and 'price' (integer) as value, 2. Implement a function add_item(inventory, name, quantity, price) that: - Adds a new item if it doesn't already exist in the inventory, - Increases the quantity if the item already exists (without changing the price), - Displays an appropriate message for both cases, 3. Implement a function display_inventory(inventory) to show the entire inventory in a neat format.
"""

inventory = {
    "t-shirt": {"total": 10, "price": 100000},
    "fedora": {"total": 1, "price": 200000},
}


def add_item(inventory, name, total, price):
    if name in inventory:
        inventory[name]["total"] += total
        print(f"'{name}' added, quantity updated to {inventory[name]['total']} units.")
    else:
        inventory[name] = {"total": total, "price": price}
        print(f"\nnew '{name}' added to inventory.")


def show_inventory(inventory):
    for name_item, details in inventory.items():
        print(f"\nname item: {name_item}")
        print(f"- total: {details['total']}")
        print(f"- price: Rp {details['price']}")
        print("---------------------")


print("initial inventory:")
show_inventory(inventory)

add_item(inventory, "pen", 20, 3500)
add_item(inventory, "fedora", 2, 200000)

print("\ninventory after additions:")
show_inventory(inventory)
