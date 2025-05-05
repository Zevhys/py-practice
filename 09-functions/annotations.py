"""
! Category: Easy
Todo: Create a function called multiply_by_two that takes one parameter which is an integer, and returns the result of that number multiplied by two. You must explain that the parameter is of type int and the returned value is also of type int. After that, ask the user to input a number, call the function, and display the result.
"""


def multiply_by_two(a: int) -> int:
    return a * 2


print(multiply_by_two(2), "\n")

"""
! Category: Medium
Todo: Create a function called format_profile that takes three parameters: 1. name (data type: str), 2. age (data type: int), 3. is_student (data type: bool). This function should return a string containing information formatted with the following template: Name: <name>, Age: <age>, Student Status: <Yes/No>. If is_student is True, display "Yes", if not display "No". After that, ask the user to enter their name, age, and student status, then call the function and display the result.
"""


def format_profile(name: str, age: int, is_student: bool) -> str:
    return f"\nname: {name}\nage: {age}\nstudent status: {is_student}"


user_name = input("enter name: ")
user_age = int(input("enter age: "))
user_status = input("Are you a student? (yes/no): ").lower()
status_result = user_status == "yes"
print(format_profile(user_name, user_age, status_result))
