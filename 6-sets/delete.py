"""
! category : easy
TODO : You have a shopping list represented as a set of items. Create a function called clean_shopping_list(shopping_list, items_to_remove) that: 1. Takes two parameters: - shopping_list: A set containing your initial shopping items, - items_to_remove: A list of items you want to remove from your shopping list. 2. Your function should: - For each item in items_to_remove, try to remove it from shopping_list using the appropriate set method, - If an item is in the list, use remove(), - If you're not sure if an item is in the list, use discard(), - Return the final shopping list as a set.
"""


def clean_shopping_list(shopping_list, items_to_remove):
    for item in items_to_remove:
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            shopping_list.discard(item)

    return shopping_list


list_shopping = {"Apple", "Banana", "Milk", "Bread", "Cheese"}
remove_list = ["Milk", "Biscuit", "Bread"]
result = clean_shopping_list(list_shopping, remove_list)
print(result)


"""
! category : medium
TODO : You have a contact list that needs to be cleaned up. Create a function named clean_contacts(contacts, operations) that: Accepts two parameters: contacts: A set containing contact names, operations: A list of strings representing operations to be performed. 1. Possible operations: - If an operation starts with "remove:", use the remove() method to remove the contact mentioned after "remove:", - If an operation starts with "discard:", use the discard() method to discard the contact mentioned after "discard:", - If an operation is "pop", use the pop() method to remove one contact randomly, - If an operation is "clear", use the clear() method to remove all contacts. 2. Your function must: - Handle errors if they occur (for example, trying to remove a contact that doesn't exist), - Return the cleaned contacts set.
"""


def clean_contacts(contacts, operations):
    for op in operations:
        if ":" in op:
            method, name = op.split(":", 1)
        else:
            method, name = op, None

        if method == "remove" and name:
            try:
                contacts.remove(name)
            except KeyError:
                pass
        elif method == "discard" and name:
            contacts.discard(name)
        elif method == "pop" and contacts:
            contacts.pop()
        elif method == "clear":
            contacts.clear()

    return contacts


list_contact = {"Budi", "Ani", "Citra", "Dodi", "Eko"}
list_operations = [
    "remove:Budi",
    "discard:Fani",
    "pop",
    "discard:Ani",
    "remove:Citra",
]

output = clean_contacts(list_contact, list_operations)
print("\nthe remaining contact:", output)
