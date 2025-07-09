class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

class Manager(Employee):
    def __init__(self,name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()      
        print(f"Department: {self.department}")

dev = Developer("siva", "100000", "Python")
dev.display_info()
mgr = Manager("ram", "100000", "Sales")
mgr.display_info()

