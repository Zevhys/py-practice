"""
! category : easy
TODO : 1. Create a dictionary containing 3 fruit names as keys and prices as values, 2. Remove one fruit from the dictionary, 3. Display the dictionary with the deleted element, 4. Remove one fruit from the dictionary, 5. Display the dictionary with the deleted element.
"""

fruits = {"apple": 5000, "manggo": 7000, "orange": 6000}
del fruits["apple"]
print(fruits)

"""
! category : medium
TODO : 1. Create a dictionary containing the following information: - name: a person's name, - age: age in numbers, - job: type of job, 2. Ask for user input for the key they want to delete, 3. Remove that key from the dictionary (if it exists), then display: - The dictionary after deletion, - If the key is not found, display the message: "Key not found in dictionary."
"""

people = {"Name": "John Doe", "Age": 25, "Profession": "Professor"}
user_input = input("\nchoose key you want to delete: ")

if user_input in people:
    del people[user_input]
    print(f"\nkey {user_input} has been deleted from dictionary")
else:
    print("the key is not in dictionary")

print("updated dictionary: ", people)
