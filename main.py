import datetime


class Media:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Title: {self.title}"


class Book(Media):
    def __init__(self, title, authors, status='On Shelf', condition='Good'):
        super().__init__(title)
        self.authors = authors
        self.status = status
        self.condition = condition
        self.due_date = None

    def checkout(self):
        if self.status == "On Shelf":
            self.status = "Checked Out"
            self.due_date = datetime.datetime.now() + datetime.timedelta(weeks=2)
            return True
        else:
            return False

    def return_item(self):
        if self.status == "Checked Out":
            self.status = "On Shelf"
            self.due_date = None
            return True
        else:
            return False

    def degrade_condition(self, condition):
        conditions = ["Good", "Fair", "Poor", "Recycle"]
        if condition != "Recycle":
            current_index = conditions.index(condition)
            return conditions[current_index + 1]
        else:
            return condition

    def __str__(self):
        return f"Title: {self.title} by {', '.join(self.authors)}\nStatus: {self.status}\
                  \nCondition: {self.condition}\n"


class Movie(Media):
    def __init__(self, title, runtime, directors, status='On Shelf'):
        super().__init__(title)
        self.runtime = runtime
        self.directors = directors
        self.status = status
        self.due_date = None

    def checkout(self):
        if self.status == "On Shelf":
            self.status = "Checked Out"
            self.due_date = datetime.datetime.now() + datetime.timedelta(weeks=2)
            return True
        else:
            return False

    def return_item(self):
        if self.status == "Checked Out":
            self.status = "On Shelf"
            self.due_date = None
            return True
        else:
            return False

    def __str__(self):
        return f"Title: {self.title},\nRuntime: {self.runtime} minutes\
          \nDirector(s): {', '.join(self.directors)}\nStatus: {self.status}\n"


def display_media(catalog):
    # if catalog is None:
    #     print("No media found.")
    #     return

    for media in catalog:
        print(media)


def checkout_media(catalog):
    title = input("\nEnter title of the media to check out: ")
    selected = next((media for media in catalog if media.title.lower() == title.lower()), None)
    if selected:
        if selected.checkout():
            print(f"\nThank you for checking out {selected.title}. Please return by: {selected.due_date.strftime('%Y-%m-%d')}.")
        else:
            print(f"\nSorry, {selected.title} is already checked out.")
    else:
        print("\nMedia not found.")
    return catalog


def search_by_a_d(a_d, catalog):
    name = input("\nEnter " + a_d + "'s name: ")
    results = []
    if a_d == 'author':
        results = [media for media in catalog if
                   isinstance(media, Book) and name.lower() in ', '.join(media.authors).lower()]
    elif a_d == 'director':
        results = [media for media in catalog if
                   isinstance(media, Movie) and name.lower() in ', '.join(media.directors).lower()]
    if results:
        print("\nSearch Results:")
        display_media(results)
        continue_checking_out = input("\nWould you like to continue checking out? (y/n): ")
        if continue_checking_out == "y":
            checkout_media(catalog)
    else:
        print("\nNo books found.")
    return catalog


def search_by_title(catalog):
    keyword = input("\nEnter title keyword: ")
    results = [media for media in catalog if keyword.lower() in media.title.lower()]
    if results:
        print("\nSearch Results:")
        display_media(results)
        continue_checking_out = input("\nWould you like to continue checking out? (y/n): ")
        if continue_checking_out == "y":
            checkout_media(catalog)
    else:
        print("\nNo books found.")
    return catalog


def return_media(catalog, a_d):
    title = input("\nEnter the title of the media to return: ")
    selected = next((media for media in catalog if media.title.lower() == title.lower()), None)
    if selected.return_item():
        print(f"\nThank you for returning '{selected.title}'.")
        if a_d == "author":
            selected.condition = selected.degrade_condition(selected.condition)
            if selected.condition == 'Recycle':
                catalog.remove(selected)
        elif selected.condition == 'Recycle':
            catalog.remove(selected)
    else:
        print(f"\n{selected.title} was not checked out.")
        return catalog
    return catalog


def main_questions(catalog, a_d):
    print("\nCatalog:\n")
    display_media(catalog)
    choice = input("Would you like to continue to check out? (y/n): ")
    if choice.lower() == "y":
        option = input("What would you like to do?\n(a) Search by " + a_d + " \
                        \n(b) Search by title keyword\n(c) Check out media\
                        \n(d) Return media\n(e) Exit:\n")
        if option == "a":
            return search_by_a_d(a_d, catalog)
        elif option == "b":
            return search_by_title(catalog)
        elif option == "c":
            return checkout_media(catalog)
        elif option == "d":
            return return_media(catalog, a_d)
        elif option == "e":
            print("\nExiting...")
            return catalog
        else:
            print("\nInvalid option. Please try again.")
            return main_questions(catalog, a_d)
    elif choice.lower() == "n":
        print("\nExiting...")
        return catalog
    else:
        print("\nInvalid option. Please try again.")
        return main_questions(catalog, a_d)

# Create book and movie catalogs
book_catalog = [
    Book("The Great Gatsby", ["F. Scott Fitzgerald"]),
    Book("To Kill a Mockingbird", ["Harper Lee"]),
    Book("Go Set a Watchman", ["Harper Lee"]),
    Book("The Catcher in the Rye", ["J.D. Salinger"]),
    Book("The Hobbit", ["J.R.R. Tolkien"]),
    Book("Harry Potter and the Philosopher's Stone", ["J.K. Rowling"]),
    Book("Pride and Prejudice", ["Jane Austen"]),
    Book("The Lord of the Rings", ["J.R.R. Tolkien"]),
    Book("Animal Farm", ["George Orwell"]),
    Book("The Talisman", ["Stephen King", "Peter Straub"]),
    Book("The Da Vinci Code", ["Dan Brown"]),
    Book("Angels and Demons", ["Dan Brown"])
]

movie_catalog = [
    Movie("Inception", 148, ["Christopher Nolan"]),
    Movie("The Shawshank Redemption", 142, ["Frank Darabont"]),
    Movie("The Godfather", 175, ["Francis Ford Coppola"]),
    Movie("Pulp Fiction", 154, ["Quentin Tarantino"]),
    Movie("Forrest Gump", 142, ["Robert Zemeckis"]),
    Movie("The Dark Knight", 152, ["Christopher Nolan"]),
    Movie("The Matrix", 136, ["Lana Wachowski", "Lilly Wachowski"]),
    Movie("Interstellar", 169, ["Christopher Nolan"]),
    Movie("Fight Club", 139, ["David Fincher"]),
    Movie("The Fellowship of the Ring", 178, ["Peter Jackson"])
]


def main(book_catalog, movie_catalog):
    choice = input("\nWould you like to see the status of books or movies or quit? (b/m/q): ")
    if choice.lower() == "b":
        book_catalog = main_questions(book_catalog, 'author')
        main(book_catalog, movie_catalog)
    elif choice.lower() == "m":
        movie_catalog = main_questions(movie_catalog, 'director')
        main(book_catalog, movie_catalog)
    elif choice.lower() == "q":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please enter 'b' for books or 'm' for movies or 'q' to quit.")
        main(book_catalog, movie_catalog)


main(book_catalog, movie_catalog)
