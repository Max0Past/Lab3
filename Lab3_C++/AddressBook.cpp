#include "AddressBook.h"
//#include "FileHandler.h"
#include <fstream>
#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>

AddressBook::AddressBook(string FileName) : filename(FileName) {} 

void AddressBook::AddAddress(shared_ptr<Address> address) {
    addresses_.push_back(address); 
    // ³�������� ���� ��� ���������
    ofstream file(filename, ios::app); // ³�������� ���� � ����� "������"
    if (file.is_open()) {
        // �������� ������ � ����
        cout << endl;
        file << address->toString() << endl; // ����� � ����
        file.close(); // ��������� ����
    }
    else {
        cerr << "Error: " << filename << endl;
    }
}

void AddressBook::AnalyzeAddresses() {
    int privateHouseCount = 0;
    int appartmentCount = 0;
    size_t buildingCount = 0;
    map<int, int> appartmentDistribution;

    // First verify we have selected indices
    if (selected_indices_.empty()) { 
        cout << "No addresses selected for analysis. Please select addresses first." << endl;
        return;
    }

    // Read and process the file to match with selected indices
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        return;
    }

    string line;
    vector<string> fileLines;

    // Store all lines from file
    while (getline(file, line)) {
        fileLines.push_back(line);
    }
    file.close();

    // Process selected addresses
    for (int index : selected_indices_) {  
        // Check if index is valid for our file lines
        if (index >= 0 && index < fileLines.size()) {
            string addressLine = fileLines[index];

            // Parse the address line
            istringstream iss(addressLine);
            string addressType;
            iss >> addressType; // Get first word which should be the type

            if (addressType == "Private" || addressType == "PrivateHouse") {
                privateHouseCount++;
            }
            else if (addressType == "Apartment" || addressType == "Appartment") {
                appartmentCount++;

                // Extract building number from the address line
                int buildingNum = 0;
                string token;
                while (iss >> token) {
                    // Try to find building number in the address string
                    if (isdigit(token[0])) {
                        buildingNum = stoi(token);
                        break;
                    }
                }

                if (buildingNum > 0) {
                    appartmentDistribution[buildingNum]++;
                }
            }
        }
        else {
            cerr << "Warning: Invalid index " << index << " (out of range)" << endl;
        }
    }

    // Calculate building count from apartment distribution
    buildingCount = appartmentDistribution.size();

    // Output analysis results
    cout << "\nAnalysis Results:" << endl;
    cout << "------------------------" << endl;
    cout << "Number of private houses: " << privateHouseCount << endl;
    cout << "Number of apartments: " << appartmentCount << endl;
    cout << "Number of unique buildings: " << buildingCount << endl;

    if (buildingCount > 0) {
        double averageAppartments = static_cast<double>(appartmentCount) / buildingCount;
        cout << "Average number of apartments per building: " << fixed << setprecision(2)
            << averageAppartments << endl;

        // Display distribution of apartments per building
        cout << "\nApartments distribution by building:" << endl;
        for (const auto& pair : appartmentDistribution) {
            cout << "Building " << pair.first << ": " << pair.second << " apartment(s)" << endl;
        }
    }
    else if (appartmentCount > 0) {
        cout << "Warning: Apartments found but building numbers could not be determined." << endl;
    }

    // Verify all addresses were processed
    int totalProcessed = privateHouseCount + appartmentCount;
    if (totalProcessed < selected_indices_.size()) {
        cout << "\nWarning: " << (selected_indices_.size() - totalProcessed)
            << " selected address(es) could not be properly analyzed." << endl;
    }
    cout << endl;
}

void AddressBook::DisplayAddresses() const {
    ifstream file(filename); 
    if (!file.is_open()) { 
        cerr << "Error: " << filename << endl; 
        return; 
    } 

    string line; 
    int index = 1; 
    // ������ ���� ����� �� ������ �� �������� �� ����� 
    while (getline(file, line)) { 
        cout << index++ << ": " << line << endl; // �������� ������ 
    } 

    file.close(); 
}

void AddressBook::SelectAddressesForMailing() {
    DisplayAddresses(); // �������� ������ ��� ������ 

    cout << "Enter the address numbers (separated by a space) that you want to select for the mailing list: "; 
    string input; 
    getline(cin, input); 

    istringstream iss(input); 
    int number; 

    selected_indices_.clear(); // ������� �������� ������ 
    bool validInput = false; // ���� ��� ��������, �� ���� ������ ����� ������ 

    // ������� ������, ������ ������������
    while (iss >> number) { 
        // ������ �� selectedIndices, ���� ����� ������
        if (number > 0) { 
            selected_indices_.push_back(number - 1); // �������� ������ � ������ 0-���������� 
            validInput = true; 
        }
    }

    // ��������, �� ���� ������ ������
    if (validInput) {
        cout << "You have selected addresses with numbers: ";
        for (int index : selected_indices_) { 
            cout << (index + 1) << " "; // �������� ������ � 1-����������
        }
        cout << endl;

    }
    else {
        cout << "No addresses were selected." << endl;
    }
}

void AddressBook::ClearAddresses() {
    addresses_.clear();
}
