

class Car:
    def __init__(self, make, model, year, odometer_reading=0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back mileage!!")

    def read_odometer(self):
        print(self.odometer_reading)

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage


class Battery:
    def __init__(self, battery_size=75, range=360):
        self.battery_size = battery_size
        self.range = range

    def display_battery_size(self):
        print(f"You have a {self.battery_size} kWh battery")

    def decrement_range(self):
        self.range -= 20

    def display_range(self):
        print(f"You have {self.range} miles left")


my_car = Car('Honda', 'Civic', 2007)

friends_car = Car('Honda', 'Accord', 2010, 50000)

'''
my_car.read_odometer()
my_car.update_odometer(75000)
my_car.read_odometer()

friends_car.read_odometer()
friends_car.odometer_reading = 80000
friends_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()
'''


class ElectricCar(Car):
    def __init__(self, make, model, year, odometer_reading):
        super().__init__(make, model, year, odometer_reading)
        self.battery = Battery()


my_tesla = ElectricCar("Tesla", "Model S", 2020, 50)
my_tesla.read_odometer()
my_tesla.battery.display_battery_size()
# the super() function just allows for calling from parent class
my_tesla.battery.decrement_range()
my_tesla.battery.display_range()
