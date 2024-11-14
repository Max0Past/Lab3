#pragma once
#ifndef UI_H 
#define UI_H

#include "AddressBook.h"
#include "Address.h"
#include "FileHandler.h"

class UI {
public:
    UI(AddressBook& address_book, FileHandler& file_handler);

    void loadAddresses();
    void AddPrivateAddress(const string& city, const string& street, int building_number);
    void AddAppartmentAddress(const string& city, const string& street, int building_number, int appartment_number);
    void AnalyzeAddresses();
    void SelectAddressesForMailing();

private:
    AddressBook& address_book_;
    FileHandler& file_handler_;
};

#endif // UI_H
