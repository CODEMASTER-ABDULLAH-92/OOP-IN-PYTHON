"""
OOP Concept: COMPOSITION
-------------------------
Composition is a HAS-A relationship.
One class contains an object of another class.
Example: A Car HAS an Engine.

This allows the Car to use ALL methods & variables of Engine.
"""

# -----------------------------
# Engine Class (Component Class)
# -----------------------------
class Engine:
    """
    The Engine class represents a real engine.
    It has its own methods like start, accelerate, stop.
    """

    def start(self):
        print("Engine started")

    def accelerate(self):
        print("Engine accelerating...")

    def stop(self):
        print("Engine stopped")


# -----------------------------
# Car Class (Uses Composition)
# -----------------------------
class Car:
    """
    The Car class uses Composition.
    Car HAS an Engine → self.engine = Engine()

    Because of this, Car can call:
        self.engine.start()
        self.engine.accelerate()
        self.engine.stop()

    This shows the power of Composition.
    """

    def __init__(self):
        # COMPOSITION: Car contains an Engine object
        self.engine = Engine()

    def drive(self):
        print("Driving the car...")
        self.engine.start()        # Using Engine's method
        self.engine.accelerate()   # Using Engine's method
        print("Car is moving...")

    def park(self):
        print("Parking the car...")
        self.engine.stop()         # Using Engine's method
        print("Car parked.")


# -----------------------------
# Testing Composition
# -----------------------------
# if __name__ == "__main__":
car = Car()

print("\n--- DRIVE ---")
car.drive()
print("\n--- PARK ---")
car.park()
