#from influxdb import InfluxDBClient
import random
import influxdb

def upload_to_db(place, sensorRead):
        readings = float(sensorRead)
        json_body = [
                {
                    "measurement": place,
                    "tags": {
                        "location": "TestHive"
                    },
                    "fields": {
                         "value": readings
                    }
                 }
            ]

	client = InfluxDBClient('localhost', 8086, 'TestHiveDB')
	client.write_points(json_body)

def upload_to_db_String(place, sensorRead):
        if sensorRead is None:
                print('No data')
        else:

                readings = sensorRead
                json_body = [
                        {
                            "measurement": place,
                            "tags": {
                                "location": "TestHive"
                            },
                            "fields": {
                                 "value": readings
                            }
                         }
                    ]

                client = InfluxDBClient('localhost', 8086, 'TestHiveDB')
                client.write_points(json_body)


#result = client.query('select * from temperature;')
#
#print("Result: {0}".format(result))


