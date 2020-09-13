class ElectricCar(Car):
    def __init__(self, make, model, year, odometer_reading):
        super.__init__(make, model, year, odometer_reading)


my_tesla = ElectricCar("Tesla", "Model S", 2020, 0)
