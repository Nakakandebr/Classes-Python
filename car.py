# class Car:
#     max_speed = 240 # km/h
#     min_speed = 0 # km/h
#     acceleration_rate = 10 # km/h/s
#     deceleration_rate = 20 # km/h/s
    
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.current_speed = 0
    
#     def acceleration(self, time):
#         new_speed = self.current_speed + (self.acceleration_rate * time)
#         if new_speed <= self.max_speed:
#             self.current_speed = new_speed
#         else:
#             self.current_speed = self.max_speed
#         return f"The {self.color} {self.make} {self.model} accelerates to {self.current_speed} km/h in {time} seconds."
    
#     def deceleration(self, time):
#         new_speed = self.current_speed - (self.deceleration_rate * time)
#         if new_speed >= self.min_speed:
#             self.current_speed = new_speed
#         else:
#             self.current_speed = self.min_speed
#         return f"The {self.color} {self.make} {self.model} decelerates to {self.current_speed} km/h in {time} seconds."
    
#     def current_speed_info(self):
#         return f"The current speed of the {self.color} {self.make} {self.model} is {self.current_speed} km/h."
#         car1 = Car("Toyota", "Corolla", "Red")
# print(car1.acceleration(15)) # Output: The Red Toyota Corolla accelerates to 150 km/h in 15 seconds.

# print(car1.deceleration(7)) # Output: The Red Toyota Corolla decelerates to 10 km/h in 7 seconds.

# print(car1.current_speed_info()) # Output: The current speed of the Red Toyota Corolla is 10 km/h.
        
class Car:
    fuel_type = "Gasoline"
    
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def hook(self):
        return f" The {self.color} {self.make} {self.model} is hooting like pee pee "
    
    def drive(self):
        return f"The {self.color} {self.make} {self.model} is driving."
        
    def park(self):
        return f"The {self.color} {self.make} {self.model} is parked."
    
    



