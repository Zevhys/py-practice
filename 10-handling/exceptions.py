"""
! Category: Easy
Todo: Create a program that asks the user to enter two numbers and divides them (first number divided by the second number). Use try-except to handle possible errors during input or when the division is performed. The program must be able to display an error message if: ‣The input is not a number, ‣Division by zero occurs.
"""

try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    result = a / b
except ValueError:
    print("\nplease enter numeric values")
except ZeroDivisionError:
    print("\ncannot divide by zero")
else:
    print(f"\n{a} / {b} = {result:,.0f}\n")

"""
! Category: Medium
Todo: Create a function called process_data that accepts a list of mixed data (strings, numbers, and others). This function will try to convert each item in the list to an integer. If there's an item that can't be converted to an integer, skip that item without stopping the program, and display an error message like: "Cannot convert 'abc' to integer."
"""


def process_data(items: list):
    for data in items:
        try:
            print(f"converted integers: {int(data)}")
        except (ValueError, TypeError):
            print(f"cannot convert '{data}' to integer")


process_data(["123", "abc", 45.6, "78", None, "xyz", 100])
