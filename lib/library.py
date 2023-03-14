import student as Student
import books as Books

class Library:
    studentList = []

    def addSampleStudents(self):
        #adding some students for testing#
        student1 = Student.Student("Kamil", "Arent")
        student2 = Student.Student("Kuba", "Ulrych")
        student3 = Student.Student("Pascal", "Kot")
        student4 = Student.Student("Szymon", "Kowalski")
        student5 = Student.Student("Jan", "Kowalski")
        Library.studentList.append(student1)
        Library.studentList.append(student2)
        Library.studentList.append(student3)
        Library.studentList.append(student4)
        Library.studentList.append(student5)
        print("Loaded students")

    def addSampleBooks(self):
        #adding books for testing#
        book1 = Books.Books("Suzanne Collins", "The Hunger Games", 2008, "Fiction")
        book2 = Books.Books("J.K. Rowling", "Harry Potter and the Order of the Phoenix", 2003, "Fantasy")
        book3 = Books.Books("Jane Austenn, Anna Quindlen", "Pride and Prejudice", 1813, "Classics")
        book4 = Books.Books("Harper Lee", "To Kill a Mockingbird", 1960, "Classics")
        book5 = Books.Books("Markus Zusak", "The Book Thief", 2006, "Historical Fiction")
        Books.Books.listBooks[book1] = 1
        Books.Books.listBooks[book2] = 3
        Books.Books.listBooks[book3] = 1
        Books.Books.listBooks[book4] = 5
        Books.Books.listBooks[book5] = 3
        Books.Books.listBooks[book1] = 2
        print("Loaded books")
    
    
    def addStudent(self):
        #adding a student via console#
        nazwisko = input("Students last name: ")
        imie = input("Students first name: ")
        student = Student.Student(nazwisko, imie)
        Library.studentList.append(student)
        print("Success")

    # function that adds a book to library#
    def addBooks(self):
        #adding book from user via console#
        name = input('Book title: ')
        ilosc = int(input('Quantity: '))
        for book in Books.Books.listBooks:
            if name.lower() == book.title.lower():
                Books.Books.listBooks[book] += ilosc
                print("Amount of " + name + " has increased")
                return
        author = input('Author: ')
        year = input('Date of publishing: ')
        category = input("Category: ")
        book = Books.Books(author, name, year, category)
        Books.Books.listBooks[book] = ilosc
        print("added book")
    
    #displaying all students#
    def displayStudents(self):
        for s in Library.studentList:
            Student.Student.formatkaStudent(s)


    #function that signs a book to a student#
    def addBookToStudent(self):
        sID = int(input("Students ID: "))
        title = input("Book title: ")
        for student in Library.studentList:
            if student.studentID == sID:
                for book in Books.Books.listBooks:
                    if title.lower() == book.title.lower() and Books.Books.listBooks[book] > 0:
                        student.books.append(book)
                        Books.Books.listBooks[book] -= 1
                        print("Book has been added")
                        return
                    else:
                        print("We dont have '" + title + "' at the moment")
                        return
        print("fail")
                        
    #function that displays all students that have a book signed to them#
    def studentsWithBooks(self):
        f = open("StudentsWithBooks.txt", "w+")
        #with open("StudentsWithBooks.txt", "w+") as f:
        if f:
            for student in Library.studentList:
                if len(student.books) > 0:
                    #alternative to display in console students that have at least one book#
                    #Student.formatkaStudent(student)#
                    st = Student.Student.StudentToString(student)
                    f.write(st)
            print("done")
            f.close()
        else:
            print("Failed to open file")
                
    #function that display all books avaiable in the library#
    def displayBooks(self):
        for book in Books.Books.listBooks:
            if  Books.Books.listBooks[book] > 0:
                Books.Books.formBook(book)

    def removeStudent(self):
        a = input("Write students ID: ")
        a = int(a)
        for student in Library.studentList:
            if student.studentID == a:
                Library.studentList.remove(student)
                print("Student has been removed")
                return
        print("Fail")

    def removeBook(self):
        a = input("Write title of the book that you would like to remove: ")
        a = a.lower()
        for book in Books.Books.listBooks:
            if a == book.title.lower():
                Books.Books.listBooks.pop(book)
                print("Success")
                return
        print("There is no such book")

    def returnBook(self):
        studentid = input("Students id: ")
        booktitle = input("Books title: ")
        studentid = int(studentid)
        for student in Library.studentList:
            #if student.studentID == studentid and booktitle.lower() in [b.title.lower() for b in student.books]:
            if student.studentID == studentid:
                for b in student.books:
                    if booktitle.lower() == b.title.lower():
                        ind = student.books.index(b)
                        student.books.pop(ind)
                        Books.Books.listBooks[b] += 1
                        print("Success")
                        return
                return
                print(studentid, " doesn't have " + booktitle)
        print("There's no student with id ", studentid)

