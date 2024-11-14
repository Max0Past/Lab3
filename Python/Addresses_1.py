import os   # для роботи з файлами та шляхами
from abc import ABC, abstractmethod # для створення абстрактних класів
from typing import List, Dict   # для анотації типів списків і словників


class Address(ABC):     # Абстрактний клас адреси
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


class PrivateHouse(Address):
    def get_type(self) -> str:
        return "Private"

    def to_string(self) -> str:
        return f"Private: {self.city} {self.street} {self.building_number}"


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



class UI:
    def __init__(self, address_book: AddressBook, file_handler: FileHandler):
        self.address_book = address_book
        self.file_handler = file_handler

    def load_addresses(self):
        # Очищуємо список адрес перед новим завантаженням, щоб уникнути дублювання
        self.address_book.addresses.clear()

        # Завантажуємо адреси з файлу та додаємо їх до книги адрес
        addresses = self.file_handler.load_addresses()
        for address in addresses:
            self.address_book.add_address(address)

        print("Addresses loaded successfully. Here is the list of addresses:")
        self.address_book.display_addresses()  # Виводимо список адрес після завантаження

    def add_private_address(self, city: str, street: str, building_number: int):
        address = PrivateHouse(city, street, building_number)
        self.address_book.add_address(address)
        self.file_handler.save_address(address)

    def add_appartment_address(self, city: str, street: str, building_number: int, appartment_number: int):
        address = Appartment(city, street, building_number, appartment_number)
        self.address_book.add_address(address)
        self.file_handler.save_address(address)

    def analyze_addresses(self):
        self.address_book.analyze_addresses()

    def select_addresses_for_mailing(self):
        self.address_book.select_addresses_for_mailing()




class Menu:
    def start(self):
        file_path = "C:/Users/Max/OOP/Lab_3/Python/addresses.txt"
        address_book = AddressBook()
        file_handler = FileHandler(file_path)
        ui = UI(address_book, file_handler)

        ui.load_addresses()

        choice = -1
        while choice != 0:
            print("\nMenu:")
            print("1. Load addresses from file")
            print("2. Add private house")
            print("3. Add appartment")
            print("4. Select addresses for mailing")
            print("5. Analyze addresses")
            print("0. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                ui.load_addresses()
            elif choice == 2:
                city, street, number = input("Enter city, street, building number: ").split()
                ui.add_private_address(city, street, int(number))
            elif choice == 3:
                city, street, number, apartment_number = input("Enter city, street, building number and apartment number: ").split()
                ui.add_appartment_address(city, street, int(number), int(apartment_number))
            elif choice == 4:
                ui.select_addresses_for_mailing()
            elif choice == 5:
                ui.analyze_addresses()

if __name__ == "__main__":
    menu = Menu()
    menu.start()
