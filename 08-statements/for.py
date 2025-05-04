"""
! Category: Easy
Todo: Create a program that asks the user to input a positive integer n. The program should then print all even numbers from 1 to n (including n if it is even).
"""

number_input = int(input("enter positive integer number: "))

for n in range(1, number_input + 1):
    if n % 2 == 0:
        print(f"{n}")

"""
! Category: Medium
Todo: Create a program that asks the user to input a sentence (string). The program should count and print: 1. The number of vowels (a, i, u, e, o), 2. The number of consonants (excluding vowels and spaces).
"""

string_input = input("\nenter a sentence: ")
vowels = 0
chars = 0

for w in string_input:
    if w.lower() in ("a", "e", "i", "o", "u"):
        vowels += 1
    elif w != " " and w.isalpha() and w.lower() not in ("a", "e", "i", "o", "u"):
        chars += 1


print(f"number of vowels are: {vowels}")
print(f"number of characters (excluding vowels and spaces): {chars}")
