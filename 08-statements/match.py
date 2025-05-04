"""
! Category: Easy
Todo: Create a program that asks the user to enter the name of a day in English (e.g., "Monday", "Tuesday", etc.). Print the default activity for that day. You can freely determine the activities in the statements according to the name of the day, but at least 3 different days must have different activities. If the entered day is not recognized, display the message "Invalid day".
"""

day_input = input("enter the name of the day: ").lower()

match day_input:
    case "monday":
        print("you have a meeting at 9 am\n")
    case "tuesday":
        print("reading a book\n")
    case "wednesday":
        print("going for a run\n")
    case "thursday":
        print("cooking dinner\n")
    case "friday":
        print("studying for exams\n")
    case "saturday":
        print("it’s time to relax! enjoy your weekend\n")
    case "sunday":
        print("Watching a movie\n")
    case _:
        print("invalid day\n")

"""
! Category: Medium
Todo: Create a program for a drink cashier system in a simple café. The user is asked to choose one of the following 4 types of drinks: "coffee", "tea", "juice", or "water", and determine the price for each drink. After choosing a drink, the user is also asked to enter the quantity, and the program should print the total final price. The drink prices can be as follows: ‣coffee = 15000, ‣tea = 10000, ‣juice = 12000, ‣water = 5000, If the user enters a drink name that is not on the list, display "Menu not available".
"""

drink_input = input("enter drink choice (coffee/tea/juice/water): ").lower()
qty_input = int(input("enter quantity: "))

coffee = 15000
tea = 10000
juice = 12000
water = 5000

match drink_input:
    case "coffee":
        print("\nyou ordered: coffee")
        print(f"quantity: {qty_input}")
        print("price per item: 15000")
        print(f"total price: {qty_input * coffee}")
    case "tea":
        print("\nyou ordered: tea")
        print(f"quantity: {qty_input}")
        print("price per item: 10000")
        print(f"total price: {qty_input * tea}")
    case "juice":
        print("\nyou ordered: juice")
        print(f"quantity: {qty_input}")
        print("price per item: 12000")
        print(f"total price: {qty_input * juice}")
    case "water":
        print("\nyou ordered: water")
        print(f"quantity: {qty_input}")
        print("price per item: 5000")
        print(f"total price: {qty_input * water}")
    case _:
        print("\nmenu not available")
        exit()
