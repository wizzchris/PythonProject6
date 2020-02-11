
from PeopleClass import *
from FlightClass import *
from BuildingsClass import *
from AircraftClass import *



#Lists all passanagers on a flight

#Psudo code
#import all classes
#Start empty list of what you want to track
#airplanes #customer - must be able to select flight and add to them#flights - you will always need

#Init 6 passangers
#init 3 planes
#init 3 routes

#add 2 passangers to each flight
#list passangers in one flight

aircraft = []
flights = []
workers = []
customer = []
building = []

james = Customer('James','London')
customer.append(james)
fred = Customer('Fred', 'USA')
customer.append(fred)
hope = Customer('Hope', 'Germany')
customer.append(hope)
tom = Customer('Tom', 'London')
customer.append(tom)
jaz = Customer('Jaz', 'USA')
customer.append(jaz)
chris = Customer('Chris', 'Germany')
customer.append(chris)

james.set_passport('AB85451556554')
fred.set_passport('CD54212454789')
hope.set_passport('HA44124687962')
tom.set_passport('KG44751521568')
jaz.set_passport('QQ44321654987')
chris.set_passport('YT78549851237')

plane1 = Plane(10, 'Large', 'A1')
aircraft.append(plane1)
plane2 = Plane(8, 'Mediam', 'B2')
aircraft.append(plane2)
plane3 = Plane(6, 'Small', 'C3')
aircraft.append(plane3)

flight1 = Flight('Plane', 'Southampton', 'London', '2/3/2020')
flights.append(flight1)
flight2 = Flight('Plane', 'Southampton', 'USA', '2/3/2020')
flights.append(flight2)
flight3 = Flight('Plane', 'Southampton', 'Germany', '2/3/2020')
flights.append(flight3)

flight1.assign_plane(aircraft)
flight2.assign_plane(aircraft)
flight3.assign_plane(aircraft)

james.assign_plane(flights)
fred.assign_plane(flights)
hope.assign_plane(flights)
tom.assign_plane(flights)
jaz.assign_plane(flights)
chris.assign_plane(flights)

for flight in flights:
    print(flight.destination)
