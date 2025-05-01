"""
! Category: Easy
Todo: Create a program that uses string slicing techniques to extract various parts of this string: message = "Python3.9_Programming_Tutorial". Your program should: 1. Display the first 6 characters of the string, 2. Display the last 8 characters of the string, 3. Display the characters from index 7 to 12, 4. Display the entire string in reverse order, 5. Display only the characters at even index positions (0, 2, 4, etc.).
"""

message = "Python3.9_Programming_Tutorial"

print(
    f"first 6 characters: {message[0:6]}\nlast 8 characters: {message[22:]}\ncharacter index 7-12: {message[7:12]}\nreverse Sentences: {message[::-1]}\neven Index Character: {message[::2]}\n"
)

"""
! Category: Medium
Todo: Create a program that works with the string: text = "Data_Science_and_Machine_Learning_2023". Your program needs to use string slicing to: 1. Extract the word "Science" (characters 5 to 11), 2. Extract the word "Machine" (using negative indices), 3. Reverse the order of the word "Learning" (using proper indices), 4. Take every third character from the entire string (indices 0, 3, 6, etc.), 5. Take the last 4 characters and combine them with the first 4 characters in one variable.
"""

text = "Data_Science_and_Machine_Learning_2023"

print(
    f"word 'Science': {text[5:12]}\nword 'Machine' (with a negative index): {text[-21:-14]}\nreverse word 'Learning': {text[32:24:-1]}\neach third character: {text[::3]}\nthe last 4 characters + 4 first characters: {text[-4:] + text[:4]}"
)
