"""
! category : easy
TODO : 1. Create a set containing several fruit names, 2. Add one new fruit name to the set using the appropriate method, 3. Print the set after the addition to ensure the new fruit has been successfully added.
"""

fruits = {"Banana", "Watermelon", "Strawberry"}
fruits.add("Apple")
print(f"fruits: {fruits}\n")

"""
! category : medium
TODO : 1. Create a set containing a list of unique hobbies from several people, 2. Check if a particular hobby already exists in the set or not, 3. If it doesn't exist, add the hobby using the appropriate method, 4. Print the updated set after the addition.
"""

hobbies = {"Hiking", "Cooking", "Reading"}

if "Gardening" in hobbies:
    print("hobbies already on sets")
else:
    hobbies.update(["Gardening"])
    print(f"hobbies not found, will be added on sets: {hobbies}")
