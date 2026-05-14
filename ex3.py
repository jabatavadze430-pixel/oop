class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print("User profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print()

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back 👋")
        print()


user1 = User("jaba", "tavadze", 20, "jaba@gmail.com", "Batumi")
user2 = User("lado", "tavadze", 25, "lado@yahoo.com", "Tbilisi")
user3 = User("tengo", "tavadze", 18, "tengo@mail.com", "Kutaisi")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()