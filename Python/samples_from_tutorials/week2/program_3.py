# -*- coding: utf-8 -*-
# pylint: disable=C0103
'''
    Program to convert temperature from celcius to Fahrenheit
    Formula: (°C 9/5)+32 = °F

    Test table:
    Celsius (°C)	Fahrenheit (°F)
        21 °C	        69.8 °F
        30 °C	        86.0 °F
        37 °C	        98.6 °F
        40 °C	        104.0 °F

'''

temperature_in_celcius = float(raw_input("Enter temp in celcius: "))
temperature_in_fahrenheit = (temperature_in_celcius * 9/5) + 32
celcius_symbol = u"\u2103"
fahrenheit_symbol = u"\u2109"
print r"%.2f %s  = %.2f %s" %(temperature_in_celcius, celcius_symbol, \
				temperature_in_fahrenheit, fahrenheit_symbol)
