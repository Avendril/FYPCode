import Adafruit_BMP.BMP085 as BMP085
import time

def Pressure_Read():
	while True:
		sensor = BMP085.BMP085()
		pressure = sensor.read_pressure()
		stringPressure = str(pressure)
		time.sleep(1)
		return stringPressure
