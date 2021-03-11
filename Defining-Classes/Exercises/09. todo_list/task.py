class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if not self.name == new_name:
            self.name = new_name
            return self.name
        return "Name cannot be the same."

    def change_due_date(self, new_date):
        if not self.due_date == new_date:
            self.due_date = new_date
            return self.due_date
        return "Date cannot be the same."

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number not in range(len(self.comments)):
            return "Cannot find comment."
        self.comments[comment_number] = new_comment
        return ", ".join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"

#Test code
# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())