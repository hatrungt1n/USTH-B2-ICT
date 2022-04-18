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