#!/usr/bin/env python3

from sense_hat import SenseHat
import time

sense = SenseHat()

try:
    while True:
        pressure = sense.get_pressure()
        print(f"Barometric Pressure: {pressure:.2f} hPa")
        time.sleep(5)  # read every 5 seconds
except KeyboardInterrupt:
    print("Stopping the program...")
    print("Stopped.")
