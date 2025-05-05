"""
! Category: Easy
Todo: Create a function called calculate_area() that takes one parameter: side (the length of a side) of a square. The function should return the area of the square. Then, use this function to calculate the area based on user input, and display the result.
"""


def calculate_area(side):
    return side * side


length = int(input("enter the side length: "))
print(f"the area of the square is: {calculate_area(length)}")

"""
! Category: Medium
Todo: Create a function called convert_temperature() that takes two parameters: ‣temp → temperature value (as a number), ‣unit → temperature unit input by the user ("C" for Celsius, "F" for Fahrenheit). This function should return the result of the temperature conversion: ‣If the unit is "C", convert the temperature to Fahrenheit and return the value, ‣If the unit is "F", convert the temperature to Celsius and return the value, ‣If the unit is invalid, return the string "Invalid unit".
"""


def convert_temperature(temp, unit):
    if unit == "c":
        return (temp * 1.8) + 32
    elif unit == "f":
        return (temp - 32) / 1.8
    else:
        return "invalid unit"


temperature = float(input("\nenter temperature: "))
cf = input("enter unit (c/f): ").lower()
result = convert_temperature(temperature, cf)

if result is None:
    print("invalid unit")
else:
    if cf == "c":
        print(f"result: {result:.0f}° fahrenheit")
    elif cf == "f":
        print(f"result: {result:.0f}° celcius")
