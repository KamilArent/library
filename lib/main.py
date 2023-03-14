import library
lib = library.Library()

#---------------------------------------MENU-----------------------------------#
#adding sample books and students
if __name__ == "__main__":
    lib.addSampleBooks()
    lib.addSampleStudents()
    x = ""
    while x !=  "0":
        print("1. Display students")
        print("2. Add student")
        print("3. Rent a book")
        print("4. Display avaiable books")
        print("5. Save to a file all students with books")
        print("6. Remove student")
        print("7. Remove book")
        print("8. Return a book")
        print("9. Add a book")
        print("0. End")
        x = input("Choice - ")
        print("*******")
        if x == "1":
            lib.displayStudents()
        elif x == "2":
            lib.addStudent()
        elif x =="3":
            lib.addBookToStudent()
        elif x == "4":
            lib.displayBooks()
        elif x == "5":
            lib.studentsWithBooks()
        elif x == "6":
            lib.removeStudent()
        elif x == "7":
            lib.removeBook()
        elif x == "8":
            lib.returnBook()
        elif x == "9":
            lib.addBooks()


        print("\n*******")