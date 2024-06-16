#!/usr/bin/python3

import time
import os

# Function to read CPU temperature
def get_cpu_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return float(temp.replace("temp=", "").replace("'C\n", ""))

# Function to set fan speed
def set_fan_speed(speed):
    # Adjust the fan speed using i2cset (0-100)
    os.system(f"i2cset -y 1 0x01a {speed}")

# Main loop
def main():
    while True:
        cpu_temp = get_cpu_temp()
        if cpu_temp >= 50:
            set_fan_speed(0x64)  # 100%
        elif cpu_temp >= 48:
            set_fan_speed(0x40)  # 75%
        elif cpu_temp >= 44:
            set_fan_speed(0x32)  # 50%
        elif cpu_temp >= 39:
            set_fan_speed(0x10)  # 25%
        else:
            set_fan_speed(0x00)  # Fan off
        
        time.sleep(30)

if __name__ == "__main__":
    main()
