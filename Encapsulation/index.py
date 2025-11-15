# -----------------------------------------------------------
# 🟦 Encapsulation in Python
# -----------------------------------------------------------

# Imagine you have:
# 🎒 A school bag
# Inside the bag: pencils, books, lunch
# But…
# 👉 Not everyone is allowed to open it.
# 👉 Only you (or someone you trust) can open it.
# This is encapsulation.

# Encapsulation means:
#   ➤ Hiding data + controlling access to it
#   ➤ Using Public, Protected, Private variables & methods
# -----------------------------------------------------------


# -----------------------------------------------------------
# 🟩 Why Encapsulation Is Used?
# -----------------------------------------------------------
# ✔ To protect important/sensitive data
# ✔ To stop others from changing values directly
# ✔ To keep code clean and secure
# ✔ To use secure methods to update data
# ✔ Useful in cybersecurity (hide configs, keys, signatures)
# -----------------------------------------------------------



# ===========================================================
# 1️⃣ PUBLIC ATTRIBUTES  (Everyone can access)
# ===========================================================
class PublicExample:
    def __init__(self, amount):
        self.amount = amount    # PUBLIC attribute

p = PublicExample(1000)
print("Public Attribute:", p.amount)   # ✔ Allowed



# ===========================================================
# 2️⃣ PROTECTED ATTRIBUTES (Internal use only)
# ===========================================================
class ProtectedExample:
    def __init__(self, amount):
        self._amount = amount    # PROTECTED attribute

pro = ProtectedExample(2000)
print("Protected Attribute:", pro._amount)   # ✔ Allowed, but SHOULD NOT be used directly



# ===========================================================
# 3️⃣ PRIVATE ATTRIBUTES (Hidden - name mangling)
# ===========================================================
class PrivateExample:
    def __init__(self, amount):
        self.__amount = amount    # PRIVATE attribute

pri = PrivateExample(3000)

# print(pri.__amount)  # ❌ ERROR → private
print("Private Attribute:", pri._PrivateExample__amount)  # ✔ Name-mangled



# ===========================================================
# 🟦 Encapsulation With METHODS (Public, Protected, Private)
# ===========================================================

class Example:

    # ----------------------------
    # PUBLIC METHOD
    # ----------------------------
    # ✔ Anyone can access it
    def public_method(self):
        print("Public Method")

    # ----------------------------
    # PROTECTED METHOD
    # ----------------------------
    # ✔ Meant for internal or subclass use
    # ✔ Still accessible (not strictly protected)
    def _protected_method(self):
        print("Protected Method")

    # ----------------------------
    # PRIVATE METHOD
    # ----------------------------
    # ✔ Cannot be accessed directly from outside
    # ✔ Name-mangling applies
    def __private_method(self):
        print("Private Method")

    # ----------------------------
    # INTERNAL CALLER (Runs all)
    # ----------------------------
    def call_all(self):
        print("\nCalling All Methods Internally:")
        self.public_method()
        self._protected_method()
        self.__private_method()  # ✔ Allowed (inside class)


# Creating object
obj = Example()

# Calling methods
obj.public_method()        # ✔ Allowed

obj._protected_method()    # ✔ Technically allowed, but not recommended

obj.call_all()             # ✔ Works and even calls private method internally

# obj.__private_method()   # ❌ ERROR – private method is hidden
