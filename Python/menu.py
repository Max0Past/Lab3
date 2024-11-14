from Python.file_handler import FileHandler
from Python.address_book import AddressBook
from Python.ui import UI


class Menu:
    def start(self):
        file_path = "C:/Users/Max/OOP/Lab_3/Python/addresses.txt"
        address_book = AddressBook()
        file_handler = FileHandler(file_path)
        ui = UI(address_book, file_handler)


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