# -----------------------------------------------------------
# 🟦 Encapsulation in Python
# -----------------------------------------------------------


# Imagine you have:
# 🎒 A school bag
# Inside the bag, there are pencils, books, lunch, etc.
# But…
# 👉 You don’t let everyone open your bag.
# 👉 Only you or someone you trust can open it.
# This is called encapsulation.
# You hide things inside a bag, and only allow access in controlled ways.

# Encapsulation means:
#   ➤ Keeping data + methods together inside a class
#   ➤ Controlling access to data using:
#       ✔ Public attributes
#       ✔ Protected attributes
#       ✔ Private attributes
# -----------------------------------------------------------

# -----------------------------------------------------------
# 🟦 2. Encapsulation in Python (Real Meaning)
# -----------------------------------------------------------

# Encapsulation = Hiding data + controlling access to it
# In Python, we do this using:
# ✔ Public attributes
# ✔ Protected attributes
# ✔ Private attributes
# -----------------------------------------------------------
# 🟩 3. Why Encapsulation Is Used? (Easy explanation)
# -----------------------------------------------------------


# We use encapsulation because:
# ✔ To protect data
# Example: You don’t want anyone to change your age to 200.
# ✔ To control how data is changed
# Example: You only change the password through secure functions.
# ✔ To keep code safe and clean
# Example: No direct access to sensitive values.
# ✔ To create cyber-secure software
# Example: Hide API keys, tokens, configurations, malware signatures.





# ===========================================================
# 1️⃣ PUBLIC ATTRIBUTES  (Everyone can access)
# ===========================================================
# - Defined normally: self.variable
# - Can be accessed inside & outside the class
# - No restrictions

class PublicExample:
    def __init__(self, amount):
        self.amount = amount    # PUBLIC attribute

# Creating object
p = PublicExample(1000)

print("Public Attribute:", p.amount)   # ✔ Allowed
# -----------------------------------------------------------



# ===========================================================
# 2️⃣ PROTECTED ATTRIBUTES (Convention: internal use only)
# ===========================================================
# - Defined with a single underscore: self._variable
# - Not strictly protected (Python does NOT enforce rules)
# - Intended for:
#       ✔ the class itself
#       ✔ child (sub) classes
# - Still accessible outside the class (BUT developers avoid it)

class ProtectedExample:
    def __init__(self, amount):
        self._amount = amount    # PROTECTED attribute

# Creating object
pro = ProtectedExample(2000)

print("Protected Attribute:", pro._amount)   # ✔ Works, but SHOULD NOT be used directly
# -----------------------------------------------------------



# ===========================================================
# 3️⃣ PRIVATE ATTRIBUTES (Hidden/Locked)
# ===========================================================
# - Defined using double underscore: self.__variable
# - Not accessible directly from outside
# - Python applies "name mangling":
#       self.__amount  → becomes  _ClassName__amount
# - Provides real encapsulation

class PrivateExample:
    def __init__(self, amount):
        self.__amount = amount    # PRIVATE attribute

# Creating object
pri = PrivateExample(3000)

# print(pri.__amount)  # ❌ ERROR → AttributeError

# Correct way to access (name mangling)
print("Private Attribute:", pri._PrivateExample__amount)   # ✔ Allowed using name-mangled name
# -----------------------------------------------------------



# ===========================================================
# 📝 SUMMARY (Important Notes)
# ===========================================================
# ✔ PUBLIC (no underscore)
#     - Free to access anywhere
#     - Example: self.amount
#
# ✔ PROTECTED (single underscore _)
#     - Should be treated as internal
#     - Accessible but not recommended from outside
#     - Example: self._amount
#
# ✔ PRIVATE (double underscore __)
#     - Partially hidden by name-mangling
#     - Example: self.__amount  → stored as _ClassName__amount
#
# ✔ Encapsulation helps:
#     - Protect internal data
#     - Prevent accidental modification
#     - Make code cleaner and safer
#
# ===========================================================

