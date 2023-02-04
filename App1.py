import adafruit_bme680
import time
import board

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

T = 0
while T < 10:
	t = time.time()
	print(t)
	#print("\nTemperature: %0.1f C" % bme680.temperature)
	#print("Gas: %d ohm" % bme680.gas)
	#print("Humanity: %0.1f %%" % bme680.relative_humidity)
	#print("Pressure: %0.3f hPa" % bme680.pressure)
	#print("Altitude = %0.2f meters" % bme680.altitude)
	
	time.sleep(2)
	T = T+1
	print(bme680.temperature,bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude)
	

	
