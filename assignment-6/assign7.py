class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable (single underscore)
        self.__ssn = ssn          # Private variable (double underscore)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# Create an Employee object
emp = Employee("John Doe", 75000, "123-45-6789")

# Accessing the variables:
print("Public variable (name):", emp.name)        # Works fine

print("\nProtected variable (_salary):", emp._salary)  # Works but convention says don't

try:
    print("\nPrivate variable (__ssn):", emp.__ssn)    # Will raise AttributeError
except AttributeError as e:
    print("Error accessing private variable:", e)

# How to actually access private variables (name mangling):
print("\nAccessing private variable through name mangling:", emp._Employee__ssn)

# Displaying all info through class method:
print("\nDisplaying all info through class method:")
emp.display_info()










