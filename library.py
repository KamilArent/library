class Student:
    
    #defining student#
    studentID = -1
    def __init__(self,foreName, name):
        self.foreName = foreName
        self.name = name
        self.books = []
        Student.studentID += 1
        self.studentID = Student.studentID

    #defining how student shall be printed#
    def formatkaStudent(s):
        print("\nFore Name: " + s.foreName)
        print("Name: " + s.name)
        print("studentID: " + str(s.studentID))
        print("Books: ", end="")
        for book in s.books:
            print(book.title, end=", ")
        print("")
        
    #function that converts student info to a string#
    def StudentToString(s):
        studentString = '"Forename: ' + s.foreName + ", Name: " + s.name + ", ID: " + str(s.studentID) + ", Books: ["
        for book in s.books:
            studentString += book.title + ", "
        if studentString[-1:] == " ":
            studentString = studentString[:-2]
        studentString += ']"\n'
        return studentString
        

class Library:
    studentList = []

    def addStudent():
        
        #adding some students for testing#
        """
        student1 = Student("Kamil", "Kot")
        student2 = Student("Kuba", "Siwiec")
        student3 = Student("Natalia", "Kot")
        student4 = Student("Riley", "Hej")
        student5 = Student("Stefan", "Kowalski")
        Library.studentList.append(student1)
        Library.studentList.append(student2)
        Library.studentList.append(student3)
        Library.studentList.append(student4)
        Library.studentList.append(student5)
        """
        
        #adding a student via console#
        nazwisko = input("Podaj nazwisko studenta: ")
        imie = input("Podaj imię studenta: ")
        student = Student(nazwisko, imie)
        Library.studentList.append(student)
        
    
    #displaying all students#
    def displayStudents():
        for s in Library.studentList:
            Student.formatkaStudent(s)


    #function that signs a book to a student#
    def addBookToStudent():
        sID = int(input("Podaj ID studenta: "))
        title = input("Podaj tytuł książki: ")
        for student in Library.studentList:
            if student.studentID == sID:
                for book in Books.listBooks:
                    if title.lower() == book.title.lower() and Books.listBooks[book] > 0:
                        student.books.append(book)
                        Books.listBooks[book] -= 1
                        
    #function that displays all students that have a book signed to them#
    def studentsWithBooks():
        file_name  = "StudentWithBooks.txt"
        f = open(file_name, "w+")
        for student in Library.studentList:
            if len(student.books) > 0:
                #alternative to display in console students that have at least one book#
                #Student.formatkaStudent(student)#
                st = Student.StudentToString(student)
                f.write(st)
        print("done")
        f.close()
                

class Books:
    listBooks = {}

    #defining book#
    def __init__(self, author, title, year, category):
        self.author = author
        self.title = title
        self.year = year
        self.category = category


    #function that adds a book to library#
    def addBooks():
        #adding books for testing#
        """
        book1 = Books("Suzanne Collins", "The Hunger Games", 2008, "Fiction")
        book2 = Books("J.K. Rowling", "Harry Potter and the Order of the Phoenix", 2003, "Fantasy")
        book3 = Books("Jane Austenn, Anna Quindlen", "Pride and Prejudice", 1813, "Classics")
        book4 = Books("Harper Lee", "To Kill a Mockingbird", 1960, "Classics")
        book5 = Books("Markus Zusak", "The Book Thief", 2006, "Historical Fiction")
        Books.listBooks[book1] = 1
        Books.listBooks[book2] = 1
        Books.listBooks[book3] = 1
        Books.listBooks[book4] = 1
        Books.listBooks[book5] = 1
        Books.listBooks[book1] = 2
        """
        
        #adding book from user via console#
        name = input('Podaj tytuł książki: ')
        author = input('Podaj autora książi: ')
        year = input('Podaj rok publikacji')
        ilosc = int(input('Podaj ile książek chciałbyś dodać do biblioteki: '))
        category = input("Wpisz kategorię książki: ")
        for book in Books.listBooks:
            if name == book.title:
                Books.listBooks[book] += ilosc
                return True
        book = Books(author, name, year, category)
        Books.listBooks[book] = ilosc
        
         
         
    #function that display all books avaiable in the library#
    def displayBooks():
        for book in Books.listBooks:
            if  Books.listBooks[book] > 0: 
                print("title: ", book.title +" by " + book.author + " - Ilość: ", Books.listBooks[book])



#---------------------------------------MENU-----------------------------------#
Books.addBooks()
x = ""
while x !=  "0":    
    print("1. Display students")
    print("2. Add student")
    print("3. Rent a book")
    print("4. Display avaiable books")
    print("5. Save to a file all students with books") 
    print("0. End")
    x = input("Wpisz swój wybór: ")
    print("*******")
    if x == "1":
        Library.displayStudents()
    elif x == "2":
        Library.addStudent()
    elif x =="3":
        Library.addBookToStudent()
    elif x == "4":
        Books.displayBooks()
    elif x == "5":
        Library.studentsWithBooks()

    print("\n*******")