from abc import *


class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass
