"""
! category : easy
TODO : Given two sets containing lists of hobbies from two people, namely Naruto and Sasuke. 1. Display the union of both sets, 2. Display the difference of Naruto's hobbies relative to Sasuke's, 3. Display the difference of Sasuke's hobbies relative to Naruto's.
"""

naruto_hobbies = {"Reading", "Cooking", "Cycling"}
sasuke_hobbies = {"Cooking", "Writing", "Singing"}

print(f"union both sets: {naruto_hobbies | sasuke_hobbies}\n")
print(f"difference naruto hobbies to sasuke: {naruto_hobbies - sasuke_hobbies}\n")
print(f"difference sasuke hobbies to naruto: {sasuke_hobbies - naruto_hobbies}\n")

"""
! category : medium
TODO : Given two sets containing lists of elective subjects taken by Class X and Class Y. 1. Display the intersection of both classes, 2. Display the symmetric difference of both classes.
"""

class_x = {"Math", "Biology", "Language", "Physics"}
class_y = {"Physics", "Art", "Language", "History"}

print(f"intersection of both classes: {class_x & class_y}\n")
print(f"symmetric difference of both classes: {class_x ^ class_y}\n")
