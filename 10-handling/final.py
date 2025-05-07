"""
! Category: Easy
Todo: Create a program that asks the user to input two numbers. Then, perform division of these two numbers. Catch possible errors (for example division by zero), but always display the message "program completed" at the end, regardless of whether an error occurred or not.
"""

try:
    a = int(input("first number: "))
    b = int(input("second number: "))
    result = a / b
    print(f"\n{a} / {b} = {result:,.0f}")
except ValueError:
    print(f"\nplease enter numeric values")
except ZeroDivisionError:
    print(f"\ncannot divide by zero")
finally:
    print("program completed\n")

"""
! Category: Medium
Todo: Create a function read_file_content() that accepts one parameter which is a file name (str). This function must try to open the file and display the contents of the file. If the file is not found, display an appropriate message. Display the message "file reading process completed", which must appear regardless of the outcome of the process.
"""


def read_file_content(name):
    try:
        with open(name, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"files are not found: {name}")
    finally:
        print("file reading process completed")


read_file_content("data.txt")
