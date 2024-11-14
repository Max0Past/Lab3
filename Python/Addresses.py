import os   # для роботи з файлами та шляхами
from abc import ABC, abstractmethod # для створення абстрактних класів
from typing import List, Dict   # для анотації типів списків і словників

class Address(ABC):     # абстрактний клас
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
        # Повертає тип адреси
        pass

    @abstractmethod
    def to_string(self) -> str:
        # Повертає рядкове представлення адреси
        pass

class PrivateHouse(Address):
    def __init__(self, city: str, street: str, building_number: int):
        # super() для виклику конструктора базового класу Address
        super().__init__(city, street, building_number)

    def get_type(self) -> str:
        # Повертає тип адреси 
        return "Private"

    def to_string(self) -> str:
        # Повертає рядкове представлення адреси
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
    def __init__(self, filename: str):
        self.filename = filename
        self.addresses: List[Address] = []      # список об’єктів адрес
        self.selected_indices: List[int] = []   # індекси вибраних адрес для аналізу
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                print("Loading addresses from file:")
                for line in file:
                    parts = line.strip().split(":")
                    
                    if len(parts) < 2:
                        continue  #  Пропускаємо некоректні рядки

                    address_type = parts[0].strip()  # Тип адреси, наприклад, «Private» або «Appartment»
                    address_data = parts[1].strip().split()  # Інша частина адреси

                    # Парсимо дані залежно від типу адреси
                    if address_type == "Private":
                        if len(address_data) >= 3:
                            city = address_data[0]
                            street = address_data[1]
                            building_number = int(address_data[2])
                            address = PrivateHouse(city, street, building_number)
                            self.addresses.append(address)

                    elif address_type == "Appartment":
                        if len(address_data) >= 4:
                            city = address_data[0]
                            street = address_data[1]
                            building_number = int(address_data[2])
                            appartment_number = int(address_data[3])
                            address = Appartment(city, street, building_number, appartment_number)
                            self.addresses.append(address)
                
                print("Addresses successfully loaded into the list.")
        except FileNotFoundError:
            print(f"File not found. Make sure that the file {self.filename} exists.")

    def add_address(self, address: Address):
        # Додає нову адресу до книги адрес та записує її у файл
        self.addresses.append(address)
        with open(self.filename, 'a') as file:
            file.write(address.to_string() + '\n')

    def load_addresses_from_file(self):
        # Виводить вміст файлу на екран, без додавання адрес до списку
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                print("File contents:")
                for line in file:
                    print(line.strip())  # Виводимо кожен рядок без зайвих пробілів
            print("File contents successfully output.")
        except FileNotFoundError:
            print(f"File not found. Make sure that the file {self.filename} exists.")

    def analyze_addresses(self):
        # Аналізує обрані адреси для розсилки
        private_house_count = 0
        appartment_count = 0
        appartment_distribution: Dict[int, int] = {}

        if not self.selected_indices:
            print("There are no addresses selected for analysis.")
            return

        # Обробляємо вибрані адреси
        for index in self.selected_indices:
            if 0 <= index < len(self.addresses):
                address = self.addresses[index]
                
                if address.get_type() == "Private":
                    private_house_count += 1
                elif address.get_type() == "Appartment":
                    appartment_count += 1
                    building_number = address.building_number

                    # Оновлюємо розподіл квартир за номерами будівель
                    if building_number in appartment_distribution:
                        appartment_distribution[building_number] += 1
                    else:
                        appartment_distribution[building_number] = 1
            else:
                print(f"Warning: Wrong index {index}")

        # Підраховуємо унікальні будівлі та виводимо результати
        building_count = len(appartment_distribution)

        print("\nAnalysis Results:")
        print("------------------------")
        print(f"Number of private houses: {private_house_count}")
        print(f"Number of appartments: {appartment_count}")
        print(f"Number of unique buildings: {building_count}")

        if building_count > 0:
            average_appartments = appartment_count / building_count
            print(f"Average number of appartments per building: {average_appartments:.2f}")
            print("\nDistribution of appartments by houses:")
            for building, count in appartment_distribution.items():
                print(f"Building {building}: {count} appartments")

    def display_addresses(self):
        # Виводить список адрес із файлу
        if not os.path.isfile(self.filename):
            print(f"Error: {self.filename} not found.")
            return
        with open(self.filename, 'r') as file:
            for idx, line in enumerate(file, start=1):
                print(f"{idx}: {line.strip()}")

    def select_addresses_for_mailing(self):
        # Дозволяє користувачу обрати адреси для розсилки за номером
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

class Menu:
    def start(self):
        file_path = os.path.join("C:/Users/Max/OOP/Lab_3/Python", "addresses.txt")
        address_book = AddressBook(file_path)
        choice = -1

        while choice != 0:
            print("1. Load addresses from file")
            print("2. Add private house")
            print("3. Add appartment")
            print("4. Select addresses for mailing")
            print("5. Analyze addresses")
            print("0. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("------------------")
                address_book.load_addresses_from_file()
                print("------------------")
            elif choice == 2:
                city, street, number = input("Enter city, street and building number: ").split()
                address_book.add_address(PrivateHouse(city, street, int(number)))
            elif choice == 3:
                city, street, number, apartment_number = input("Enter city, street, building number and apartment number: ").split()
                address_book.add_address(Appartment(city, street, int(number), int(apartment_number)))
            elif choice == 4:
                address_book.select_addresses_for_mailing()
            elif choice == 5:
                address_book.analyze_addresses()

if __name__ == "__main__":
    menu = Menu()
    menu.start()
