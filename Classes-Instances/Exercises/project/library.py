from user import User

class Library:
    def __init__(self):
        self.user_records = []      # will contain user objects
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user: User):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user: User):
        if user not in self.user_records:
            return "We could not find such user to remove!"



# Test Code
user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))