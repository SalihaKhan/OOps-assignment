class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def get_info(self):
        return f"Employee {self.emp_id}: {self.name}"

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # Aggregation - stores Employee references
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def list_employees(self):
        print(f"Employees in {self.dept_name}:")
        for employee in self.employees:
            print(f"- {employee.get_info()}")

# Create independent Employee objects
emp1 = Employee("John Doe", "E1001")
emp2 = Employee("Jane Smith", "E1002")

# Create Department
hr_dept = Department("Human Resources")

# Add employees to department (aggregation)
hr_dept.add_employee(emp1)
hr_dept.add_employee(emp2)

# List department employees
hr_dept.list_employees()

# Employees continue to exist independently
print("\nEmployee working independently:")
print(emp1.get_info())