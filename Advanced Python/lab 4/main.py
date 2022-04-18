import input
import numpy as np

def listCourses():
    print("Id".ljust(15, " "), "Name")
    for j in range(0, input.numOfCourses):
        input.courses[j].printCoursesList


def listStudents():
    print("Id".ljust(15, " "), "Name".ljust(20, " "), "Dob")
    for i in range(0, input.numOfStudents):
        input.students[i].printList


def showMarks():
    for j in range(0, input.numOfCourses):
        print(input.courses[j].getCourseName())
        print("\tId".ljust(15, " "), "Name".ljust(20, " "), "Mark")
        for i in range(0, input.numOfStudents):
            input.students[i].getNameAndId()
            input.courses[j].printList(i)


def showAverageMarks():
    print("Average mark: ")
    input.marksLength = len(input.marks)
    averageMarks = []
    for i in range(0, input.numOfStudents):
        averageMark = np.average(input.marks[i:input.marksLength:input.numOfStudents])
        averageMarks.append(averageMark)
    print(sorted(averageMarks, reverse=True))