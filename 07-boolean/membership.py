"""
! Category: Easy
Todo: Create a program that checks if a name is in the list of students in a class. Initial Data: students = ["Rina", "Budi", "Ani", "Joko", "Sari"]. Tasks: 1. Accept input of a name from the user, 2. Check if the name entered by the user is in the list, 3. If the name is found, print "Name found in the list.", 4. If the name is not found, print "Name not found in the list".
"""

students = ["Rina", "Budi", "Ani", "Joko", "Sari"]
user_input = input("please enter name students: ")

if user_input in students:
    print("name found in the list students")
else:
    print("name not found in the list students")

"""
! Category: Medium
Todo: Create a program that checks if all the letters of a word are present in a sentence. Tasks: 1. Accept a word input from the user, 2. Accept a sentence input from the user, 3. Check each letter in the word to see if it is in the sentence using the "not in" operator, 4. If any letter is not found in the sentence, print "Not all letters of the word are present in the sentence", 5. If all letters are found, print "All letters of the word are present in the sentence".
"""

word_input = input("\nenter word: ")
sentence_input = input("enter sentence: ")

for letter in word_input:
    if letter not in sentence_input:
        print("\nnot all letters of the word are in sentences.")
        break
else:
    print("\nall letters of the word are in sentences.")
