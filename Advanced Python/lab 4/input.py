import math
import numpy as np
import domains

students = []
courses = []
marks = []

# Input number of students in a class
numOfStudents = int(input("How many students are there in a class ? \n"))

# Input student information: id, name, DoB
for i in range(0, numOfStudents):
    print(f"Student {i+1}'s informations: ")
    id = input("Id: ")
    name = input("Name: ")
    dob = input("Dob (format: dd/mm/yy): ")
    students.append(domains.student(id, name, dob))

    i += 1

# Input number of courses
numOfCourses = int(input("How many courses are there ? \n"))

# Input course information: id, name
for j in range(0, numOfCourses):
    print(f"Course {j+1}'s informations: ")
    id = input("Id: ")
    name = input("Name: ")
    studentsList = students

    courses.append(domains.course(id, name, studentsList, 0))

    j += 1

courseSelection = 1
while courseSelection in range(1, numOfCourses + 1):
    courseSelection = int(
        input(
            f"To enter marks for student, select a course (from 1 to {numOfCourses}, type 0 to quit): "
        )
    )

    if courseSelection == 0:
        break

    for k in range(0, numOfStudents):
        print(f"Mark for student {students[k].getStudentName()}: ")
        _mark = round(float(input()), 1)
        marks.append(_mark)

        k += 1

    courses[courseSelection - 1].markList = marks[
        (courseSelection - 1) * numOfStudents : courseSelection * numOfStudents
    ]
