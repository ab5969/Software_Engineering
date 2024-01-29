class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def sort_employees(self, key):
        if key == 1:  # Sort by Age
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:  # Sort by Name
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:  # Sort by Salary
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid choice")

    def print_table(self):
        for employee in self.employees:
            print(employee)


def main():
    employees_data = [
        ("161E90", "Ramu", 35, 59000),
        ("171E22", "Tejas", 30, 82100),
        ("171G55", "Abhi", 25, 100000),
        ("152K46", "Jaya", 32, 85000),
    ]

    employees = [Employee(*data) for data in employees_data]
    employee_table = EmployeeTable(employees)

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    try:
        sorting_parameter = int(input("Enter your choice (1/2/3): "))
        employee_table.sort_employees(sorting_parameter)

        print("\nSorted Employee Table:")
        employee_table.print_table()
    except ValueError:
        print("Invalid input. Please enter a valid number (1/2/3).")


if __name__ == "__main__":
    main()
