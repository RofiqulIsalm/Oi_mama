from abc import ABC, abstractmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.derivers = []
        self.rides = []
    def add_rider(self,rider):
        self.riders.append(rider)
    def add_driver(self,driver):
        self.derivers.append(driver)
    

    def __repr__(self) -> str:
        return f'Company name: {self.company_name}\nRiders: {len(self.riders)}\nDrivers: {len(self.derivers)}'

class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name = name
        self.email = email
        # TODO:
        self.__id = 0
        self.__nid = nid
        self.wallet = 0
    @abstractmethod
    def display_Profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid,current_location,initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nid)
    
    def display_Profile(self):
        print(f'_____  Rider----->  {self.name}\n-----> {self.email}')
    def load_cash(self, amount):
        if amount >0:
            self.wallet += amount
    def update_location(self,current_location):
        self.current_location = current_location

    def Request_ride(self,ride_shring, destination):
        if not self.current_ride:
            ride_request = Ride_request(self,destination)
            ride_matcher = Ride_matching(ride_shring.derivers)
            self.current_ride = ride_matcher.find_driver(ride_request)

    def show_current_ride(self):
        print(f'current ride : {self.current_ride}')
            

class Driver(User):
    def __init__(self, name, email, nid) -> None:
        self.wallet = 0
        super().__init__(name, email, nid)

    
    def display_Profile(self):
        print(f'----->  {self.name}\n-----> {self.email}')

    def accept_ride(self,ride):
        print(f'Accepted the ride..')
        ride.set_driver(self)

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self,driver):
        self.driver = driver
    def start_ride(self):

        self.ride_start = datetime.now()
    def end_ride(self,amount):
        self.ride_end = datetime.now()
        self.ride.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
    def __repr__(self) -> str:
        return f'Ride start from: {self.start_location} --> {self.end_location}'

class Ride_request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location
        print(f'Found Ride...')
    
    
class Ride_matching:
    def __init__(self,Drivers) -> None:
        self.availabel_drivers = Drivers
    
    def find_driver(self,ride_request):
        if len(self.availabel_drivers) > 0:
            driver = self.availabel_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            print(f'Ride found from ---> {ride.start_location}')
            return ride

class Vehicle:
    speed = {
        "car ": 150,
        "bike ": 70,
        "cng ": 50
    }
    def __init__(self,vehicle_type,license_plate,rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'Availabel'

    @abstractmethod
    def start_drive(self):
        pass

class car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'Unavailabel'

class bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'Unavailabel'

class cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'Unavailabel'


Oi_mama = Ride_sharing("Oi_mama")
Rafiq = Rider("Rafiq", 'code.dev.rafiq@Oimama.com', 3145875, 'saver', 300)
Oi_mama.add_rider(Rafiq)
Rafiq2 = Rider("Rafiq2", 'code.dev.rafiq@Oimama.com', 3145875, 'saver', 300)
Oi_mama.add_rider(Rafiq2)
Rafiq3 = Rider("Rafiq3", 'code.dev.rafiq@Oimama.com', 3145875, 'saver', 300)
Oi_mama.add_rider(Rafiq3)
Parky = Driver("Parky", 'parky@oimama.com',456758)
Oi_mama.add_driver(Parky)
print(Oi_mama)

print('_______________________________________')

Rafiq.Request_ride(Oi_mama,'Dhaka')
Rafiq.show_current_ride()