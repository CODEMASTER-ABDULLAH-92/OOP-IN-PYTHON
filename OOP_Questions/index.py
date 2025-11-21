
# 1. Write a Python class `Car` with attributes (brand, model) and a method to display full details.

# class Car:
#     def __init__(self, brand,model):
#         self.brand = brand
#         self.model = model
#     def displayDetails(self):
#         return print(f"{self.brand} {self.model}")

# car = Car("Toyota", "V8")
# car.displayDetails()



# 2. Create a class `Student` that takes name and marks, and print grade based on marks.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def gettingMarks(self):
#         if self.marks >= 90:
#             print("A")
#         elif self.marks >= 80:
#             print("B")
#         elif self.marks >= 70:
#             print("C")
#         elif self.marks >= 60:
#             print("D")
#         else:
#             print("E")


# student = Student("Muhammad Abdullah", 89)
# student.gettingMarks()




# 3. Write a program to implement inheritance between `Animal` and `Dog` classes.

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Dog(Animal):
#     def __init__(self, name, age, category):
#         super().__init__(name, age)
#         self.category = category

#     def details(self):
#         print(f"{self.category} {self.name} {self.age}")

# dog = Dog("Tommy", "5 months", "German Shepherd")
# dog.details()


# 4. Create a class `BankAccount` with deposit and withdraw methods, maintaining balance.

# class BankAccount:
#     def __init__(self, amount):
#         self.__balance = amount   # use constructor amount
#         print("Initial Balance:", self.__balance)

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit amount must be positive!")
#             return
#         self.__balance += amount
#         print("After Deposit:", self.__balance)

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdraw amount must be positive!")
#             return

#         if amount > self.__balance:
#             print("Insufficient balance!")
#             return

#         self.__balance -= amount
#         print("After Withdraw:", self.__balance)


# ba = BankAccount(1000)
# ba.deposit(1000)
# ba.withdraw(1000)



# 5. Write Python code to demonstrate method overriding in inheritance.

# class Animal:
#     def sound(self):
#         print("Animal make some sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog bark: woof woof!")

# animal = Animal()
# dog = Dog()

# animal.sound()
# dog.sound()


# 6. Implement multiple inheritance using two parent classes `Father` and `Mother`.

# class Father:
#     def skills(self):
#         return "Coding, Problem Solving"

# class Mother:
#     def skills(self):
#         return "Cooking Only , Time Wasting "

# class Child(Father, Mother):
#     def skills(self):
#         return Father.skills(self) + Mother.skills(self) + "Web Dev" + "PYTHON DEV"


# c = Child()
# print(c.skills())





# 7. Write a program using `super()` to access parent class constructor.

# class Teacher:
#     def __init__(self, work):
#         self.work = work

#     def working(self):
#         print(f"{self.work}")


# class Student(Teacher):
#     def __init__(self, work, hobby):
#         super().__init__(work)
#         self.hobby = hobby

#     def working(self):
#         print(f"Working: {self.work} \nHobby: {self.hobby}")


# s = Student("Studying", "Playing Cricket")
# s.working()



# 9. Implement polymorphism: create two classes `Cat` and `Dog` with a `sound()` method.

# class Cat:
#         def sound(self):
#             return print("Cat Speaking: Meow Meow")

# class Dog:
#     def sound(self):
#         return print("Dog Speaking: Boew Boew")

# animals = [Cat(), Dog()]

# for animal in animals:
#     animal.sound()
    

# 16. Write a program that uses encapsulation with private variables and getters/setters.
# class Human:
#     def __init__(self, name,age):
#         self.__name = name
#         self.__age = age
#     def gettingInfo(self):
#         return self.__name, self.__age
    
#     def settingInfo(self, name,age):
#         self.__name = name
#         self.__age = age
        
#     def showInfo(self):
#         return print(f"Name: {self.__name}\nAge: {self.__age}")

# h = Human("Abdullah", 22)
# h.gettingInfo()
# h.settingInfo("Rajab",20)
# h.showInfo()    



# 17. Demonstrate composition by creating a `Laptop` class containing a `Battery` object.

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity   # in mAh

    def show_battery(self):
        return f"Battery Capacity: {self.capacity}mAh"


class Laptop:
    def __init__(self, brand, battery_capacity):
        self.brand = brand
        
        # Composition: Laptop HAS a Battery
        self.battery = Battery(battery_capacity)

    def laptopInfo(self):
        return f"Laptop Brand: {self.brand}\n{self.battery.show_battery()}"


lap = Laptop("Dell", 6000)
print(lap.laptopInfo())

         