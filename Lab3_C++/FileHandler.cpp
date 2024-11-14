#include "FileHandler.h"
#include <fstream>
#include <iostream>
#include <string>

FileHandler::FileHandler(const string& filename) : filename_(filename) {}

vector<shared_ptr<Address>> FileHandler::loadAddressesFromFile() {

    ifstream file(filename_); // Відкриваємо файл
    if (!file.is_open()) { // Перевірка на відкриття
        cerr << "Error: " << filename_ << endl;
        return; // Вихід з функції, якщо файл не відкрито 
    }

    string line;


    // Читаємо файл рядок за рядком
    while (getline(file, line)) {
        cout << line << endl; // Виводимо рядок на екран
    }

    file.close(); // Закриваємо файл
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
