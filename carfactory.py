from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class CarFactory():

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_date):
        return Calliope(current_date, last_service_date, current_mileage, last_service_date)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_date):
        return Glissade(current_date, last_service_date, current_mileage, last_service_date)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        return Palindrome(current_date, last_service_date, warning_light_is_on)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_date):
        return Rorschach(current_date, last_service_date, current_mileage, last_service_date)
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_date):
        return Thovex(current_date, last_service_date, current_mileage, last_service_date)


