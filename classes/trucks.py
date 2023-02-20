from datetime import date
import math
from classes.vehicle_info import VehicleInfo
from classes.passenger_vehicles import PassengerVehicle


class Trucks(VehicleInfo):

    def __init__(self,  km_per_year, number, fuel_type, fixed_costs,
                 technical_inspection_dates, driving_licence_category, fuel_consumption, insurance_date,
                 weight_capacity, trailer, trailer_weight_capacity):
        super().__init__(km_per_year, number, fuel_type, fixed_costs, technical_inspection_dates,
                         driving_licence_category, fuel_consumption, insurance_date)
        self.weight_capacity = weight_capacity
        self.trailer = trailer
        self.trailer_weight_capacity = trailer_weight_capacity

    def check_expiration_dates(self):
        return PassengerVehicle(self.km_per_year, self.number, self.fuel_type, self.fixed_costs,
                                self.technical_inspection_dates, self.driving_licence_category, self.fuel_consumption,
                                self.insurance_date.check_expiration_dates())

    def giving_costs(self, distance, current_fuel_price):
        return PassengerVehicle(self.km_per_year, self.number, self.fuel_type, self.fixed_costs,
                                self.technical_inspection_dates, self.driving_licence_category, self.fuel_consumption,
                                self.insurance_date.giving_costs(distance=distance,
                                                                 current_fuel_price=current_fuel_price))

    def counting_capacity(self, weight):
        if self.trailer is True:
            trips = weight / (self.weight_capacity + self.trailer_weight_capacity)
            trailers = math.ceil((weight - (self.weight_capacity * trips)) / self.trailer_weight_capacity)
            return trailers
        else:
            return math.ceil(weight/self.weight_capacity)

    def delivery_costs(self, weight, distance, current_fuel_price):
        trips = self.counting_capacity(weight)
        fixed_cost = round(self.fixed_costs * distance / self.km_per_year, 2)
        fuel_price = distance / 100 * self.fuel_consumption * current_fuel_price
        return f'Costs for {weight} tones delivery traveling {distance} kilometers: ' \
               f'{round((fixed_cost + fuel_price) * trips, 2)} EUR'




trucks = Trucks(km_per_year=95876, number=100, fuel_type='dysel', fixed_costs=14500, technical_inspection_dates=date(year=2023, month=7, day=31), driving_licence_category='smtgh',
                fuel_consumption=32, insurance_date=date(year=2023, month=5, day=31),weight_capacity=12, trailer=False,
                trailer_weight_capacity=5)
# print(trucks.giving_costs(distance=650, current_fuel_price=1.7))
print(trucks.counting_capacity(20))
print(trucks.delivery_costs(20, 650, 1.7))

