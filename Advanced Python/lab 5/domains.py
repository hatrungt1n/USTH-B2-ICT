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
    def printStudentTxt(self):
        try:
            with open('./students.txt', 'a') as f:
                f.write((self.id).ljust(15, " ") + (self.name).ljust(20, " ") + (self.dob) + "\n")
        except FileNotFoundError:
            print("The 'docs' directory does not exist")
            
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

    @property
    def printCourseTxt(self):
        try:
            with open('./courses.txt', 'a') as f:
                f.write((self.id).ljust(15, " ") + self.name + "\n")
        except FileNotFoundError:
            print("The 'docs' directory does not exist")

    def printList(self, i):
        print(self.markList[i])