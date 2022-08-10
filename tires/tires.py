from abc import *


class Tires(ABC):
    @abstractmethod
    def needs_service(self):
        pass
