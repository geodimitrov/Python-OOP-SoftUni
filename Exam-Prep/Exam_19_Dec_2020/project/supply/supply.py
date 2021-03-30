from abc import ABC, abstractmethod


class Supply(ABC):

    def __init__(self, needs_increase):
        self.__needs_increase = needs_increase

    @property
    def needs_increase(self):
        return self.__needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")
        self.__needs_increase = value

    @abstractmethod
    def __str__(self):
        pass

    def apply(self, survivor):
        survivor.needs += self.__needs_increase