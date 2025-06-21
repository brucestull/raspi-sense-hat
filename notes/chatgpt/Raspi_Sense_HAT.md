# Measure pressure Sense HAT - ChatGPT - Shared

- [Measure pressure Sense HAT - ChatGPT - Shared](https://chatgpt.com/share/68570add-2354-8002-94f1-4eb412672337)

To measure **barometric pressure** using a **Sense HAT** on your **Raspberry Pi 4** and display it to the terminal, follow these steps:

---

### ✅ Step 1: Install the Sense HAT software

Run the following command to install the required packages:

```bash
sudo apt update
sudo apt install sense-hat python3-sense-hat
```

---

### ✅ Step 2: Create a Python script

You can use the built-in `sense_hat` Python module to access the barometer.

```python
from sense_hat import SenseHat

sense = SenseHat()

# Get pressure in millibars (hPa)
pressure = sense.get_pressure()

print(f"Barometric Pressure: {pressure:.2f} hPa")
```

Save it as, for example: `read_pressure.py`

---

### ✅ Step 3: Run the script

```bash
python3 read_pressure.py
```

---

### ✅ Optional: Repeated readings

To see updates over time, modify the script like this:

```python
from sense_hat import SenseHat
import time

sense = SenseHat()

try:
    while True:
        pressure = sense.get_pressure()
        print(f"Barometric Pressure: {pressure:.2f} hPa")
        time.sleep(5)  # read every 5 seconds
except KeyboardInterrupt:
    print("Stopped.")
```

---

Let me know if you'd like to **log the pressure to a file**, **plot it**, or **display it on the Sense HAT LED matrix**.
