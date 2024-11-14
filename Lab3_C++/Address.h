#pragma once
#ifndef ADDRESS_H 
#define ADDRESS_H

#include <string>
using namespace std;

class Address {
protected:
    string city;
    string street;
    int buildingNumber;
public:
    Address(string City, string Street, int BuildingNumber);
    virtual string GetType() const = 0;
    string GetCity() const;
    string GetStreet() const;
    int GetBuildingNumber() const;
    virtual ~Address() = default;

    virtual string toString() const = 0; // Віртуальний метод для отримання рядкового представлення
};

#endif // ADDRESS_H
