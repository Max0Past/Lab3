from Python.address import Address

class PrivateHouse(Address):
    def get_type(self) -> str:
        return "Private"

    def to_string(self) -> str:
        return f"Private: {self.city} {self.street} {self.building_number}"
