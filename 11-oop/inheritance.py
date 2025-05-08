"""
! Category: Easy
Todo: Create two classes: 1. Person with the following attributes: ‣name, ‣age, ‣A method greet() that prints a greeting with the person's name and age, 2. Student as a subclass of Person, with an additional attribute: ‣major, ‣A method introduce() that prints complete information (name, age, and major).
"""


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hello your name and age is {self.name}-{self.age}\n")


class Student(Person):
    def __init__(self, name, age, major: str):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        print(f"name: {self.name}\nage: {self.age}\nmajor: {self.major}\n")


student1 = Student("rasha", 20, "science")
student1.greet()
student1.introduce()

"""
! Category: Medium
Todo: Create the following three classes: 1. Parent class named Employee with the following attributes: ‣name, ‣salary, ‣A method get_info() that prints the name and salary. 2. Subclass named Manager that inherits from Employee, with an additional attribute: ‣department, ‣Override the get_info() method to include department information. 3. Subclass named Intern that also inherits from Employee, with an additional attribute: ‣duration_months, ‣Override the get_info() method to display the internship duration.
"""


class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"name: {self.name}\nsalary: {self.salary}\n"


class Manager(Employee):
    def __init__(self, name, salary, department: str):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        return (
            f"name: {self.name}\nsalary: {self.salary}\ndepartment: {self.department}\n"
        )


class Intern(Employee):
    def __init__(self, name, salary, duration_months: int):
        super().__init__(name, salary)
        self.duration_months = duration_months

    def get_info(self):
        return f"name: {self.name}\nsalary: {self.salary}\ninternship duration: {self.duration_months} months"


employee1 = Employee("jannah", 3000)
print(employee1.get_info())

manager1 = Manager("rosky", 5000, "IT")
print(manager1.get_info())

intern1 = Intern("rusty", 1000, 6)
print(intern1.get_info())
