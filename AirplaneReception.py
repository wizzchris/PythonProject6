
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
customer_list = []
building = []

james = Customer('James','London')
customer_list.append(james)
fred = Customer('Fred', 'Usa')
customer_list.append(fred)
hope = Customer('Hope', 'Germany')
customer_list.append(hope)
tom = Customer('Tom', 'London')
customer_list.append(tom)
jaz = Customer('Jaz', 'Usa')
customer_list.append(jaz)
chris = Customer('Chris', 'Germany')
customer_list.append(chris)

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

the_1_flight = Flight('Plane', 'Southampton', 'London', '2/3/2020')
flights.append(the_1_flight)
the_2_flight = Flight('Plane', 'Southampton', 'Usa', '2/3/2020')
flights.append(the_2_flight)
the_3_flight = Flight('Plane', 'Southampton', 'Germany', '2/3/2020')
flights.append(the_3_flight)

the_1_flight.assign_plane(aircraft)
the_2_flight.assign_plane(aircraft)
the_3_flight.assign_plane(aircraft)


for customer in customer_list:
    customer.assign_flight(flights)

def worker_check(workers,username):
    for worker in workers:
        if username == worker.name:
            return True


while True:
    answer = input('Hello, please give you username:\n').strip().lower()
    if answer == 'add new worker':
        name = input('What is the username?\n')
        name = Worker(name)
        workers.append(name)
    elif worker_check(workers, answer) == True:
        while worker_check(workers, answer):
            print ('Welcome ' + answer)
            answer1 = input('What would you like to do? Type EXIT to exit and HELP for help.\n').strip().lower()
            if answer1 == 'exit':
                break
            elif answer1 == 'help':
                print('Type EXIT to break\nType HELP for help\n')
            elif answer1 == 'add aircraft':
                while True:
                    answer_aircraft = input('What would you like to add?\nA plane?\nType EXIT to return to commands\n').strip().lower()
                    if answer_aircraft == 'exit':
                        break

                    elif answer_aircraft == 'plane':
                        capacity = input('Please specify capacity\n').strip().lower()
                        size_of_fuel_tank = input('Please specify size of fuel tank\n').strip().lower()
                        while True:
                            plane_num = input('Please specify plane number\n')
                            x = '0'
                            for plane in aircraft:
                                if plane.plane_number == plane_num:
                                    x = '1'
                            if x == '1':
                                print('Sorry that is already taken')
                            elif x == '0':
                                print('Plane number accepted')
                                break
                        plane_num = Plane(capacity,size_of_fuel_tank,plane_num)
                        print('Plane successfully created')
                        aircraft.append(plane_num)
                        break
                    else:
                        print('Please put a valid input')

            elif answer1 == 'add flight':
                flight_name = input('Please specify name of flight')
                aircraft = input('Please specify aircraft. Plane?')
                origin = input('Please specify origin of flight')
                destination = input('Please specify destination').strip().lower().capitalize()
                datetime = input('Please specify date')
                print ('Flight successfully created')
                flight_name = Flight(aircraft,origin,destination,datetime)

            elif answer1 == 'add passanger':
                name = input('Please specify name')
                destination = input('Please specify destination of customer')
                print('Passanger successfully created')
                name = Customer(name, destination)

            elif answer1 == 'add passport':
                name = input('Please specify name of passanger you want').lower().strip()
                passport_num = input('Please specify pass port num')
                for passanger in customer_list:
                    if passanger.name == name:
                        passanger.set_passport(passport_num)
                        passanger.assign_flight(flights)

            elif answer1 == 'flight list':
                for flight in flights:
                    print (flight.destination)

            elif answer1 == 'customer list':
                for customer in customer_list:
                    print (customer.name)

            elif answer1 == 'flight customer list':
                flight_choice = input('Please specify flight')
                for flight in flights:
                    if flight.name == flight_choice:
                        x = 0
                        for customer in flight.customers:
                            x += 1
                            print(str(x) + ' '+ customer.name)


    elif answer == 'exit':
        break
    else:
        print('Please give valid username')
