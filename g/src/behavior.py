from abc import ABC, abstractmethod

class Behavior(ABC):
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass