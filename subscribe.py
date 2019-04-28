import os
import time
import paho.mqtt.client as mqtt
import testhiveDBscript as database

#hardcoded data used in this prototype
broker="192.168.0.157"
test = "TestHive/#"
#Subscribing to everything
mqtt_topics = [test]
mqtt_broker_ip = broker
client = mqtt.Client()


# These functions handle what happens when the MQTT client connects
# to the broker, and what happens then the topic receives a message
def on_connect(client, userdata, flags, rc):
    print "Connected!", str(rc)
    for topic in mqtt_topics:
        client.subscribe(topic)

#seperating each message in the queue by topic, and then sending it to the database
def on_message(client, userdata, msg):
	if msg.topic == "TestHive/Weight/Weight1": #Weight data
		print("Weight: " + str(msg.payload))
		database.upload_to_db('weight', str(msg.payload))
	elif msg.topic == "TestHive/Temperature/Temp1": #Temperature 1 data
		print("Temp1: " + str(msg.payload))
		database.upload_to_db('Temperature1', str(msg.payload))
	elif msg.topic == "TestHive/Temperature/Temp2": #Temperature 2 data
		print("Temp2: " + str(msg.payload))
		database.upload_to_db('Temperature2', str(msg.payload))
	elif msg.topic == "TestHive/Humidity/Humi1": #Humidity data
		print("Humidity: " + str(msg.payload))
		database.upload_to_db('Humidity', str(msg.payload))
	elif msg.topic == "TestHive/Gyroscope/AxisZ": #Gyroscope data
		print("Gyro:AxisX: " + str(msg.payload))
		database.upload_to_db('Gyroscope/AxisZ', str(msg.payload))
	elif msg.topic == "TestHive/Gyroscope/AxisY":
		print("Gyro:AxisZ: " + str(msg.payload))
		database.upload_to_db('Gyroscope/AxisY', str(msg.payload))
	elif msg.topic == "TestHive/Gyroscope/AxisX":
		print("Gyro:AxisY: " + str(msg.payload))
		database.upload_to_db('Gyroscope/AxisX', str(msg.payload))
	elif msg.topic == "TestHive/Gyroscope/AxisZ":
		print("Gyro:AxisX: " + str(msg.payload))
		database.upload_to_db('Gyroscope/AxisX', str(msg.payload))
	elif msg.topic == "TestHive/Accelerometer/AxisZ": #Accelerometer data
		print("Accel:AxisZ: " + str(msg.payload))
		database.upload_to_db('Accelerometer/AxisZ', str(msg.payload))
	elif msg.topic == "TestHive/Accelerometer/AxisY":
		print("Accel:AxisY: " + str(msg.payload))
		database.upload_to_db('Accelerometer/AxisY', str(msg.payload))
	elif msg.topic == "TestHive/Accelerometer/AxisX":
		print("Accel:AxisX: " + str(msg.payload))
		database.upload_to_db('Accelerometer/AxisX', str(msg.payload))
	elif msg.topic == "TestHive/Barometer/Barometer1":
		print("Barometer: " + str(msg.payload))
		database.upload_to_db('Barometer', str(msg.payload))

#   elif msg.topic == "motion":
#	print "5"
#   print "Topic: ", msg.topic + "\nMessage: " + str(msg.payload) 

#Initialise the above connection and message definitions
client.on_connect=on_connect
client.on_message=on_message

#Connect to broker on port 1883
client.connect(broker, 1883)

#Let it run until interrupted
client.loop_forever()
client.disconnect()

