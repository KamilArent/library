class Books:
    listBooks = {}

    #defining book#
    def __init__(self, author, title, year, category):
        self.author = author
        self.title = title
        self.year = year
        self.category = category

    def formBook(self):
        print("title: " + self.title, end="")
        print(" by " + self.author, end="")
        print(" - Quantity: ", Books.listBooks[self])
