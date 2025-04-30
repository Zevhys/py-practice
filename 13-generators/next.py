"""
! category: easy
TODO: Create a generator function named fibonacci_generator that produces Fibonacci numbers in sequence. This function must: 1. Accept one parameter limit that determines how many Fibonacci numbers to generate, 2. Produce Fibonacci numbers starting from 0, 1, 1, 2, 3, 5, ... (in order), 3. Stop after producing the specified limit of numbers. After creating the generator, also write code to print these Fibonacci numbers using a for loop.
"""


def fibonacci_generator(limit):
    a = 0
    b = 1

    for i in range(limit):
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator(7)

for number in fibonacci:
    print(number)

"""
! category: medium
TODO: Create a generator named custom_enumerate that mimics Python's built-in enumerate() function but with additional capabilities. This generator must: 1. Accept three parameters: iterable: An object that can be iterated (for example list, string, tuple), start_index: Starting value for the index (default = 0), step: Increment value for each subsequent index (default = 1). 2. Produce pairs of (index, value) for each element in the iterable index starts from start_index and increases by step with each iteration, value is the value of the element at the current iteration position. 3. Implement using the yield keyword 4. Ensure the generator function can be used with a for loop just like the built-in enumerat ()
"""


def custom_enumerate(sequence, start_index=0, step=1):
    for elem in sequence:
        yield start_index, elem
        start_index += step


print()

for idx, val in custom_enumerate(["a", "b", "c"], start_index=10, step=5):
    print(f"index: {idx}, value: {val}")
