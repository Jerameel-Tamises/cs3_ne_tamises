class Starships:
    def __init__(self, weight, cargo_weight, fuel_capacity):
        self.weight = weight
        self.cargo_weight = cargo_weight
        self.fuel_capacity = fuel_capacity

    def calculate_fuel(self):
        total_weight = 50000
        fuel_needed = 1000
        self.final_fuel = (self.weight + self.cargo_weight) 

        return self.final_fuel

    starship1 = Starships(50000, 1000, 0)
    starship1.cargo_weight()
    
