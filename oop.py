class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"

# Inheritance 
class ElecticCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
new_t = ElecticCar("Tesla", "Model T", "84")
print(new_t.full_name())

# my_new_car = Car("Toyota","Corolla")
# print(my_new_car.full_name())
        