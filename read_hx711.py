import serial
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

"""Pico Connections
To HX711:   Pin 40 (5V) to Vcc of HX711
            Pin 38 (GND) to GND of HX711
            Pin 124(GPIO 18) to DT of HX711
            Pin 17 (GPIO 25) to SCK of HX711
            
To LCD Display: 
            Pin 40 (5V) to VCC of LCD
            Pin 38 (GND) to GND of LCD
            Pin 1 (GPIO 0) to SCL of LCD
            Pin 2 (GPIO 1) to SDA of LCD

Run this code on PC. 
Load lcd_api.pi, pico_i2c_lcd.py, hx711.py, testHX.py on to Pico. Run textHX.py

"""
# Reads the data from the serial line and plots it on a scrolling axis.

def animate(i):
    global x
    x += 1
    y_str = ser.readline()
    #print(y)
    y = float(y_str.decode('utf-8')) * scaleFactor
    data.append((x, y))
    ax.relim()
    ax.autoscale_view()

    line.set_data(*zip(*data))



ser = serial.Serial(
    port='COM6',       # Set the COM port to whatever it shows in Device Properties.
    baudrate=9600,
    timeout=1)
scaleFactor = 1
fig, ax = plt.subplots()
x = 0
y = np.random.randn()
data = deque([(x, y)], maxlen=100)
line, = plt.plot(*zip(*data), c='green')

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()