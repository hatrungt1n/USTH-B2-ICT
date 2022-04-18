import string

courses = []
students = []
marks = []

# Input number of students in a class
numOfStudents = int(input("How many students are there in a class ? \n"))

# Input student information: id, name, DoB
for i in range(0, numOfStudents):
    print(f"Student {i+1}'s informations: ")
    id = int(input("Id: "))
    name = input("Name: ")
    dob = input("Dob (format: dd/mm/yy): ")
    students.append({"id": id, "name": name, "Dob": dob})

    i += 1

# Input number of courses
numOfCourses = int(input("How many courses are there ? \n"))

# Input course information: id, name
for j in range(0, numOfCourses):
    print(f"Course {j+1}'s informations: ")
    _id = int(input("Id: "))
    _name = input("Name: ")
    courses.append({"id": _id, "name": _name, "studentsList": students})

    j += 1

# Select a course, input marks for student in this course
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
        print(f"Mark for student {students[k]['name']}: ")
        mark = int(input())
        marks.append({students[k]["name"]: mark})

        k += 1

    courses[courseSelection - 1]["marks"] = marks[
        (courseSelection - 1) * numOfStudents : courseSelection * numOfStudents
    ]

choices = 1

# Listing functions
while choices < 4:
    choices = int(
        input(
            "If you want to see courses list, please type 1, students list, type 2, student marks, type 3, another number to quit: "
        )
    )

    # List courses
    if choices == 1:
        print("Id".ljust(5, " "), "Name")
        for j in range(0, numOfCourses):
            print(str(courses[j]["id"]).ljust(5, " "), courses[j]["name"])
    # List students
    elif choices == 2:
        print("Id".ljust(5, " "), "Name".ljust(15, " "), "Dob")
        for i in range(0, numOfStudents):
            print(
                str(students[i]["id"]).ljust(5, " "),
                students[i]["name"].ljust(15, " "),
                students[i]["Dob"],
            )
    # Show student marks for a given course
    elif choices == 3:
        for j in range(0, numOfCourses):
            print(courses[j]["name"])
            print("\tId".ljust(5, " "), "Name".ljust(15, " "), "Mark")
            for i in range(0, numOfStudents):
                print(
                    "\t",
                    str(students[i]["id"]).ljust(5, " "),
                    students[i]["name"].ljust(15, " "),
                    courses[j]["marks"][i][students[i]["name"]],
                )
    else:
        break
