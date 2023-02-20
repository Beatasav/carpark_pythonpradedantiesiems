import math
from datetime import date, timedelta
from classes.vehicle_info import VehicleInfo

from classes.passenger_vehicles import PassengerVehicle


class Buses(VehicleInfo):

    def __init__(self,  km_per_year, number, fuel_type, fixed_costs,
                 technical_inspection_dates, driving_licence_category, fuel_consumption, insurance_date,
                 passenger_seats):
        super().__init__(km_per_year, number, fuel_type, fixed_costs, technical_inspection_dates,
                         driving_licence_category, fuel_consumption, insurance_date)
        self.passenger_seats = passenger_seats

    def check_expiration_dates(self):
        return PassengerVehicle(self.km_per_year, self.number, self.fuel_type, self.fixed_costs,
                                self.technical_inspection_dates, self.driving_licence_category, self.fuel_consumption,
                                self.insurance_date).check_expiration_dates()

    def giving_costs(self, distance, current_fuel_price):
        return PassengerVehicle(self.km_per_year, self.number, self.fuel_type, self.fixed_costs,
                                self.technical_inspection_dates, self.driving_licence_category, self.fuel_consumption,
                                self.insurance_date).giving_costs(distance=distance,
                                                                  current_fuel_price=current_fuel_price)

    def counting_buses_needed(self, passenger_number: int):
        return math.ceil(passenger_number/self.passenger_seats)

    def giving_cost_by_passenger_number(self, passenger_number: int, distance, current_fuel_price):
        fixed_cost = round(self.fixed_costs * distance / self.km_per_year, 2)
        fuel_price = distance / 100 * self.fuel_consumption * current_fuel_price
        passengers = self.counting_buses_needed(passenger_number=passenger_number)
        return f'Costs for {passenger_number} passengers traveling {distance} kilometers: ' \
               f'{round((fixed_cost + fuel_price) * passengers, 2)} EUR'




buses = Buses(km_per_year=44879, number=1000, fuel_type='dysel', fixed_costs=5500,
                  technical_inspection_dates=date(year=2023, month=5, day=31), driving_licence_category='B',
                  fuel_consumption=25, insurance_date=date(year=2023, month=7, day=31), passenger_seats=20)



# print(buses.counting_buses_needed(21))
# print(buses.giving_costs(distance=650, current_price_of_fuel_type=1.7))
print(buses.giving_cost_by_passenger_number(passenger_number=21, distance=650, current_fuel_price=1.7))
print(buses.check_expiration_dates())



