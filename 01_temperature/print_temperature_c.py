#!/usr/bin/env python3

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temperature_c = sense.get_temperature()

print("Current Temperature (C):", temperature_c)
