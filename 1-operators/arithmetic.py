"""
! category : easy
TODO : Create a program that converts time input in seconds into hours, minutes, and seconds format. The program must : Accept input in the form of an integer representing the number of seconds, Use arithmetic operators to calculate hours, minutes, and remaining seconds, the result in the format "X hours, Y minutes, Z seconds"
"""


def conversion_time(total_seconds):
    hours = total_seconds // 3600

    remain_seconds = total_seconds % 3600

    minutes = remain_seconds // 60

    seconds = remain_seconds % 60

    return f"{hours} hour, {minutes} minute, {seconds} second"


time_second = int(input("enter number seconds : "))
result = conversion_time(time_second)
print(result)

"""
! category : medium
TODO :
"""
