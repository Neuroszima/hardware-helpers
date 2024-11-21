import pyvisa
from pyvisa.resources.usb import USBInstrument
from pyvisa.resources.resource import Resource
from time import sleep, time
from matplotlib import pyplot as plt

rm = pyvisa.ResourceManager()
p = rm.list_resources()
print(p)

connection: USBInstrument | Resource = rm.open_resource(p[0])
info = connection.query("*IDN?")
print(info)
connection.write("SENSE:VOLT:DC:RANG 10")
connection.write("SENSE:VOLT:DC:NPLC 0.6")

voltage_readings = []
timeline = []
start = time()

for i in range(200):
    voltage = connection.query("READ?")
    timestamp = time() - start
    voltage_readings.append(float(voltage))
    timeline.append(round(timestamp, 3))
    sleep(0.02)

connection.close()

print([(voltage, t) for voltage, t in zip(voltage_readings, timeline)])
plt.plot(timeline, voltage_readings)
plt.show()

