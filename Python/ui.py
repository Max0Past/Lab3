from Python.file_handler import FileHandler
from Python.address_book import AddressBook
from Python.appartment import Appartment
from Python.private_house import PrivateHouse

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