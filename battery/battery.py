from abc import *


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass
