from AircraftClass import Plane
import random

class Flight:

    def __init__(self,aircraft, origin, desitnation, date_time, customers = None):
        if customers is None:
            self.customers = []
        self.aircraft = aircraft
        self.destination = desitnation
        self.origin = origin
        self.flight_num = ''
        self.date_time = date_time


    def assign_plane(self,list_of_planes):
        plane_index = 0
        while self.flight_num == '':
            if list_of_planes[plane_index].taken == 'no':
                self.flight_num = list_of_planes[plane_index].plane_number
                list_of_planes[plane_index].taken = 'yes'
            elif list_of_planes[plane_index].taken == 'yes':
                plane_index += 1
            else:
                print('Sorry no planes left')

        return self.flight_num








