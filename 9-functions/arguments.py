"""
! category: easy
TODO: Create a function called greeting() that has two parameters: 1. name (required), 2. language (optional, default is "English"). If the chosen language is "English", display: - Hello, name!, If it's "Indonesian", display: - Halo, name!, If the user enters any other language, display: - Language not supported. After creating the function, call the greeting() function at least 2 times: 1. Once with only name, 2. Once more with name and language.
"""


def greeting(name, language="english"):
    if language == "english":
        print(f"hello, {name}!")
    elif language == "indonesian":
        print(f"halo, {name}!")
    else:
        print("language not supported")


greeting("rey")
greeting("kegin", "indonesian")

print("")

"""
! category: medium
TODO: Create a function called order_summary() that accepts: - Any number of order items, - Customer information such as name, address, and contact. This function should print: - Customer name, address, and contact, - List of ordered items. Example of function usage: order_summary("Burger", "Fries", "Cola", name="John", address="Jakarta", contact="08123456789"). The output should match the information above, and if no items are provided, display the message: - No items ordered.
"""


def order_summary(*menu, **info):
    print("customer info:")
    print(f"name    : {info['name']}")
    print(f"address : {info['address']}")
    print(f"contact : {info['contact']}\n")

    print("ordered items:")
    if menu:
        for item in menu:
            print(f"- {item}")
    else:
        print("no items ordered")


order_summary(
    "Burger", "Fries", "Cola", name="John", address="Jakarta", contact="08123456789"
)
