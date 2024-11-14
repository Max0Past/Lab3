#include "FileHandler.h"
#include <fstream>
#include <iostream>
#include <string>

FileHandler::FileHandler(const string& filename) : filename_(filename) {}

vector<shared_ptr<Address>> FileHandler::loadAddressesFromFile() {

    ifstream file(filename_); // ³�������� ����
    if (!file.is_open()) { // �������� �� ��������
        cerr << "Error: " << filename_ << endl;
        return; // ����� � �������, ���� ���� �� ������� 
    }

    string line;


    // ������ ���� ����� �� ������
    while (getline(file, line)) {
        cout << line << endl; // �������� ����� �� �����
    }

    file.close(); // ��������� ����
}

void FileHandler::saveAddress(const Address& address) const {
    ofstream file(filename_, ios::app);
    if (file.is_open()) {
        file << address.toString() << "\n";
        file.close();
    }
    else {
        cerr << "Error opening file for saving." << endl;
    }
}
