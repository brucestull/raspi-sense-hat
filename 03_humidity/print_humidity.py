#!/usr/bin/env python3

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

humidity = sense.get_humidity()
print("Humidity (%):", humidity)
