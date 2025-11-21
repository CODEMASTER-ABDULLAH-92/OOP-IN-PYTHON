
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

class BankAccount:
    def __init__(self, amount):
        self.__balance = amount   # use constructor amount
        print("Initial Balance:", self.__balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.__balance += amount
        print("After Deposit:", self.__balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive!")
            return

        if amount > self.__balance:
            print("Insufficient balance!")
            return

        self.__balance -= amount
        print("After Withdraw:", self.__balance)


ba = BankAccount(1000)
ba.deposit(1000)
ba.withdraw(1000)

