"""
! category: easy
TODO: Create a program that asks the user to enter a list of numbers in the form of a comma-separated string, for example: 1,2,3,4,5. Then: 1. Convert this input into a list of integers, 2. Use the map() function together with lambda to multiply each number in the list by 3, 3. Display the final result in the form of a list of multiplied numbers.
"""

input_number = [int(x.strip()) for x in input("enter number: ").split(",")]
print(list(map(lambda x: x * 3, input_number)), "\n")

"""
! category: medium
TODO: Create a function that accepts a list of integer numbers, then: Filter out only the even numbers, Convert the even numbers into strings with the format "even:<number>", Return the resulting list of strings from this process and display it.
"""


def process_even_numbers(numbers: list[int]):
    even = list(filter(lambda x: x % 2 == 0, numbers))
    result = list(map(lambda x: f"even: {x}", even))
    return result


print(process_even_numbers([1, 2, 3, 4, 5, 6]))
