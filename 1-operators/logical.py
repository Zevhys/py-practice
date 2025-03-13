"""
! category : easy
TODO: Create a program that determines whether a person qualifies for a scholarship program. The program must : (1). Request input from the user : Academic score (0-100), Age (in years) Employment status (working/not working - input as True/False), (2). Use logical operators (and, or, not) to determine : Eligible Category 1: If academic score is above 80 AND age is below 25, Eligible Category 2: If academic score is above 90 OR age is below 20, Eligible Category 3: If academic score is above 70 AND NOT working, (3). Display the eligibility results for all three categories (True/Fa
"""

print("eligibility checker\n===================")
academic_value = int(input("enter academic value (0-100) : "))
age = int(input("enter age : "))
has_work = input("are you working (True/False) : ").lower() == "true"

print(
    f"\neligibility check results : \nCategory 1 (value > 80 and age < 25) : {academic_value > 80 and age < 25}\nCategory 2 (value > 90 or age < 20) : {academic_value > 90 or age < 20}\nCategory 3 (value > 70 and doesn't work) : {academic_value > 70 and not has_work}\n"
)

"""
! category : medium
TODO:
"""

print("password validator\n==================")
password = input("enter password : ")
length = len(password) >= 8
upper = any(char.isupper() for char in password)
lower = any(char.islower() for char in password)
number = any(char.isdigit for char in password)

if length and upper and lower and number:
    strength = "very strong"
elif length and ((upper and lower) or (upper and number) or (lower and number)):
    strength = "strong"
elif length and (upper or lower or number):
    strength = "medium"
elif length:
    strength = "weak"
else:
    strength = "very weak"

print(
    f"\nvalidation results : \nminimum length of 8 characters : {length}\ncontains uppercase : {upper}\ncontains lowercase : {lower}\ncontains number : {number}\n\npassword strength : {strength}"
)
