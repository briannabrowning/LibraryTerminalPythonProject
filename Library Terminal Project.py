class Book():
    total_books = 0
    books_checked_out = 0

    def __init__(self, title, author, checked_out=False, good_condition=True):
        self.title = title
        self.author = author
        self.checked_out = checked_out
        self.good_condition = good_condition
        Book.total_books += 1

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            Book.books_checked_out += 1
            return f"{self.title} by {self.author} has been checked out."
        else:
            return f"{self.title} by {self.author} is already checked out."

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            Book.books_checked_out -= 1
            return f"{self.title} by {self.author} has been checked in."
        else:
            return f"{self.title} by {self.author} is already checked in."

    def book_condition(self):
        if self.good_condition:
            return f"{self.title} by {self.author} is in good condition."
        else:
            return f"{self.title} by {self.author} is in bad condition. Please discard."

    def __str__(self):
        if self.checked_out:
            return f'{self.title} by {self.author} is checked out.'
        else:
            return f'{self.title} by {self.author} is available.'


books_list = [
    Book("The Great Gatsby", "F. Scott Fitzgerald"),
    Book("To Kill a Mockingbird", "Harper Lee"),
    Book("1984", "George Orwell"),
    Book("The Catcher in the Rye", "J.D. Salinger"),
    Book("The Hobbit", "J.R.R. Tolkien"),
    Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling"),
    Book("Pride and Prejudice", "Jane Austen"),
    Book("The Lord of the Rings", "J.R.R. Tolkien"),
    Book("Animal Farm", "George Orwell"),
    Book("The Chronicles of Narnia", "C.S. Lewis"),
    Book("The Da Vinci Code", "Dan Brown"),
    Book("The Alchemist", "Paulo Coelho")
]

for book in books_list:
    print(book)
