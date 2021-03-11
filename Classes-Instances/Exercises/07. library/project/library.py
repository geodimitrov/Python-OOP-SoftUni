from user import User

class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {} # {author: [book1, book2, ...]}
        self.rented_books = {}  # {username: {bookname: days_to_return}}

    def get_user_obj(self, user_id):
        user_obj = [user for user in self.user_records if user.user_id == user_id]
        if user_obj:
            return user_obj[0]
        return None

    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user):
        if user in self.user_records:
            self.rented_books.pop(user.username)
            self.user_records.remove(user)
        return "We could not find such user to remove!"

    def change_username(self, user_id, new_username):
        user = self.get_user_obj(user_id)
        if not user:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return "Please check again the provided username -\
it should be different than the username used so far!"
        if user.username in self.rented_books:
            self.rented_books[new_username] = self.rented_books.pop(user.username)
        user.username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"

user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))
library.remove_user(user)
print(library.remove_user(user))
library.add_user(user)
print(library.change_username(2, 'Igor'))
print(library.change_username(12, 'Peter'))
print(library.change_username(12, 'George'))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})


user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
print(library.books_available)
print(library.rented_books)
print(user.books)
