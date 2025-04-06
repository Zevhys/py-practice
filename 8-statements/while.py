"""
! category: easy
TODO: Create a program that asks the user to enter positive integers one by one. The program should keep asking for input until the user enters an even number for the first time. After that, the program prints the total number of integers entered (including the even number) and stops.
"""

counter = 0

while True:
    number_input = int(input("enter number: "))
    counter += 1

    if number_input % 2 == 0:
        print(f"\ntotal numbers: {counter}\n")
        break

"""
! category: medium
TODO: Create a program that simulates a simple login system. The correct password is "python123". The program should: 1. Ask the user to input a password using input(), 2. Allow a maximum of 3 attempts, 3. If the user enters the correct password, display the message "Access granted" and stop the program, 4. If the user fails to enter the correct password after 3 attempts, display "Access denied" and stop the program.
"""

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password_input = input("enter password: ")

    if password_input == "python123":
        print("\naccess granted")
        break
    else:
        attempts += 1

if attempts == max_attempts:
    print("\naccess denied")
