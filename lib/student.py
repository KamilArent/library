class Student:
    # defining student#
    studentID = -1

    def __init__(self, forename, name):
        self.foreName = forename
        self.name = name
        self.books = []
        Student.studentID += 1
        self.studentID = Student.studentID

    # defining how student shall be printed#
    def formatkaStudent(self):
        print("\nFore Name: " + self.foreName)
        print("Name: " + self.name)
        print("studentID: " + str(self.studentID))
        print("Books: ", end="")
        for book in self.books:
            print(book.title, end=", ")
        print("")

    # function that converts student info to a string#
    def StudentToString(self):
        studentString = '"Forename: ' + self.foreName + ", Name: " + self.name + ", ID: " + str(self.studentID) + ", Books: ["
        for book in self.books:
            studentString += book.title + ", "
        if studentString[-1:] == " ":
            studentString = studentString[:-2]
        studentString += ']"\n'
        return studentString
