from Python.address import Address

class Appartment(Address):
    def __init__(self, city: str, street: str, building_number: int, appartment_number: int):
        super().__init__(city, street, building_number)
        self._appartment_number = appartment_number

    @property
    def appartment_number(self) -> int:
        return self._appartment_number

    def get_type(self) -> str:
        return "Appartment"

    def to_string(self) -> str:
        return f"Appartment: {self.city} {self.street} {self.building_number} {self.appartment_number}"
