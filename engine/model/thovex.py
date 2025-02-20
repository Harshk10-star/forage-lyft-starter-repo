from datetime import datetime
from car import Car
from battery.nubbin_battery import nubbin_battery
from engine.capulet_engine import CapuletEngine


class Thovex(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(last_service_mileage, current_mileage)
        self.battery = NubbinBattery(last_service_date, current_date)
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
