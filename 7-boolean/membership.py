"""
! category : easy
TODO :  Create a program that checks if a name is in the list of students in a class. Check if the name entered by the user is in the list. If it is, print "Name found in the list.", if not, print "Name not found in the list." Available student list: students = ["Rina", "Budi", "Ani", "Joko", "Sari"]. Instructions: 1. Check if the user's input is in the list, 2. Ensure the program can accept input from the user.
"""

students = ["Rina", "Budi", "Ani", "Joko", "Sari"]
user_input = input("please enter name students: ")

if user_input in students:
    print("name found in the list students")
else:
    print("name not found in the list students")

"""
! category : medium
TODO : Create a program that checks if all the letters of a word are present in a sentence. The program should: 1. Accept a word input from the user, 2. Accept a sentence input from the user, 3. Check each letter in the word to see if it is in the sentence using the "not in" operator, 4. If any letter is not found in the sentence, print "Not all letters of the word are present in the sentence", 5. If all letters are found, print "All letters of the word are present in the sentence".
"""

word_input = input("enter word: ")
sentence_input = input("enter sentence: ")

for letter in word_input:
    if letter not in sentence_input:
        print("\nNot all letters of the word are in sentences.")
        break
else:
    print("\nAll letters of the word are in sentences.")
