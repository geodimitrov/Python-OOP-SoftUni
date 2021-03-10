from project.user import User

class Library:
    def __init__(self):
        self.user_records = []      # will contain user objects
        self.books_available = {}   # {author: [book1, book2, book3]
        self.rented_books = {}      # {usernames: {book name: days left}}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)


    def del_user_data(self, user):
        if user.books:
            self.rented_books.pop(self.rented_books[user.username])
        self.user_records.remove(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        return self.del_user_data(user)


    def invalid_user_id(self, user_id):
        for user in self.user_records:
            if user_id == user.user_id:
                return True
        return False

    def change_username(self, user_id, new_username):
        pass



# Test Code
user = User(12, 'Peter')
user2 = User(2, "Doro")
library = Library()
library.add_user(user)
library.add_user(user2)
print(library.add_user(user))
print(library.add_user(user2))
# print(library.change_username(4, 'Igor'))
# print(library.remove_user(user))