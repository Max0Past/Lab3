from typing import List, Dict
from Python.address import Address
from Python.private_house import PrivateHouse
from Python.appartment import Appartment

class AddressBook:
    def __init__(self):
        self.addresses: List[Address] = []      # список адрес
        self.selected_indices: List[int] = []   # індекси вибраних адрес для розсилки

    def add_address(self, address: Address):
        # Додає нову адресу до списку
        self.addresses.append(address)

    def analyze_addresses(self):
        private_house_count = 0
        appartment_count = 0
        appartment_distribution: Dict[int, int] = {}

        if not self.selected_indices:
            print("There are no addresses selected for analysis.")
            return

        # Обробляємо вибрані адреси
        for index in self.selected_indices:
            address = self.addresses[index]
            if address.get_type() == "Private":
                private_house_count += 1
            elif address.get_type() == "Appartment":
                appartment_count += 1
                building_number = address.building_number
                if building_number in appartment_distribution:
                    appartment_distribution[building_number] += 1
                else:
                    appartment_distribution[building_number] = 1

        building_count = len(appartment_distribution)
        print("\nAnalysis Results:")
        print(f"Number of private houses: {private_house_count}")
        print(f"Number of appartments: {appartment_count}")
        print(f"Number of unique buildings: {building_count}")
        if building_count > 0:
            average_appartments = appartment_count / building_count
            print(f"Average number of appartments per building: {average_appartments:.2f}")
            for building, count in appartment_distribution.items():
                print(f"Building {building}: {count} appartments")

    def display_addresses(self):
        for idx, address in enumerate(self.addresses, start=1):
            print(f"{idx}: {address.to_string()}")

    def select_addresses_for_mailing(self):
        # Дозволяє користувачу обрати адреси для розсилки
        self.display_addresses()
        input_str = input("Enter the numbers of the addresses (separated by spaces) for mailing:  ")
        selected_numbers = input_str.split()

        self.selected_indices.clear()
        for num_str in selected_numbers:
            try:
                number = int(num_str) - 1
                if 0 <= number < len(self.addresses):
                    self.selected_indices.append(number)
            except ValueError:
                print(f"Invalid number: {num_str}")

        if self.selected_indices:
            print("You have selected addresses with numbers:", ", ".join(str(i + 1) for i in self.selected_indices))
        else:
            print("No addresses have been selected.")