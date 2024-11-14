import os
from typing import List
from Python.address import Address
from Python.appartment import Appartment
from Python.private_house import PrivateHouse

class FileHandler:
    def __init__(self, filename: str):
        self.filename = filename

    def load_addresses(self) -> List[Address]:
        addresses = []
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    addresses = self._parse_file(file)
            except UnicodeDecodeError:
                print("Warning: UTF-8 decoding failed, trying Windows-1251...")
                with open(self.filename, "r", encoding="windows-1251") as file:
                    addresses = self._parse_file(file)
        return addresses

    def _parse_file(self, file) -> List[Address]:
        addresses = []
        for line in file:
            parts = line.strip().split(":")
            if len(parts) < 2:
                continue
            address_type = parts[0].strip()
            address_data = parts[1].strip().split()
            if address_type == "Private" and len(address_data) >= 3:
                address = PrivateHouse(address_data[0], address_data[1], int(address_data[2]))
                addresses.append(address)
            elif address_type == "Appartment" and len(address_data) >= 4:
                address = Appartment(address_data[0], address_data[1], int(address_data[2]), int(address_data[3]))
                addresses.append(address)
        return addresses

    def save_address(self, address: Address):
        with open(self.filename, 'a', encoding="utf-8") as file:
            file.write(address.to_string() + '\n')