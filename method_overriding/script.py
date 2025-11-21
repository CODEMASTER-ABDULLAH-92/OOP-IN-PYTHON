# 👉 A child class defines a method with the same name as a method in the parent class,
# 👉 and changes (overrides) its behavior.
# So the child class “replaces” the parent’s method.

# ✅ Easy Example of Method Overriding

class Animal:
    def sound(self):
        print("Animals make some sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof Woof!")

# Creating objects
a = Animal()
d = Dog()

a.sound()   # Parent version
d.sound()   # Overridden version
