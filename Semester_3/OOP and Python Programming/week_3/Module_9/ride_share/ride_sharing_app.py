from abc import ABC, abstractmethod
import datetime


class Ride_sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f"{self.company_name} with riders : {len(self.riders)} and drivers {len(self.drivers)}"


class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        # TODO : set user id dynamically
        self.__id = 0
        self.__nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_money) -> None:
        super().__init__(name, email, nid)
        self.current_ride = None
        self.wallet = initial_money
        self.current_location = current_location

    def update_location(self, current_location):
        self.current_location = current_location

    def load_cash(self, amount):
        if (amount >= 0):
            self.wallet += amount

    def display_profile(self):
        print(f"Rider : {self.name} and email {self.email}")

    def request(self, rider_sharing, destination):
        if (not self.current_ride):
            ride_request = Ride_request(self, destination)
            rider_matcher = Ride_matching(rider_sharing.drivers)
            self.current_ride = rider_matcher.find_drivers(ride_request)

    def show_ride_details(self):
        print(self.current_ride)


class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def accept_ride(self, ride):
        ride.set_driver(self)

    def display_profile(self):
        print(f"Driver : {self.name} and email {self.email}")


class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f"Rider started from : {self.start_location} to {self.end_location}"


class Ride_request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location


class Ride_matching:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers

    def find_drivers(self, ride_request):
        if (len(self.available_drivers) > 0):
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location,
                        ride_request.end_location)
            driver.accept_ride(ride)
            return ride


class Vehicle(ABC):
    speed = {
        "car": 50,
        "bike": 60,
        "cng": 20
    }

    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = "available"

    @abstractmethod
    def start_drive(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = "unavailable"


class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = "unavailable"


pathao = Ride_sharing("Pathao")

shakib = Rider("Shakib", "shakib75@gmail.com", 1234, "Bosundhora ave", 2000)
pathao.add_rider(shakib)
ratan_ahmed = Driver("Ratan Ahmed", "ratan@gmail.com", 123445, "Gulsan 1")
pathao.add_driver(ratan_ahmed)

shakib.request(pathao, "Uttara")
shakib.show_ride_details()
# print(pathao)
