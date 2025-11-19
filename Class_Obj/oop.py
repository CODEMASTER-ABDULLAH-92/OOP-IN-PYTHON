class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"

my_new_car = Car("Toyota","Corolla")
print(my_new_car.full_name())
        

class Dog:
    def __init__(self,name, breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def brak(self):
        print("Whoof Whoof")

class Owner:
    def __init__(self, name,address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

owner = Owner("hfh", "gffgfgf","489494-49994")
dog = Dog("Tommy", "Brcue 2", owner)
print(dog.owner.contact_number)



class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def greet(self):
        return print(f"My name is {self.name} and i am {self.age} years old.")

res = Person("Muhammad Abdullah", 22)
res.greet()

class User:
    def __init__(self,userName,email,password):
        self.userName = userName
        self.password = password
        self.email = email
    def say_hi_to_user(self, user):
        print(f"Sending message to {user.userName}: Hi {user.userName} its {self.userName}") 

user1 = User("abdullah", "abdullah@gmail.com","123")
user2 = User("Huzifa", "huzaifa@gmail.com","abc")

user1.say_hi_to_user(user2)

user1.email = "rajab@gmail.com" # we can modify the value