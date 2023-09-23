from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    # true is any of the parts return true
    def needs_service(self):
        pass
