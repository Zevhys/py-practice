"""
! category : easy
todo : Create a program that asks the user to enter 5 integer numbers and stores them in a list. Check if at least one number in the list is negative.
"""

number_input = list(map(int, input("enter numbers: ").split()))

if any(num < 0 for num in number_input):
    print("there is a negative number in the list")
else:
    print("all numbers are non-negative")

"""
! category : medium
todo :  Create a program that asks the user to enter a sentence. Check if all the words in the sentence have more than 3 letters.
"""

sentence_input = input("enter sentence: ").split()

if all(len(word) > 3 for word in sentence_input):
    print("all words have more than 3 letters")
else:
    print("not all words have more than 3 letters")
