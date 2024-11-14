#include "Ui.h"
#include "AddressBook.h" 
#include "AddressBook.cpp"
#include "FileHandler.h"
#include "PrivateHouse.h"
#include "Appartment.h"
#include <iostream>

UI::UI(AddressBook& address_book, FileHandler& file_handler)
    : address_book_(address_book), file_handler_(file_handler) {}

void UI::loadAddresses() {
        address_book_.ClearAddresses();  // Очищення перед завантаженням  

        auto addresses = file_handler_.loadAddressesFromFile();
        for (const auto& address : addresses) {
            address_book_.AddAddress(address); 
        }

        cout << "Addresses loaded successfully. Here is the list of addresses:\n";
        address_book_.DisplayAddresses();  
}

void UI::AddPrivateAddress(const string& city, const string& street, int building_number) {
    auto address = make_shared<PrivateHouse>(city, street, building_number);
    address_book_.AddAddress(address);
    file_handler_.saveAddress(*address); 
}

void UI::AddAppartmentAddress(const string& city, const string& street, int building_number, int appartment_number) {
    auto address = make_shared<Appartment>(city, street, building_number, appartment_number);
    address_book_.AddAddress(address);
    file_handler_.saveAddress(*address); 
}

void UI::AnalyzeAddresses() {
    address_book_.AnalyzeAddresses();
}

void UI::SelectAddressesForMailing() {
    address_book_.SelectAddressesForMailing();
}
