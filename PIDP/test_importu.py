# import test #<--- test.car()
# from test import car  #<---car()
# from test import car as caaar  #<c--- aaar()
# import test as mn #<---mn.car()
# from test import *


# car_1 = car("audi", "tt", predkosc = " 300 km/h", kolor = "black")
# print(car_1)


class Car():
	"""Tutaj powinien być krutki docstring"""
	
	def __init__(self, make, model, year):
		"""Kolejny docstring"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		"""Naastepny doc string"""
		long_name = str(self.year) + " " + self.make + " " + self.model
		return (long_name)
	
	def read_odometer(self):
		"""Doc string"""
		print("Ten samochód ma przejechane " + str(self.odometer_reading) + " km")
	
	def update_odometer(self, mileage):
		"""Doc string"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("Nie cofniesz licznika")
	
	def increment_odometer(self, kilometres):
		"""Doc string"""
		if kilometres >= 0:
			self.odometer_reading += kilometres
		else:
			print("Tak też nie cofniesz licznika")


class Battery():
	"""Ta klasa będzie w klasie ElectricCar"""
	
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""DocString"""
		print("Ten samochód ma baterie o pojemnosci " + str(self.battery_size) + "kWh")
	
	def get_range(self):
		"""DocString"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "Zasięg tego samochodu to " + str(range)
		message += " po pełnym naładowaniu akumulatorów"
		print(message)
	
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85


class ElectricCar(Car):
	"""DocString DZIEDZICZENIE"""
	
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()