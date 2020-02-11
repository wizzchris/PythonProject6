

class People:
    def __init__(self, name, heart = 'yes'):
        self.name = name
        self.heart = heart



class Worker(People):
    def __init__(self, name, heart = 'yes' ):
        super().__init__(name, heart)


class Customer(People):
    def __init__(self, name , destination, heart = 'yes'):
        super().__init__(name, heart)
        self.__passport = ''
        self.destination = destination

    def set_passport(self,passport_number):
        self.__passport = passport_number
        return self.__passport


    def assign_flight(self, flight_list):
        for flight in flight_list:
            if self.destination == flight.destination:
                flight.customers.append(self)


