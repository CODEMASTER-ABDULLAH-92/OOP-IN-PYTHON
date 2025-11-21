# 🐍 Python Programming Mastery - Ultimate Cheatsheet

![Python Logo](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-2.0-blue)
![License](https://img.shields.io/badge/License-MIT-green)

> 🚀 The most comprehensive Python cheatsheet on GitHub! Perfect for beginners to advanced developers.

## 📖 Table of Contents

- [🌟 Quick Start](#-quick-start)
- [📚 Fundamentals](#-fundamentals)
- [🏗️ Data Structures](#️-data-structures)
- [⚙️ Functions & Modules](#️-functions--modules)
- [🎭 OOP](#-object-oriented-programming)
- [🔧 Advanced Topics](#-advanced-topics)
- [📊 Popular Libraries](#-popular-libraries)
- [💡 Best Practices](#-best-practices)
- [🎯 Projects](#-projects)
- [🚀 Installation](#-installation)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)


---

## 📌 OOP Concepts Table

| Title | Code Link | Solution Link | Website Link |
|-------|-----------|---------------|--------------|
| Classes & Objects | [Code](https://example.com/code1) | [Solution](https://example.com/solution1) | [Website](https://example.com/site1) |
| Inheritance | [Code](https://example.com/code2) | [Solution](https://example.com/solution2) | [Website](https://example.com/site2) |
| Polymorphism | [Code](https://example.com/code3) | [Solution](https://example.com/solution3) | [Website](https://example.com/site3) |
| Encapsulation | [Code](https://example.com/code4) | [Solution](https://example.com/solution4) | [Website](https://example.com/site4) |
| Abstraction | [Code](https://example.com/code5) | [Solution](https://example.com/solution5) | [Website](https://example.com/site5) |

---

## 📌 OOP Questions Table

| Sr No. | Question | Code Link | Solution Link |
|--------|----------|-----------|---------------|
| 1 | Write a class for a calculator | [Link](https://example.com/q1code) | [Link](https://example.com/q1solution) |
| 2 | Demonstrate single inheritance | [Link](https://example.com/q2code) | [Link](https://example.com/q2solution) |
| 3 | Show polymorphism using methods | [Link](https://example.com/q3code) | [Link](https://example.com/q3solution) |
| 4 | Explain encapsulation with private variables | [Link](https://example.com/q4code) | [Link](https://example.com/q4solution) |
| 5 | Method Overriding in inheritance | [Link](https://example.com/q5code) | [Link](https://example.com/q5solution) |
| 6 | Create a Student class with attributes | [Link](https://example.com/q6code) | [Link](https://example.com/q6solution) |
| 7 | Demo constructor and destructor | [Link](https://example.com/q7code) | [Link](https://example.com/q7solution) |
| 8 | Create a bank account class | [Link](https://example.com/q8code) | [Link](https://example.com/q8solution) |
| 9 | Show operator overloading example | [Link](https://example.com/q9code) | [Link](https://example.com/q9solution) |
| 10 | Create an Animal base class | [Link](https://example.com/q10code) | [Link](https://example.com/q10solution) |

---
## 🌟 Quick Start

### Basic Python Example
```python
# Hello World in Python
print("Hello, World! 🌍")

# Variables and Data Types
name = "Alice"
age = 25
height = 5.6
is_student = True

# f-strings (Python 3.6+)
print(f"{name} is {age} years old and {height} feet tall")
```

### Run Your First Script
```bash
# Save as hello.py and run
python hello.py
# or
python3 hello.py
```

## 📚 Fundamentals

### 🔤 Variables & Data Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42` | Integer numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"hello"` | Text strings |
| `bool` | `True` | Boolean values |
| `list` | `[1, 2, 3]` | Mutable sequences |
| `tuple` | `(1, 2, 3)` | Immutable sequences |
| `dict` | `{"key": "value"}` | Key-value pairs |
| `set` | `{1, 2, 3}` | Unique collections |

### 🧮 Basic Operations

```python
# Arithmetic Operations
a, b = 10, 3
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3 (floor division)
print(a % b)    # 1 (modulus)
print(a ** b)   # 1000 (exponent)

# Comparison Operators
print(a > b)    # True
print(a == b)   # False
print(a != b)   # True

# Logical Operators
x, y = True, False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

### 🔤 String Manipulation

```python
text = "Python Programming"

# String Methods
print(text.upper())        # PYTHON PROGRAMMING
print(text.lower())        # python programming
print(text.title())        # Python Programming
print(text.replace("P", "J"))  # Jython Programming

# String Searching
print("Python" in text)    # True
print(text.find("Pro"))    # 7
print(text.startswith("Py")) # True

# String Formatting
name = "Alice"
age = 25
# f-string (recommended)
print(f"{name} is {age} years old")
# format method
print("{} is {} years old".format(name, age))
```

## 🏗️ Data Structures

### 📋 Lists

```python
# List Creation & Operations
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

# Adding Items
fruits.append("orange")          # Add to end
fruits.insert(1, "mango")       # Insert at index

# Removing Items
fruits.remove("banana")         # Remove specific item
popped = fruits.pop()           # Remove and return last item

# List Slicing
print(numbers[0])               # First item: 1
print(numbers[-1])              # Last item: 5
print(numbers[1:4])             # Slice: [2, 3, 4]
print(numbers[::2])             # Every 2nd: [1, 3, 5]

# List Comprehensions
squares = [x**2 for x in range(5)]           # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
```

### 📚 Dictionaries

```python
# Dictionary Creation
student = {
    "name": "John Doe",
    "age": 20,
    "grades": [85, 92, 78],
    "is_active": True
}

# Accessing Values
print(student["name"])                    # John Doe
print(student.get("age"))                 # 20
print(student.get("email", "Not provided")) # Safe access

# Modifying Dictionaries
student["email"] = "john@email.com"      # Add new key
student["age"] = 21                      # Update value
del student["is_active"]                 # Delete key

# Iterating
for key, value in student.items():
    print(f"{key}: {value}")
```

### 🎯 Sets & Tuples

```python
# Sets - Unique Collections
unique_numbers = {1, 2, 3, 3, 4, 4}  # {1, 2, 3, 4}
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union: {1, 2, 3, 4, 5, 6}
print(A & B)   # Intersection: {3, 4}
print(A - B)   # Difference: {1, 2}

# Tuples - Immutable
coordinates = (10, 20)
person = ("Alice", 25, "Engineer")
x, y = coordinates  # Tuple unpacking
```

## ⚙️ Functions & Modules

### 🎯 Function Basics

```python
# Basic Function
def greet(name):
    """Greets a person by name"""
    return f"Hello, {name}! 👋"

# Default Parameters
def create_profile(name, age=25, city="Unknown"):
    return {"name": name, "age": age, "city": city}

# Type Hints (Python 3.5+)
def calculate_area(length: float, width: float) -> float:
    return length * width

# Calling Functions
print(greet("Alice"))
profile = create_profile("Bob", city="New York")
```

### 🔄 Advanced Functions

```python
# Arbitrary Arguments
def print_args(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

print_args(1, 2, 3, name="Alice", age=25)

# Lambda Functions
square = lambda x: x ** 2
add = lambda a, b: a + b

# Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

### 📦 Modules

```python
# Importing Modules
import math
from datetime import datetime
import numpy as np

# Using Modules
print(math.sqrt(16))        # 4.0
print(datetime.now())       # Current datetime

# Creating Custom Modules
"""
# my_module.py
def hello():
    return "Hello from module!"
    
# main.py  
import my_module
print(my_module.hello())
"""
```

## 🎭 Object-Oriented Programming

### 🏗️ Classes & Objects

```python
class Dog:
    """A simple Dog class"""
    
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
        self.tricks = []
    
    def bark(self):
        return "Woof! 🐕"
    
    def learn_trick(self, trick):
        self.tricks.append(trick)
        return f"{self.name} learned {trick}! 🎉"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

# Creating Objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())           # Woof! 🐕
print(dog2.get_info())       # Max is 5 years old
```

### 🧬 Inheritance

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        raise NotImplementedError("Subclasses must implement this!")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Felis catus")
        self.breed = breed
    
    def speak(self):
        return "Meow! 😺"

class Lion(Cat):
    def __init__(self, name, pride_size):
        super().__init__(name, "Lion")
        self.pride_size = pride_size
    
    def speak(self):
        return "ROAR! 🦁"

# Polymorphism
animals = [Cat("Whiskers", "Siamese"), Lion("Simba", 5)]
for animal in animals:
    print(f"{animal.name}: {animal.speak()}")
```

### 🔒 Encapsulation

```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"✅ Deposited ${amount}"
        return "❌ Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"✅ Withdrew ${amount}"
        return "❌ Insufficient funds"
    
    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("Alice", 1000)
print(account.deposit(500))     # ✅ Deposited $500
print(account.get_balance())    # 1500
```

## 🔧 Advanced Topics

### 🐞 Exception Handling

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("❌ Please enter a valid number!")
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
else:
    print("✅ Operation successful!")
finally:
    print("🔚 This always executes")

# Custom Exceptions
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Required: ${amount}, Available: ${balance}")
```

### 📁 File Handling

```python
# Reading Files
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("❌ File not found!")

# Writing Files
with open("output.txt", "w") as file:
    file.write("Hello, World! 🌍\n")
    file.write("This is a new line.\n")

# Working with CSV
import csv
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
```

### 🔄 Generators

```python
# Generator Function
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Using Generator
print("Fibonacci sequence:")
for num in fibonacci(100):
    print(num, end=" ")

# Generator Expression
squares = (x**2 for x in range(10))
print(list(squares))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## 📊 Popular Libraries

### 🧮 NumPy

```python
import numpy as np

# Creating Arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))

# Array Operations
print(arr1 * 2)          # [2, 4, 6, 8, 10]
print(arr1 + arr1)       # [2, 4, 6, 8, 10]
print(np.dot(arr1, arr1)) # 55

# Statistics
print(f"Mean: {np.mean(arr1)}")      # 3.0
print(f"Median: {np.median(arr1)}")  # 3.0
```

### 🐼 Pandas

```python
import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}
df = pd.DataFrame(data)

# Data Operations
print(df.head())
print(f"Average Age: {df['Age'].mean()}")
print(f"Oldest: {df.loc[df['Age'].idxmax(), 'Name']}")

# Filtering
high_age = df[df['Age'] > 28]
print(high_age)
```

### 📈 Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
plt.title('Sine Wave Function 📈', fontsize=14)
plt.xlabel('X values')
plt.ylabel('sin(X)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
```

## 💡 Best Practices

### 🎯 Pythonic Code

```python
# ✅ Good - List Comprehension
squares = [x**2 for x in range(5)]

# ❌ Avoid - Traditional Loop
squares = []
for x in range(5):
    squares.append(x**2)

# ✅ Good - Proper Naming
class BankAccount:
    def calculate_interest(self):
        pass

# ❌ Avoid - Poor Naming
class bank_account:
    def calc_int(self):
        pass

# ✅ Good - Type Hints
def process_data(data: list) -> dict:
    return {"processed": True}
```

### ⚡ Performance Tips

```python
# Use generators for large datasets
def process_large_data():
    for i in range(1000000):
        yield i * 2

# Use sets for membership testing
large_set = set(range(1000000))
print(999999 in large_set)  # Very fast! ⚡

# Use local variables in loops
def efficient_loop():
    local_len = len  # Local reference
    items = list(range(1000))
    for i in items:
        pass  # Using local variable is faster
```

## 🎯 Projects

### 📞 Contact Management System

```python
class ContactManager:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone, email=""):
        self.contacts[name] = {'phone': phone, 'email': email}
        return f"✅ Contact '{name}' added!"
    
    def find_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            return f"📞 {name}: {contact['phone']}"
        return f"❌ Contact '{name}' not found!"
    
    def list_contacts(self):
        if not self.contacts:
            return "No contacts! 📭"
        result = "📒 Contacts:\n"
        for name, info in self.contacts.items():
            result += f"  👤 {name}: {info['phone']}\n"
        return result

# Usage
manager = ContactManager()
manager.add_contact("Alice", "123-4567")
print(manager.list_contacts())
```

### 🎮 Number Guessing Game

```python
import random

class NumberGame:
    def __init__(self, min_num=1, max_num=100):
        self.min = min_num
        self.max = max_num
        self.target = 0
        self.attempts = 0
    
    def start_game(self):
        self.target = random.randint(self.min, self.max)
        self.attempts = 0
        print(f"🎯 Guess between {self.min}-{self.max}!")
        self._play()
    
    def _play(self):
        while True:
            try:
                guess = int(input("🤔 Your guess: "))
                self.attempts += 1
                
                if guess < self.target:
                    print("📈 Too low!")
                elif guess > self.target:
                    print("📉 Too high!")
                else:
                    print(f"🎉 Correct! Attempts: {self.attempts}")
                    break
            except ValueError:
                print("❌ Enter a number!")

game = NumberGame()
game.start_game()
```

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Basic Setup
```bash
# Check Python version
python --version

# Install packages
pip install numpy pandas matplotlib

# Create virtual environment (recommended)
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### Popular Package Installation
```bash
# Data Science Stack
pip install numpy pandas matplotlib jupyter

# Web Development
pip install flask django requests

# Machine Learning
pip install scikit-learn tensorflow torch

# Testing
pip install pytest unittest
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### 🐛 Reporting Issues
- Use the GitHub Issues tab
- Provide clear description and steps to reproduce
- Include Python version and environment details

### 💡 Feature Requests
- Suggest new topics or improvements
- Provide use cases and examples
- Help implement new features

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Python Software Foundation
- Amazing open-source community
- Contributors and maintainers

## 📞 Support

If you have any questions or need help:

- 📧 **Email**: [infoabdullahdev92@gmail.com]
- 💬 **Discussions**: GitHub Discussions
- 🐛 **Issues**: GitHub Issues
- 📚 **Documentation**: [Python Official Docs](https://docs.python.org)

---

<div align="center">

### ⭐ Don't forget to star this repository if you found it helpful!

**Happy Coding! 🐍✨**

[![Python](https://img.shields.io/badge/Made_with-Python-blue?logo=python)](https://python.org)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)](CONTRIBUTING.md)
[![Stars](https://img.shields.io/github/stars/CODEMASTER-ABDULLAH-92/repository?style=social)](https://github.com/CODEMASTER-ABDULLAH-92/repository)

</div>
