"""
! Category: Easy
Todo: Create a program that asks the user to enter a number. The program should perform the following checks: 1. If the number is greater than 0, print "Positive number", 2. If the number is less than 0, print "Negative number", 3. If the number is equal to 0, print "Zero".
"""

number_input = int(input("enter number: "))

if number_input > 0:
    print("positive number\n")
elif number_input < 0:
    print("negative number\n")
else:
    print("zero number\n")

"""
! Category: Medium
Todo: Create a program that asks the user to enter an exam score (0 - 100). Based on the score, the program should output the grade as follows: 1. Score 80 - 100 → "A (Very Good)", 2. Score 65 - 79 → "B (Good)", 3. Score 50 - 64 → "C (Fair)", 4. Score 35 - 49 → "D (Poor)", 5. Score 0 - 34 → "E (Very Poor)", 6. If the score is outside the range of 0 - 100, print "Invalid score".
"""

grade_input = int(input("enter an exam score: "))

if grade_input < 0 or grade_input > 100:
    print("invalid score")
elif grade_input >= 80:
    print("A (very good)")
elif grade_input >= 65:
    print("B (good)")
elif grade_input >= 50:
    print("C (fair)")
elif grade_input >= 35:
    print("D (poor)")
else:
    print("E (very poor)")
