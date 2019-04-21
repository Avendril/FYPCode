import os
import time
import paho.mqtt.client as mqtt
#from influxdb import InfluxDBClient as influx

broker="192.168.0.157"
test = "TestHive/#"
temperature1 = "TestHive/Temperature/Temp1"
temperature2 = "TestHive/Temperature/Temp2"
humidity1 = "TestHive/Humidity/Humi1"
weight1 = "TestHive/Weight/Weight1"
gyrox = "TestHive/Gyroscope/AxisX"
gyroy = "TestHive/Gyroscope/AxisY"
gyroz = "TestHive/Gyroscope/AxisZ"
accelx = "TestHive/Accelerometer/AxisX"
accely = "TestHive/Accelerometer/AxisY"
accelz = "TestHive/Accelerometer/AxisZ"
barometer = "TestHive/Barometer/Baro1"
gasSensor = "TestHive/GasSensor/gas1"

mqtt_topics = [test, weight1, humidity1]
mqtt_broker_ip = broker
client = mqtt.Client()


# These functions handle what happens when the MQTT client connects
# to the broker, and what happens then the topic receives a message
def on_connect(client, userdata, flags, rc):
    print "Connected!", str(rc)
    for topic in mqtt_topics:
        client.subscribe(topic)

def on_message(client, userdata, msg):
    if msg.topic == "TestHive/Weight/Weight1":
	print("Weight: " + str(msg.payload))
    elif msg.topic == "TestHive/Temperature/Temp1":
	print("Temp1: " + str(msg.payload))
    elif msg.topic == "TestHive/Temperature/Temp2":
	print("Temp2: " + str(msg.payload))
    elif msg.topic == "TestHive/Humidity/Humi1":
	print("Humidity: " + str(msg.payload))
    elif msg.topic == "motion":
	print "5"
 #   print "Topic: ", msg.topic + "\nMessage: " + str(msg.payload) 

#Initialise the above connection and message definitions
client.on_connect=on_connect
client.on_message=on_message

#Connect to broker on port 1883
client.connect(broker, 1883)

#Let it run until interrupted
client.loop_forever()
client.disconnect()

