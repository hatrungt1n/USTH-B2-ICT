class student:
    def __init__(self, _id, _name, _dob):
        self.id = _id
        self.name = _name
        self.dob = _dob

    def getStudentName(self):
        return self.name

    def getNameAndId(self):
        print("\t", (self.id).ljust(15, " "), (self.name).ljust(20, " "), end="")

    @property
    def printList(self):
        print((self.id).ljust(15, " "), (self.name).ljust(20, " "), self.dob)


class course(student):
    def __init__(self, _id, _name, _studentList, _markList):
        self.id = _id
        self.name = _name
        self.studentList = _studentList
        self.markList = _markList

    @property
    def printCoursesList(self):
        print((self.id).ljust(15, " "), self.name)

    def getCourseName(self):
        return self.name

    def printList(self, i):
        print(self.markList[i])


class mark:
    def __init__(self, _mark):
        self.mark = _mark


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
    students.append(student(id, name, dob))

    i += 1

# Input number of courses
numOfCourses = int(input("How many courses are there ? \n"))

# Input course information: id, name
for j in range(0, numOfCourses):
    print(f"Course {j+1}'s informations: ")
    id = input("Id: ")
    name = input("Name: ")
    studentsList = students

    courses.append(course(id, name, studentsList, 0))

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
        _mark = int(input())
        marks.append(_mark)

        k += 1

    courses[courseSelection - 1].markList = marks[
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
        print("Id".ljust(15, " "), "Name")
        for j in range(0, numOfCourses):
            courses[j].printCoursesList

    # List students
    elif choices == 2:
        print("Id".ljust(15, " "), "Name".ljust(20, " "), "Dob")
        for i in range(0, numOfStudents):
            students[i].printList

    # Show student marks for a given course
    elif choices == 3:
        for j in range(0, numOfCourses):
            print(courses[j].getCourseName())
            print("\tId".ljust(15, " "), "Name".ljust(20, " "), "Mark")
            for i in range(0, numOfStudents):
                students[i].getNameAndId()
                courses[j].printList(i)

    else:
        break
