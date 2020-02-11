

class Aircraft:
    def __init__(self, capacity, size_of_fuel_tank, taken = 'no'):
        self.capacity = capacity
        self.size_of_fuel_tank = size_of_fuel_tank
        self.taken = taken


class Plane(Aircraft):
    def __init__(self, capacity, size_of_fuel_tank, plane_number,taken = 'no' ):
        super().__init__(capacity,size_of_fuel_tank, taken)
        self.plane_number = plane_number





class Heliecopter(Aircraft):
    def __init__(self,capacity, size_of_fuel_tank, num_of_blades, taken = 'no'):
        super().__init__(capacity,size_of_fuel_tank, taken)
        self.num_of_blades = num_of_blades


