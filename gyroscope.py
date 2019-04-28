from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)

#Testing code to check if the data is being recieved.
#while True:
#	gyro_data = sensor.get_gyro_data()
#	x = str(gyro_data['x'])
#	print(x)
#Accelerometer Readings functions
def Accelerometer_Read_X():
	while True:
		accel_data = sensor.get_accel_data()
		x = str(accel_data['x'])
		return x

def Accelerometer_Read_Y():
        while True:
                accel_data = sensor.get_accel_data()
                y = str(accel_data['y'])
		return y

def Accelerometer_Read_Z():
        while True:
                accel_data = sensor.get_accel_data()
                z = str(accel_data['z'])
                return z


#Gyroscope Readings functions
def Gyroscope_Read_X():
	while True:
		gyro_data = sensor.get_gyro_data()
        	a = str(gyro_data['x'])
		return a

def Gyroscope_Read_Y():
        while True:
                gyro_data = sensor.get_gyro_data()
                b = str(gyro_data['y'])
                return b


def Gyroscope_Read_Z():
        while True:
                gyro_data = sensor.get_gyro_data()
                c = str(gyro_data['z'])
                return c


#Temperature Readings functions
def Temperature_Read_MPU():
	while True:
		temp =str(sensor.get_temp())
		return temp
