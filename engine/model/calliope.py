from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery

class Calliope(Car):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_date):
        self.engine = CapuletEngine(last_service_mileage, current_date)
        self.battery = SpindlerBattery(last_service_date, current_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
