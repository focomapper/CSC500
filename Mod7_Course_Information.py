# Create room number dict
room_number = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Create instructor dict
instructor = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Create course time dict
meeting_time = {
    "CSC101": "8:00a.m.",
    "CSC102": "9:00a.m.",
    "CSC103": "10:00a.m.",
    "NET110": "11:00a.m.",
    "COM241": "1:00p.m."
}

# Get user input for course number
course_number = input("Enter course number: ")

# Validate if course exists and return course information
try:
    print(f"Course: {course_number}")
    print(f"Location: Room {room_number[course_number]}")
    print(f"Instructor: {instructor[course_number]}")
    print(f"Meeting time: {meeting_time[course_number]}")
except KeyError:
    print("Course does not exist, enter valid course number")
    exit()


