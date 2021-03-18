class Library:
    def __init__(self):
        self.user_records = []     # will store User objects
        self.books_available = {}  # author: [book1, book2...]
        self.rented_books = {}     # username: {book_name: days_to_return}

    @staticmethod
    def get_user_obj(user_id, user_records):
        user_obj = [user for user in user_records if user.user_id == user_id]
        if user_obj:
            return user_obj[0]

    def remove_rented_books(self, user):
        if user.username in self.rented_books:
            self.rented_books.pop(user.username)

    def has_rented_books(self, current_username, new_username):
        if current_username in self.rented_books:
            self.rented_books[new_username] = self.rented_books.pop(current_username)

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.remove_rented_books(user)
        self.user_records.remove(user)

    def change_username(self, user_id, new_username):
        user = self.get_user_obj(user_id, self.user_records)
        if user and not user.username == new_username:
            self.has_rented_books(user.username, new_username)
            user.username = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"

        if user and user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"