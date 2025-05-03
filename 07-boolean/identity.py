"""
! Category: Easy
Todo: Create a program that checks if two variables point to the same object in memory. Instructions: 1. Create two variables that store the same numeric value, 2. Check if both variables point to the same object in memory.
"""

a = 1
b = a

print(f"check both variables point: {a is b}")

"""
! Category: Medium
Todo: Create a program that checks if two lists with the same elements but created separately are different objects in memory. Instructions: 1. Create two lists containing the same elements, but create them separately, 2. Check if both lists point to different objects in memory, 3. Add a new element to one of the lists, then check again if their identities remain different.
"""

list_1 = ["Cherry", "Apple", "Manggo", "Avocado"]
list_2 = ["Cherry", "Apple", "Manggo", "Avocado"]

print(f"\ncheck both lists: {list_1 is not list_2}")

list_1.append("Strawberry")
print(f"add a new element, then check again: {list_1 is not list_2}")
