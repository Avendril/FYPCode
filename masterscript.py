import serial
import time
import os

import ds18b20code as temperature
import humidity as humi
import gyroscope as gyro
import barometer as baro

hostname = "192.168.0.157"#rpi:192.168.0.157
temperatureQueue1 = "TestHive/Temperature/Temp1"
temperatureQueue2 = "TestHive/Temperature/Temp2"
humidityQueue = "TestHive/Humidity/Humi1"
gyroscopeQueueZ = "TestHive/Gyroscope/AxisZ"
gyroscopeQueueY = "TestHive/Gyroscope/AxisY"
gyroscopeQueueX = "TestHive/Gyroscope/AxisX"
accelerometerQueueZ = "TestHive/Accelerometer/AxisZ"
accelerometerQueueY = "TestHive/Accelerometer/AxisY"
accelerometerQueueX = "TestHive/Accelerometer/AxisX"
barometerQueue = "TestHive/Barometer/Barometer1"

print("Starting mqtt publishing")

while True:
	while True:
		#Temperature
		os.system("mosquitto_pub -h " + hostname + " -t " + temperatureQueue1 + " -m " + temperature.Read_Temp1())
		os.system("mosquitto_pub -h " + hostname + " -t " + temperatureQueue2 + " -m " + temperature.Read_Temp2() )
		#Gyroscope
		os.system("mosquitto_pub -h " + hostname + " -t " + gyroscopeQueueZ + " -m " + gyro.Gyroscope_Read_Z())
		os.system("mosquitto_pub -h " + hostname + " -t " + gyroscopeQueueY + " -m " + gyro.Gyroscope_Read_Y())
		os.system("mosquitto_pub -h " + hostname + " -t " + gyroscopeQueueX + " -m " + gyro.Gyroscope_Read_X())
		#Accelerometer
		os.system("mosquitto_pub -h " + hostname + " -t " + accelerometerQueueZ + " -m " + gyro.Accelerometer_Read_Z())
		os.system("mosquitto_pub -h " + hostname + " -t " + accelerometerQueueY + " -m " + gyro.Accelerometer_Read_Y())
		os.system("mosquitto_pub -h " + hostname + " -t " + accelerometerQueueX + " -m " + gyro.Accelerometer_Read_X())
		#Humiditiy
		os.system("mosquitto_pub -h " + hostname + " -t " + humidityQueue + " -m " + humi.Read_Humidity())
		#Barometer
		os.system("mosquitto_pub -h " + hostname + " -t " + barometerQueue + " -m " + baro.Pressure_Read())
		time.sleep(4)
