from project.user import User


class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}  # {author: [books available]}
        self.rented_books: dict[str, dict[str, int]] = {}  # {username: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        for username, books in self.rented_books.items():
            if book_name in books:
                return (
                    f'The book "{book_name}" is already rented and '
                    f'will be available in {books[book_name]} days!'
                )

        if author in self.books_available and \
                book_name in self.books_available[author]:

            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}

            self.rented_books[user.username][book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)

        if user.username in self.rented_books:
            self.rented_books[user.username].pop(book_name, None)

        if author not in self.books_available:
            self.books_available[author] = []

        self.books_available[author].append(book_name)

        return None
