

class Aircraft:
    def __init__(self, capacity, size_of_fuel_tank, taken = 'no'):
        self.capacity = capacity
        self.size_of_fuel_tank = size_of_fuel_tank
        self.taken = taken


class Plane(Aircraft):
    def __init__(self, capacity, size_of_fuel_tank, plane_number,taken = 'no' ):
        super().__init__(capacity,size_of_fuel_tank, taken)
        self.plane_number = plane_number




