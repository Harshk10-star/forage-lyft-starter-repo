from datetime import datetime
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.sternman_engine import SternmanEngine


class Palindrome(Car):
    def __init__(self,current_date, last_service_date, warning_light_is_on):
        self.engine = SternmanEngine(warning_light_is_on)
        self.battery = SpindlerBattery(last_service_date, current_date)
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
