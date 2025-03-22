"""
! category : easy
TODO : 1. Create two tuples, each containing several integers (e.g., minimum 4 elements in each tuple), 2. Combine both tuples into one tuple using tuple operations, 3. Use slicing on the combined tuple to get every 2nd element (e.g., take elements at indices 0, 2, 4, etc), 4. Ask for user input of a number, then count how many times that number appears in the combined tuple. (Use the appropriate tuple method to count occurrences of elements), 5. Print the combined tuple, the slicing result, and the number of occurrences of the entered number.
"""

number1 = (1, 2, 3, 4)
number2 = (5, 6, 7, 8)
combined_number = number1 + number2
print(f"\ncombined tuple: {combined_number}")

print(f"\neach 2nd element: {combined_number[::2]}")

user_input = int(input("\nenter number to check: "))

check_number = combined_number.count(user_input)
print(f"\nthe number {user_input} appears as many as: {check_number}\n")

"""
! category : medium
TODO : You have data for several students with their names and scores in the form of tuples. Your task is to process this data with tuple operations. Format: (name, (math_score, language_score, science_score)) student_data = [("Ani", (85, 90, 78)), ("Budi", (70, 65, 80)), ("Cindy", (90, 88, 92)), ("Dodi", (75, 80, 85))]. Instructions: 1. Create a function average_score(score_tuple) that takes a tuple of scores and returns the average, 2. Use tuple unpacking to get the name of the student with the highest average score, 3. Create a new tuple containing student names and their math scores, then sort by math score from highest to lowest, 4. Add a new student data ("Eko", (88, 85, 90)) to student_data using concatenation operation, 5. Use tuple slicing to get the first 2 students from the updated student_data.
"""

student_data = [
    ("Ani", (85, 90, 78)),
    ("Budi", (70, 65, 80)),
    ("Cindy", (90, 88, 92)),
    ("Dodi", (75, 80, 85)),
]


def average_score(a, b, c):
    total = a + b + c
    return total / 3


print(f"function average_score: {average_score(85, 90, 78):.2f}")

highest_average = max(student_data, key=lambda x: sum(x[1]) / len(x[1]))[0]
print("\nstudent with the highest average score:", highest_average)

name_math = [(s[0], s[1][0]) for s in student_data]
sort_math = sorted(name_math, key=lambda x: x[1], reverse=True)
print("\nstudent names and their math scores:", sort_math)

new_student = student_data + [("Eko", (88, 85, 90))]
print("\nadd a new student data:", new_student)

slicing_students = student_data[:2]
print("\nGet first 2 students using slicing:", slicing_students)
