from abc import ABC, abstractmethod

class Address(ABC):     
    def __init__(self, city: str, street: str, building_number: int):
        self._city = city
        self._street = street
        self._building_number = building_number

    @property
    def city(self) -> str:
        return self._city

    @property
    def street(self) -> str:
        return self._street

    @property
    def building_number(self) -> int:
        return self._building_number

    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass
