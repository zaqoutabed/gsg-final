from utils import (
    is_valid_email,
    is_valid_mobile_number,
    is_valid_dob,
    is_valid_name,
    is_valid_address,
    is_valid_id,
    is_valid_float,
    is_valid_time,
    is_valid_duration,
)

from db import get_levels, add_student_details, add_course_details, student_enroll, add_course_schedule, get_student_schedule


def add_student():
    print("\n")
    print("Register New Student!")

    ids, levels = get_levels()
    levels_str = ", ".join(levels)
    levels = [level.lower() for level in levels]

    student_name = ""
    dob = ""
    level = ""
    mobile = ""
    email = ""
    address = ""

    while True:
        student_name = input(
            "Enter Student Name.\n\t[!] Only alphabetical and white spaces\n\t[!] Name should be from 4 to 40 charachters\n\t[!] Multi spaces will ignored : "
        )
        is_valid, msg = is_valid_name(student_name)
        if is_valid:
            name = msg
            break
        print(msg)

    while True:
        dob = input("Enter student date of birth.\n\t[!] Use format YYYY-MM-DD : ")
        is_valid, msg = is_valid_dob(dob)
        if is_valid:
            break
        print(msg)

    while True:
        level = input("Enter student Level.\n\t[!] Select From ({}) : ".format(levels_str))
        level = level.lower()
        if level in levels:
            break
        print("Invalid Level Selected!")

    while True:
        mobile = input("Enter student mobile number.\n\t[!] Only Digits allowed : ")
        is_valid, msg = is_valid_mobile_number(mobile)
        if is_valid:
            mobile = msg
            break
        print(msg)

    while True:
        email = input("Enter student email.\n\t[!] Enter Valid Email : ")
        is_valid, msg = is_valid_email(email)
        if is_valid:
            email = msg
            break
        print(msg)

    while True:
        address = input(
            "Enter student address.\n\t[!] Only alphabetical,( _ ), ( - ), digits and white spaces\n\t[!] Multi spaces will ignored : "
        )
        is_valid, msg = is_valid_address(address)
        if is_valid:
            address = msg
            break
        print(msg)

    level = ids[levels.index(level)]
    added = add_student_details(student_name, dob, level, mobile, email, address)
    if added:
        print("Student Added succesfuly")


def enroll_couse():
    std_id = input("Enter student Id. ")
    course_id = input("Enter course Id. ")
    added = student_enroll(std_id, course_id)
    if added:
        print("Student enroll succesfuly")


def add_course():
    print("\n")
    print("Add New Course!")

    ids, levels = get_levels()
    levels_str = ", ".join(levels)
    levels = [level.lower() for level in levels]

    course_id = -1
    course_name = ""
    level = ""
    max_capacity = 0
    hour_rate = -1
    while True:
        course_id = input("Enter Course Id.\n\t[!] Only Positive values : ")
        is_valid, msg = is_valid_id(course_id)
        if is_valid:
            course_id = msg
            break
        print(msg)

    while True:
        course_name = input(
            "Enter Course Name.\n\t[!] Only alphabetical and white spaces\n\t[!] Name should be from 4 to 40 charachters\n\t[!] Multi spaces will ignored : "
        )
        is_valid, msg = is_valid_name(course_name)
        if is_valid:
            course_name = msg
            break
        print(msg)

    while True:
        max_capacity = input("Enter Course Capacity.\n\t[!] Only Positive values\n\t[!] Enter number between 1 and 40: ")
        is_valid, msg = is_valid_id(max_capacity)
        if is_valid:
            if 40 < msg < 1:
                print
            max_capacity = msg
            break
        print(msg)

    while True:
        level = input("Enter Course Level.\n\t[!] Select From ({}) : ".format(levels_str))
        level = level.lower()
        if level in levels:
            break
        print("Invalid Level Selected!")

    while True:
        hour_rate = input("Enter Course Hour Rate.\n\t[!] Only Positive values : ")
        is_valid, msg = is_valid_float(hour_rate)
        if is_valid:
            hour_rate = msg
            break
        print(msg)

    level = ids[levels.index(level)]
    added = add_course_details(course_id, course_name, level, max_capacity, hour_rate)
    if added:
        print("Course Added succesfuly")


def create_schedule():
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekdays_str = ", ".join(weekdays)
    weekdays = [day.lower() for day in weekdays]
    weekday = ""
    course_id = ""
    course_time = ""
    duration = 0

    while True:
        weekday = input("Enter Weekday.\n\t[!] Select From ({}) : ".format(weekdays_str))
        weekday = weekday.lower()
        if weekday in weekdays:
            break
        print("Invalid Weekday Selected!")
    
    while len(course_id) == 0:
        course_id = input("Enter course Id. ")
    
    
    while True:
        course_time = input("Enter Start time.\n\t[!] Use format HH:MM 24 hour format : ")
        is_valid, msg = is_valid_time(course_time)
        if is_valid:
            course_time = course_time+":00"
            break
        print(msg)
    
    end_time = None
    while True:
        duration = input("Enter Course Duration.\n\t[!] Only Positive number values : ")
        is_valid, msg = is_valid_id(duration)
        if is_valid:
            duration = msg
            is_valid, msg = is_valid_duration(course_time, duration)
            if is_valid:
                end_time = str(msg)
                break
        print(msg)
    added = add_course_schedule(course_id, weekday, course_time, duration, end_time)
    if added:
        print("Course schedule Added succesfuly")

def display_schedule():
    std_id = input("Enter student Id. ")
    status, data = get_student_schedule(std_id)
    if status:
        print(data)

def main():
    while True:
        print("Welcome to Studetns Registration")
        print("Select one of options")
        print("[1] Register New Student")
        print("[2] Enroll Course")
        print("[3] Create New Course")
        print("[4] Create New Schedule")
        print("[5] Display Student Courses Schedule")
        print("[6] Exit")
        try:
            option = int(input("\tOption :? "))
        except:
            option = -1
        match option:
            case 1:
                add_student()
            case 2:
                enroll_couse()
            case 3:
                add_course()
            case 4:
                create_schedule()
            case 5:
                display_schedule()
            case 6:
                print("Bye!")
                break
            case _:
                print("Option not recognized")


if __name__ == "__main__":
    main()
