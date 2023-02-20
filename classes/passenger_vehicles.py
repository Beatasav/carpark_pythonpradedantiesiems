from datetime import date, timedelta
from classes.vehicle_info import VehicleInfo


class PassengerVehicle(VehicleInfo):

    def __init__(self,  km_per_year, number, fuel_type, fixed_costs,
                 technical_inspection_dates, driving_licence_category, fuel_consumption, insurance_date):
        super().__init__(km_per_year, number, fuel_type, fixed_costs, technical_inspection_dates,
                         driving_licence_category, fuel_consumption, insurance_date)

    def check_expiration_dates(self):
        now = date.today().replace(day=1)
        following_month_first_day = (now + timedelta(31)).replace(day=1)
        after_following_month_first_day = (now + timedelta(62)).replace(day=1)
        if following_month_first_day <= self.technical_inspection_dates < after_following_month_first_day:
            return f'TI expiring next month'
        elif following_month_first_day <= self.insurance_date < after_following_month_first_day:
            return f'Insurance expiring next month'
        elif following_month_first_day <= self.technical_inspection_dates and self.insurance_date \
                < after_following_month_first_day:
            return f'TI and insurance expiring next month'
        else:
            return f'TI valid until: {self.technical_inspection_dates}, INSURANCE valid until: {self.insurance_date}'

    def giving_costs(self, distance, current_fuel_price):
        fixed_cost = round(self.fixed_costs * distance / self.km_per_year, 2)
        fuel_price = round(distance / 100 * self.fuel_consumption * current_fuel_price)
        return f'Costs of number {self.number} for {distance}km distance are: ' \
               f'Fixed costs: {fixed_cost} EUR , Fuel costs: {fuel_price} EUR, ' \
               f'Total: {round(fixed_cost + fuel_price, 2)} EUR'


passengervehicle = PassengerVehicle(km_per_year=14785, number=1, fuel_type='diesel',
                                             fixed_costs=1500,
                                             technical_inspection_dates=date(year=2023, month=5, day=31),
                                             driving_licence_category='B', fuel_consumption=7,
                                             insurance_date=date(year=2023, month=7, day=31)

print(passengervehicle.check_expiration_dates()),
print(passengervehicle.giving_costs(650, 1.7));


