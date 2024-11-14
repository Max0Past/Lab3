#include "Address.h"

Address::Address(string City, string Street, int BuildingNumber)
    : city(City), street(Street), buildingNumber(BuildingNumber) {}

string Address::GetCity() const {
    return city;
}

string Address::GetStreet() const {
    return street;
}

int Address::GetBuildingNumber() const {
    return buildingNumber;
}