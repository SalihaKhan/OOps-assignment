class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calls Person's constructor
        self.subject = subject
        print(f"Teacher created: {self.name} teaches {self.subject}")

# Demonstration
teacher = Teacher("Ms. Smith", "Mathematics")