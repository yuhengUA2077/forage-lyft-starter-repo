from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        # self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
