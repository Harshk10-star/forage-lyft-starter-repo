from abc import ABC

class Engine(ABC):
    def __init__(self):
    
    @abstractmethod
    def needs_service(self):
        pass