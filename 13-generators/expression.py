"""
! Category: Easy
Todo: Create a function named filter_words that uses a generator expression to filter words from a list. This function must: 1. Accept two parameters: ‣words: A list containing words (strings), ‣min_length: The minimum length of words to be filtered (integer), 2. Use a generator expression (not a list comprehension) to filter words with lengths greater than or equal to min_length, 3. Return the generator expression directly (without converting it to a list), 4. Add code to test the function by calling filter_words using the following word list: ["apple", "banana", "cherry", "date", "elderberry", "fig"] and min_length 5, then print the results using a for loop.
"""


def filter_words(words, min_length):
    result = (x for x in words if len(x) >= min_length)

    for word in result:
        print(word)


test = filter_words(["apple", "banana", "cherry", "date", "elderberry", "fig"], 5)

"""
! Category: Medium
Todo: Create a function named sum_of_squares that uses a generator expression to calculate the sum of squares of numbers that meet a specific condition. This function must: 1. Accept two parameters: ‣numbers: A list containing numbers (integers or floats), ‣condition: A string representing the filtering condition, which can be: •"even" = only even numbers, •"odd" = only odd numbers, •"positive" = only positive numbers, •"all" = all numbers, 2. Use a generator expression to: ‣Filter numbers based on the given condition, ‣Calculate the square of each filtered number, ‣Use the sum() function to add up all these squares, 3. Return the sum of these squares, 4. Add code to test the function by calling sum_of_squares using the following list of numbers: [-3, -2, -1, 0, 1, 2, 3, 4] and print the results for each condition ("even", "odd", "positive", and "all").
"""


def sum_of_squares(numbers, condition):
    if condition == "even":
        return sum(x**2 for x in numbers if x % 2 == 0)
    elif condition == "odd":
        return sum(x**2 for x in numbers if x % 2 != 0)
    elif condition == "positive":
        return sum(x**2 for x in numbers if x > 0)
    elif condition == "all":
        return sum(x**2 for x in number)


number = [-3, -2, -1, 0, 1, 2, 3, 4]
result_even = sum_of_squares(number, "even")
print(f"\nsum of squares (even): {result_even}")

result_odd = sum_of_squares(number, "odd")
print(f"sum of squares (odd): {result_odd}")

result_positive = sum_of_squares(number, "positive")
print(f"sum of squares (positive): {result_positive}")

result_all = sum_of_squares(number, "all")
print(f"sum of squares (all): {result_all}")
