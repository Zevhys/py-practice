"""
! Category: Easy
Todo: Create a class named Car that has default attributes: ‣brand: "Toyota", ‣color: "Black", ‣speed: 0. After that: 1. Create 1 object from this class and display all attributes using print(), 2. Change the color attribute of that object to "Red" and the speed to 100.
"""


class Car:
    def __init__(self):
        self.brand = "Toyota"
        self.color = "Black"
        self.speed = 0


car = Car()
car.color = "red"
car.speed = 100

print(f"name: {car.brand}\ncolor: {car.color}\nspeed: {car.speed}\n")

"""
! Category: Medium
Todo: Create a class named UserProfile with the following default attributes: ‣username (str): "guest", ‣email (str): "guest@example.com", ‣login_count (int): 0. Then: 1. Create a method display_info() that prints all the information of a UserProfile object, 2. Create an object user1 from the UserProfile class, and change its username to "rasyid123" and its email to "rasyid123@gmail.com", 3. Add a method increment_login() to increase the value of login_count each time the user logs in, 4. Call the increment_login() method 3 times for the user1 object, 5. Display the information of the user1 object using the display_info() method.
"""


class UserProfile:
    def __init__(self):
        self.username = "guest"
        self.email = "guest@example.com"
        self.login_count = 0

    def increment_login(self):
        self.login_count += 1
        print("total:", self.login_count)

    def display_info(self):
        print(f"\nusername: {self.username}\nemail: {self.email}")


user1 = UserProfile()
user1.username = "rasyid123"
user1.email = "rasyid123@gmail.com"
user1.increment_login()
user1.increment_login()
user1.increment_login()
user1.display_info()
