"""
! Category: Easy
Todo: Create a Python program that accepts text from user input and performs simple analysis on the text using at least 5 different string methods. Your program must: 1. Count the total characters in the text (including spaces), 2. Count the number of words in the text, 3. Convert the text to all capital letters and display it, 4. Count how many times the letter 'a' appears (not case sensitive).
"""

user_text = input("enter text: ")

print(f"\nanalysis results")
print(f"total character: {len(user_text)}")
print(f"total of words: {len(user_text.split())}")
print(f"text in capital: {user_text.upper()}")
print(f"total number of letter 'a': {user_text.lower().count('a')}")

"""
! Category: Medium
Todo: Create a Python program that accepts full name input from the user (can consist of 2-4 words) and formats the name using at least 4 different string methods. Your program must: 1. Convert the name to title case format (capitalize the first letter of each word), 2. Create an abbreviation (initials) from each word in the name (for example "John Doe" becomes "JD"), 3. Create a username version of the name by removing spaces and converting all letters to lowercase, 4. Display the name in the format "Last Name, First Name" (for example "John Doe" becomes "Doe, John"), 5. Display the number of vowels (a, e, i, o, u) in the full name (not case sensitive).
"""

name = input("\nenter a full name: ")
name_parts = name.split()
last_name = name_parts[-1]
first_and_middle = name_parts[:-1]
vowel_count = sum(name.lower().count(vowel) for vowel in "aeiou")
title_case = name.title()
initials = "".join(part[0].upper() for part in name_parts)
username = name.lower().replace(" ", "")
formal_format = f"{last_name.title()}, {' '.join(first_and_middle).title()}"

print("\nresults of the format")
print(f"name (title case): {title_case}")
print(f"initials: {initials}")
print(f"username: {username}")
print(f"format formal: {formal_format}")
print(f"number of vocals in names: {vowel_count}")
