class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        self.is_running = True
        return f"{self.brand} {self.model} is starting up!"
    
    def stop(self):
        self.is_running = False
        return f"{self.brand} {self.model} has stopped."
    
    def move(self):
        if self.is_running:
            return "Moving..."
        return "Start the vehicle first!"

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        self.gear = 'P'  # P for Park
    
    def change_gear(self, new_gear):
        self.gear = new_gear
        return f"Changed to {new_gear} gear"
    
    def move(self):
        if self.is_running:
            return f"{self.brand} {self.model} is driving on the road! 🚗"
        return "Start the car first!"

class Plane(Vehicle):
    def __init__(self, brand, model, year, max_altitude):
        super().__init__(brand, model, year)
        self.max_altitude = max_altitude
        self.current_altitude = 0
    
    def change_altitude(self, altitude):
        if altitude <= self.max_altitude:
            self.current_altitude = altitude
            return f"Flying at {altitude} feet"
        return "Altitude too high!"
    
    def move(self):
        if self.is_running:
            return f"{self.brand} {self.model} is flying through the air! ✈️"
        return "Start the plane first!"

# Testing the classes
if __name__ == "__main__":
    # Create a car
    my_car = Car("Toyota", "Camry", 2024, 4)
    print(my_car.start())
    print(my_car.change_gear("D"))
    print(my_car.move())
    print(my_car.stop())
    
    print("\n" + "="*50 + "\n")
    
    # Create a plane
    my_plane = Plane("Boeing", "747", 2023, 35000)
    print(my_plane.start())
    print(my_plane.change_altitude(30000))
    print(my_plane.move())
    print(my_plane.stop())