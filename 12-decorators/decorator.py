"""
! Category: Easy
Todo: Create a decorator named timer_decorator that will measure and display the execution time of the decorated function. This decorator must: 1. Calculate the start time before the function is executed, 2. Run the function, 3. Calculate the end time after the function is executed, 4. Display the message: "Function [function_name] completed execution in [execution_time] seconds", 5. Return the result of the executed function, Then create a function named count_numbers that accepts a parameter n and performs the sum from 1 to n using a loop (not a mathematical formula). Apply the timer_decorator to this function.
"""

import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(
            f"function {func.__name__}() completed execution in {duration:.4f} seconds\n"
        )
        return result

    return wrapper


@timer_decorator
def count_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


count_numbers(1000000)


"""
! Category: Medium
Todo: Create a decorator named validate_input that will validate the input of a function before executing it. This decorator must: 1. Check whether all function arguments are of the correct data type, 2. If the data type is incorrect, display an error message and return None, 3. If the data type is correct, execute the function and return its result. Implement this decorator on two different functions: 1. Function multiply_numbers(a, b) that: ‣Expects input of two numbers (int or float), ‣Returns the product of a and b, 2. Function greet_user(name, times) that: ‣Expects string input for name and integer for the number of repetitions, ‣Displays the greeting "Hello, [name]!" times number of times. The validate_input decorator must recognize the expected data type of the function parameters through comments or type annotations. When called with correct arguments, the function will run normally. But if the data type is incorrect, for example multiply_numbers("2", 3), the decorator will display an error message like "Error: Parameter 'a' must be of type int, but was given str".
"""

import inspect


def validate_input(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        parameters = list(sig.parameters.values())

        for i, arg in enumerate(args):
            if i < len(parameters):
                param_name = parameters[i].name
                expected_type = func.__annotations__.get(param_name)

                if expected_type and not isinstance(arg, expected_type):
                    print(
                        f"\nError: Parameter '{param_name}' must be of type {expected_type.__name__}, but given {type(arg).__name__}"
                    )
                    return None

        for param_name, arg in kwargs.items():
            expected_type = func.__annotations__.get(param_name)

            if expected_type and not isinstance(arg, expected_type):
                print(
                    f"Error: Parameter '{param_name}' must be of type {expected_type.__name__}, but given {type(arg).__name__}"
                )
                return None

        return func(*args, **kwargs)

    return wrapper


@validate_input
def multiply_numbers(a: int, b: int):
    return a * b


@validate_input
def greet_user(name: str, times: int):
    for _ in range(times):
        print(f"Hello, {name}!")
    return None


result = multiply_numbers(5, 3)
print(f"result: {result}\n")
greet_user("Alice", 2)
result = multiply_numbers("5", 3)
greet_user("Bob", "2")
