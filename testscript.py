from influxdb import InfluxDBClient

json_body = [
    {
        "measurement": "cpu",
        "tags": {
            "host": "serverA",
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 31
        }
    }
]

client = InfluxDBClient('192.168.237.128', 8086, 'admin', 'admin', 'statsdemo')
client.write_points(json_body)
result=client.query('select value from cpu;')
print("Result: {0}".format(result))
