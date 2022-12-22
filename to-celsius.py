#!/usr/bin/env python3.7

#python implementation goes here, float as the number

farenheit = float(input("What temperature (in farenheit) would you like converted to celsius? "))
celsius = (farenheit - 32 ) * 5 / 9

#Print the number is farenheit, run the celsius variable to see temp

print(farenheit, "F is", round(celsius, 2), "C")