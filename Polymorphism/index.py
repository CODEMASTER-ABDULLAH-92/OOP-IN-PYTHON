"""
====================================================
🐾 POLYMORPHISM IN PYTHON
====================================================

Polymorphism = "Many Forms"
It allows the same method or function to behave differently
depending on the object it is applied to.

This file explains polymorphism step by step with examples,
comments, and notes.
====================================================
"""

# ---------------------------------------------------
# Example 1: Real-life example
# ---------------------------------------------------

# Different animals make different sounds
# Same action: "Make sound!" --> Different result

# Cat -> Meows
# Dog -> Barks
# Cow -> Moos

print("Example 1: Everyday Life")
print("Make sound!")
print("- Cat: Meow")
print("- Dog: Woof")
print("- Cow: Moo")

# ✅ This shows that the same command can produce
# different results depending on the object.


# ---------------------------------------------------
# Example 2: Python Classes
# ---------------------------------------------------

class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

# List of animal objects
animals = [Cat(), Dog()]

print("\nExample 2: Python Code")
for animal in animals:
    # Same method call, different output depending on object
    print(animal.sound())

# ---------------------------------------------------
# Notes on Output:
# ---------------------------------------------------
# Meow
# Woof
# This demonstrates polymorphism: same method name,
# different behavior depending on the object.


# ---------------------------------------------------
# Types of Polymorphism in Python
# ---------------------------------------------------

# 1️⃣ Compile-time / Method Overloading
# Python does not support strict overloading, but it can be simulated using default arguments.

# 2️⃣ Run-time / Method Overriding
# Most common in Python. Child class overrides parent method.

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog2(Animal):
    def sound(self):  # overrides Animal.sound()
        return "Woof Woof"

# Polymorphism via method overriding
animal = Animal()
dog = Dog2()
print("\nExample 3: Method Overriding")
print(animal.sound())  # Some generic sound
print(dog.sound())     # Woof Woof

# ---------------------------------------------------
# Key Idea:
# ---------------------------------------------------
# Polymorphism allows you to write flexible code.
# You can call the same method on different objects,
# and Python automatically chooses the correct behavior.

# Example of flexibility
print("\nExample 4: Flexible Code")
for obj in [Cat(), Dog(), Dog2()]:
    print(obj.sound())