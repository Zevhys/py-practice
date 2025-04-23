"""
! category: easy
TODO: Create a class named Coffee that represents coffee sales in a coffee shop. The class must have: A class attribute total_sold that keeps track of the total number of coffee cups sold, A class method named sell_cup() that increments total_sold by 1 each time it is called, Display the total coffee sales after selling a few cups.
"""


class Coffee:
    total_sold = 0

    @classmethod
    def sell_cup(cls):
        cls.total_sold += 1
        print(f"total sold: {cls.total_sold}")


cofee = Coffee()
cofee.sell_cup()
cofee.sell_cup()
cofee.sell_cup()

"""
! category: medium
TODO: Create a class named Employee to store employee data. This class should have: Instance attributes: name, position, and salary, An instance method display() to display the employee's information, A class method from_string() that accepts a string in the format "Name-Position-Salary" and returns it as a new instance of the Employee class.
"""


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = int(salary)

    def display(self):
        print(f"\nname: {self.name}\nposition: {self.position}\nsalary: {self.salary}")

    @classmethod
    def from_string(cls, emp_str):
        name, position, salary = emp_str.split("-")
        return cls(name, position, int(salary))


employee1 = Employee("nerf", "manager", 15000)
employee1.display()

employee2 = Employee.from_string("dwayne-addministration-20000")
employee2.display()
