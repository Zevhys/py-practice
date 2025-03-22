"""
! category : easy
TODO : You have a tuple containing phone contact data. Each contact is stored in the format: (name, phone number). Your task is to: 1. Change the phone number of the contact "Ahmad" from "081234567" to "089876543", 2. Add a new contact ("Maya", "087654321") to the contact list, 3. Display the updated contact list. Initial Code: contact_list = (("Budi", "085678901"), ("Ahmad", "081234567"), ("Siti", "082345678"))
"""

contact_list = (("Budi", "085678901"), ("Ahmad", "081234567"), ("Siti", "082345678"))

ahmad_phone = list(contact_list)
ahmad_phone[1] = ("Ahmad", "089876543")
contact_list = tuple(ahmad_phone)
new_contact = list(contact_list)
new_contact.append(("Maya", "087654321"))
contact_list = tuple(new_contact)
print("updated contact list:", contact_list, "\n")

"""
! category : medium
TODO : You have a tuple student_data that contains student information in the format (id, name, math_score, language_score) Your task is to create two functions: 1. update_math_score(student_data, student_id, new_score) - This function returns a new tuple with the updated math score for the student, 2. update_language_score(student_data, student_id, new_score) - This function returns a new tuple with the updated language score for the student. Initial Code: # Student data: (id, name, math_score, language_score) student_data = ((1, "Andi", 85, 70), (2, "Budi", 75, 80), (3, "Citra", 90, 85), (4, "Dewi", 65, 75), (5, "Eko", 80, 90))
"""

student_data = (
    (1, "Andi", 85, 70),
    (2, "Budi", 75, 80),
    (3, "Citra", 90, 85),
    (4, "Dewi", 65, 75),
    (5, "Eko", 80, 90),
)


def update_math_score(student_data, student_id, new_score):
    result = []

    for student in student_data:
        if student[0] == student_id:
            new_grade = (student[0], student[1], new_score, student[3])
            result.append(new_grade)
        else:
            result.append(student)

    return tuple(result)


print(update_math_score(student_data, 2, 85), "\n")


def update_language_score(student_data, student_id, new_score):
    result = []

    for student in student_data:
        if student[0] == student_id:
            new_grade = (student[0], student[1], student[2], new_score)
            result.append(new_grade)
        else:
            result.append(student)

    return tuple(result)


print(update_language_score(student_data, 4, 85))
