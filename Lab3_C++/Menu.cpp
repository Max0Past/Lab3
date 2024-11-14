#include "Menu.h"
#include <iostream>
#include <string>
#include <sstream>  // для std::istringstream

void Menu::start() {
    string file_path = "C:/Users/User/Documents/Беляш/VS_code/Lab3/addresses.txt";
    AddressBook address_book(file_path);
    FileHandler file_handler(file_path);
    UI ui(address_book, file_handler);

    int choice = -1;
    while (choice != 0) {
        cout << "\nMenu:\n";
        cout << "1. Load addresses from file\n";
        cout << "2. Add private house\n";
        cout << "3. Add appartment\n";
        cout << "4. Select addresses for mailing\n";
        cout << "5. Analyze addresses\n";
        cout << "0. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            ui.loadAddresses();
            break;
        case 2: {
            string city, street;
            int building_number;
            cin.ignore();  // ігноруємо залишковий символ нового рядка після choice
            cout << "Enter city, street, building number: ";
            string input;
            getline(cin, input); 
            istringstream ss(input);
            if (ss >> city >> street >> building_number) { 
                ui.AddPrivateAddress(city, street, building_number); 
            }
            else {
                cout << "Invalid input format.\n"; 
            }
            break;
        }
        case 3: {
            string city, street;
            int building_number, apartment_number;
            cin.ignore();
            cout << "Enter city, street, building number and apartment number: ";
            string input;
            getline(cin, input);
            istringstream ss(input);
            if (ss >> city >> street >> building_number >> apartment_number) {
                ui.AddAppartmentAddress(city, street, building_number, apartment_number);
            }
            else {
                cout << "Invalid input format.\n";
            }
            break;
        }
        case 4:
            ui.SelectAddressesForMailing();
            break;
        case 5:
            ui.AnalyzeAddresses();
            break;
        case 0:
            cout << "Exiting...\n";
            break;
        default:
            cout << "Invalid choice. Please try again.\n";
        }
    }


    /*FileHandler fileHandler("addresses.txt");
    AddressBook addressBook("addresses.txt");
    int choice;

    do {
        cout << "1. Load addresses from file\n";
        cout << "2. Add private house\n";
        cout << "3. Add apartment\n";
        cout << "4. Analyze addresses\n";
        cout << "5. Save addresses to file\n";
        cout << "0. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            auto loadedAddresses = fileHandler.loadAddresses();
            for (Address* address : loadedAddresses) {
                addressBook.AddAddress(address); 
            }
            cout << "Addresses loaded successfully.\n";
        }
        else if (choice == 2) {
            string city, street;
            int number;
            cout << "Enter city, street and building number: ";
            cin >> city >> street >> number;
            addressBook.AddAddress(new PrivateHouse(city, street, number)); 
        }
        else if (choice == 3) {
            string city, street;
            int number, apartmentNumber;
            cout << "Enter city, street, building number, and apartment number: ";
            cin >> city >> street >> number >> apartmentNumber;
            addressBook.AddAddress(new Appartment(city, street, number, apartmentNumber)); 
        }
        else if (choice == 4) {
            addressBook.AnalyzeAddresses(); 
        }
        else if (choice == 5) {
            fileManager.saveAddressesToFile(addressBook.getAddresses());
            cout << "Addresses saved successfully.\n";
        }
    } while (choice != 0);*/
}
