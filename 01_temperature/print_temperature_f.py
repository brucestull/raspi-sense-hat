#!/usr/bin/env python3

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temperature_c = sense.get_temperature()
temperature_f = temperature_c * 9 / 5 + 32

print("Current Temperature (F):", temperature_f)
