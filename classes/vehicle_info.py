from datetime import date


class VehicleInfo:

    def __init__(self, km_per_year, number, fuel_type, fixed_costs, technical_inspection_dates, driving_licence_category,
                 fuel_consumption, insurance_date):

        self.km_per_year = km_per_year
        self.number = number
        self.fuel_type = fuel_type
        self.fixed_costs = fixed_costs
        self.technical_inspection_dates = technical_inspection_dates
        self.driving_licence_category = driving_licence_category
        self.fuel_consumption = fuel_consumption
        self.insurance_date = insurance_date


