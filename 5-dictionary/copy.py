"""
! category : easy
TODO : 1. Create a dictionary containing information about a person's profile, such as: Name, Age, City, 2. Copy the entire contents of that dictionary to a new dictionary using the appropriate dictionary copy method, 3. Change the age in the new dictionary without changing the value in the original dictionary, 4. Display both dictionaries (original and copy) to prove that the change only occurred in the copy.
"""

ori_data_person = {"Name": "Sasuke", "Age": 20, "City": "Utopia"}

copy_data_person = ori_data_person.copy()
copy_data_person["Age"] = 25

print(f"original data person: {ori_data_person}")
print(f"\ncopy data person: {copy_data_person}")

"""
! category : medium
TODO : 1. Given a product dictionary containing product names as keys and prices as values, 2. Copy the entire contents of the dictionary to a new dictionary using the appropriate dictionary copy method, 3. In the new dictionary, add a new product along with its price, 4. Remove one product from the new dictionary without affecting the original dictionary, 5. Print both dictionaries (original and copy) to prove that changes only occurred in the copied dictionary.
"""

products = {"Casing Handphone": 50000, "Perfume": 100000, "Hoodie": 125000}

copy_product = dict(products)
copy_product["Tote Bag"] = 45000
del copy_product["Casing Handphone"]

print(f"\noriginal data products: {products}")
print(f"copy data products: {copy_product}")
