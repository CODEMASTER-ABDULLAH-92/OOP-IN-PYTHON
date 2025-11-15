# 🐍 Python Inheritance = One Class Takes Things From Another Class
# There are:
# A Parent Class (also called Base class)
# A Child Class (also called Derived class)
# The child class automatically gets:
# ✔ Methods
# ✔ Variables
# ✔ Behavior
# …from the parent class.
# And the child can also add its own special things.


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{name} {age}")

    def addToNumbers(self, a, b):
        return a + b


class B(A):
    def __init__(self, name, age, roll_number):
        self.roll_number = roll_number

        # Call parent constructor correctly
        super().__init__(name, age)

        print(f"{name} {age} {roll_number}")

        # Correct way to call parent method
        result = self.addToNumbers(2, 5)
        print("Sum:", result)


# Creating object
c = B("MUHAMMAD Abdullah", 22, 234245)

