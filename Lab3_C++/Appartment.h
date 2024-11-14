#pragma once
#ifndef APPARTMENT_H
#define APPARTMENT_H

#include "Address.h"

class Appartment : public Address {
private:
    int appartmentNumber;
public:
    Appartment(string City, string Street, int BuildingNumber, int AppartmentNumber);
    int GetAppartmentNumber() const;
    string GetType() const override;
    string toString() const;
};

#endif // APPARTMENT_H