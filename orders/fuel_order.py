from abc import ABC, abstractmethod


class FuelOrderInterface(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def log(self):
        pass
