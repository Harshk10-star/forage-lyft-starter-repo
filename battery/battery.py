from abc import ABC

class Battery(ABC):
    def __init__(self):
    
    @abstractmethod
    def needs_service(self):
        pass