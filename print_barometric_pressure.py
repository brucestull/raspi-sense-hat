#!/usr/bin/env python3

from sense_hat import SenseHat

sense = SenseHat()

# Get pressure in millibars (hPa)
pressure = sense.get_pressure()

print(f"Barometric Pressure: {pressure:.2f} hPa")
