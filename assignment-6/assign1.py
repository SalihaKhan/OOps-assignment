# Define the Student class
class Student():
    # Constructor method to initialize object with name and marks
    def __init__(self, name, marks):
        # Public instance variable to store the student's name
        self.name = name
        # Public instance variable to store the student's marks
        self.marks = marks

    # Method to display the student's information
    def display(self):
        # Print the student's name and marks using formatted string
        print(f"The name is {self.name} and she got {self.marks} marks")

# Create an instance of the Student class with name "Saliha" and 90 marks
s = Student("Saliha", 90)

# Call the display method to show the student's details
s.display()
