class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

dev = Developer("Alice", 30, 80000, "Python")
dev.display_info()