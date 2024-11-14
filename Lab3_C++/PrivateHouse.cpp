#include "PrivateHouse.h"

PrivateHouse::PrivateHouse(string City, string Street, int BuildingNumber)
    : Address(City, Street, BuildingNumber) {}

string PrivateHouse::GetType() const {
    return "Private House";
}
string PrivateHouse::toString() const {
    return "Private House: " + city + " " + street + " " + to_string(buildingNumber);
}
