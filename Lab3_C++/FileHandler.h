#pragma once
#ifndef FILEHANDLER_H
#define FILEHANDLER_H

#include <string>
#include <vector>
#include <memory>
#include "Address.h"

class UI; // ����� ���������� ��� ��������� ��������� ��������� 

class FileHandler {
public:
    FileHandler(const string& filename);

    vector<shared_ptr<Address>> loadAddressesFromFile();  
    void saveAddress(const Address& address) const;

    friend UI;

private:
    string filename_;
};

#endif // FILEHANDLER_H
