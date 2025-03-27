"""
! category : easy
TODO : Create a nested dictionary that stores information about two students. Each student has the following data: Name, Age, Favorite Subject. Instructions: 1. Create a dictionary with a nested structure containing data for two students, 2. Display the age of one of the students using access to the nested dictionary, 3. Add a new hobby to one of the students' data, 4. Print the entire contents of the dictionary after it has been updated.
"""

students = {
    "Student1": {"Name": "Gon", "Age": 19, "Favorite Subject": "Math"},
    "Student2": {"Name": "Kurapika", "Age": 18, "Favorite Subject": "Chemistry"},
}

print(f"display the age of one of the students: {students["Student1"]["Age"]}\n")

students["Student2"]["Hobby"] = "Hiking"
print(f"add a new hobby to one of the students: {students["Student2"]["Hobby"]}")

print(f"\nprint the updated dictionary: {students}\n")

"""
! category : medium
TODO : You are given a nested dictionary containing product data in online store categories. Each category has several products, where each product has the following information: Product Name, Price, Stock. Instructions: 1. Create a dictionary with a nested structure for at least two product categories (example: Electronics and Fashion), 2. Display the price of one product in a specific category, 3. Update the stock of one product in that category, 4. Add a new product to one of the categories, 5. Print the updated dictionary.
"""

products = {
    "Electronic": {"Handphone": {"Price": 5000000, "Stock": 1}},
    "Fashion": {"T-shirt": {"Price": 100000, "Stock": 1}},
}

price_product = products["Electronic"]["Handphone"]["Price"]
print(f"display the price of one product: {price_product}\n")

products["Fashion"]["T-shirt"]["Stock"] = 2
print(f"update a product stock: {products["Fashion"]["T-shirt"]["Stock"]}")

products["Electronic"]["Television"] = {"Price": 2000000, "Stock": 2}
print(f"\nadd a new product: {products["Electronic"]["Television"]}")

print(f"\nprint the updated dictionary: {products}")
