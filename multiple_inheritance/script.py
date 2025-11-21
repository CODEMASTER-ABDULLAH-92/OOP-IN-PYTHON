"""
=========================================================
🔰 MULTIPLE INHERITANCE IN PYTHON
=========================================================

➡ Multiple Inheritance means a child class can inherit
   properties and methods from MORE THAN ONE parent class.

➡ Syntax:
        class Child(Parent1, Parent2):
            pass

➡ Python follows MRO (Method Resolution Order) to decide
   which parent method is called first when methods have
   the same name.

---------------------------------------------------------
📌 Example:
    class Father:
    class Mother:
    class Child(Father, Mother):

---------------------------------------------------------
Why use Multiple Inheritance?
---------------------------------------------------------
✔ To combine features of multiple parent classes  
✔ Used in real life:
      - A child gets surname from father  
      - Culture / habits from mother  

✔ Used in programming:
      - A class may need features from two different classes  
      - Example: A SmartPhone inherits from Phone + Camera

=========================================================
"""


# -------------------------------------------------------
# 👨 Father Class
# -------------------------------------------------------
class Father:
    def skills(self):
        return "Father Skills: Coding, Problem Solving"


# -------------------------------------------------------
# 👩 Mother Class
# -------------------------------------------------------
class Mother:
    def skills(self):
        return "Mother Skills: Cooking, Designing"


# -------------------------------------------------------
# 👦 Child Class (MULTIPLE INHERITANCE)
# -------------------------------------------------------
class Child(Father, Mother):
    """
    Child inherits from BOTH Father and Mother.
    This is MULTIPLE INHERITANCE.
    """

    def skills(self):
        """
        Method Overriding:
        Child overrides the `skills` method and
        still uses parent class methods by calling them
        directly.
        """
        father_skills = Father.skills(self)
        mother_skills = Mother.skills(self)

        return (
            father_skills
            + "\n"
            + mother_skills
            + "\nChild Skills: Sports, Gaming"
        )


# -------------------------------------------------------
# 🧪 TESTING THE MULTIPLE INHERITANCE
# -------------------------------------------------------
child = Child()
print(child.skills())


"""
=========================================================
📌 Notes: MRO (Method Resolution Order)
=========================================================

Python decides which parent class to check first
using the MRO rule:

For Child(Father, Mother):

    Child → Father → Mother → object

Check using:
    print(Child.mro())

=========================================================
📌 EXTRA: What If Both Parents Had Same Method Name?
=========================================================
Father and Mother both have skills().

Since Father is listed first:

    class Child(Father, Mother)

Python will call Father's skills() FIRST according to MRO.


"""
