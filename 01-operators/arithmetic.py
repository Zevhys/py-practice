"""
! category: Easy
Todo: Create a program that calculates the average of 3 exam scores. The program should: 1. Ask the user to input 3 exam scores (Mathematics, Physics, and Language), 2. Calculate the average of these three scores, 3. Display the average result with 2 decimal places.
"""


def average_value(math, physics, language):
    result = (math + physics + language) / 3

    return f"\ncalculation results:\naverage value: {'%.2f' % result}\n"


print("average calculator value\n========================")
math = float(input("enter value math: "))
physics = float(input("enter value physics: "))
language = float(input("enter value language: "))
print(average_value(math, physics, language))

"""
! Category: Medium
Todo: Create a program that converts time input in seconds into hours, minutes, and seconds format. The program must: 1. Accept input in the form of an integer representing the number of seconds, 2. Use arithmetic operators to calculate: ‣Hours, ‣Minutes, ‣Remaining seconds, 3. Display the result in the format "X hours, Y minutes, Z seconds".
"""


def conversion_time(total_seconds):
    hours = total_seconds // 3600
    remain_seconds = total_seconds % 3600
    minutes = remain_seconds // 60
    seconds = remain_seconds % 60

    return f"\nconversion results:\n{total_seconds} seconds = {hours} hour, {minutes} minute, {seconds} second"


print("time conversion calculator\n==========================")
time_second = int(input("enter number seconds: "))
result = conversion_time(time_second)
print(result)
