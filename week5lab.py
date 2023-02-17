import time
import random 
import sys
import csv
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
import adafruit_bme680
import board


print(sys.argv)
start_time = int(time.time())
itime = start_time 
run_time = int(sys.argv[1]) # gets arguments from terminal, has to input after name 

file_name = 'data.csv' #saves file 
if(len(sys.argv) > 2): 
    file_name = sys.argv[2] 

print(file_name)  
file = open(file_name, 'w', newline = "")  
writer = csv.writer(file)
meta_data = ["time", "PM1.0", "PM2.5", "PM10", "temperature", "gas", "relative humility", "pressure", "altitude"]
writer.writerow(meta_data)

reset_pin = None
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.95)
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

while itime < (start_time + run_time): 
    itime = int(time.time()) # gives u the massive amount of seconds, timestamp 
    #value = random.random() #the same as grapping data from a server
    print(itime, value)
    time.sleep(1)
    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")

    i2c = board.I2C()
    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
    bme680.sea_level_pressure = 1013.25
   

    data = [itime, aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"], bme680.temperature,bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude]
    writer.writerow(data)


file.close()