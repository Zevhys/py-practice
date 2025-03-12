"""
! category : easy
TODO: Create a program that asks the user to input a number, then determines the category of that number. The program must : Request a number input from the user Use comparison operators to check and display the following : Is the number greater than 0 (positive)?, Is the number less than 0 (negative)?, Is the number equal to 0?, Is the number even or odd?, Is the number greater than 100 or less than/equal to 100?
"""

print("Check the numbers category\n==========================")
num = int(input("enter a number : "))
print(
    f"\npositive : {num > 0}\nnegative : {num < 0}\nequal to zero: {num == 0}\neven : {num % 2 == 0}\nodd : {num % 2 != 0}\ngreater than 100 : {num > 100}\nless than or equal to 100 : {num <= 100}\n",
)

"""
! category : medium
TODO: Create a program that helps determine a student's passing status and grade category. The program must : Ask for the midterm (UTS) and final exam (UAS) scores from the user (range 0-100), Calculate the final score with the following weights: 40% midterm and 60% final exam, Use comparison operators to determine : Passing status: Pass if the final score is >= 60, fail if < 60, Grade category : A: final score >= 85, B: final score >= 70 and < 85, C: final score >= 60 and < 70, D: final score >= 50 and < 60, E: final score < 50, Perfect score: if the final score = 100, Is the final exam score higher than the midterm score?, Are both scores (midterm and final exam) equal?
"""


print(
    "determination of student value Categories\n========================================="
)

grade_uts = float(input("Enter the uts value (0-100) : "))
grade_uas = float(input("Enter the uas value (0-100) : "))
final_score = (grade_uts * 0.4) + (grade_uas * 0.6)


def value_category(grade):
    if grade >= 85:
        return "a"
    elif grade >= 70:
        return "b"
    elif grade >= 60:
        return "c"
    elif grade >= 50:
        return "d"
    else:
        return "e"


print(
    f"\nanalysis results:\nfinal score : {final_score}\nstatus : {"passed" if final_score >= 60 else "not pass"}\nvalue category : {value_category(final_score)}\nperfect value : {final_score == 100}\nthe uas value is higher than uts : {grade_uas > grade_uts}\nuts and uas values ​​are the same : {grade_uts == grade_uas}"
)
