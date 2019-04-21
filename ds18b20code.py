import time

def Read_Temp1():
	while 1:
		tempfile = open("/sys/bus/w1/devices/28-03168a5dd9ff/w1_slave")
		text = tempfile.read()
		tempfile.close()

		tempdata = text.split("\n")[1].split(" ")[9]
		temperature = float(tempdata[2:])
		temperature = temperature / 1000
		BCTemp1 = str(temperature)

		return BCTemp1

def Read_Temp2():
	while 1:
		tempfile2 = open("/sys/bus/w1/devices/28-020491773725/w1_slave")
		text2 = tempfile2.read()
		tempfile2.close()

		tempdata2 = text2.split("\n")[1].split(" ")[9]
		temperature2 = float(tempdata2[2:])
		temperature2 = temperature2 / 1000
		BCTemp2 = str(temperature2)
		return BCTemp2

def Read_Temp_Both():
	while 1:
		tempfile = open("/sys/bus/w1/devices/28-03168a5dd9ff/w1_slave")
		tempfile2 = open("/sys/bus/w1/devices/28-020491773725/w1_slave")

		text = tempfile.read()
		text2 = tempfile2.read()
		tempfile.close()
		tempfile2.close()

		tempdata = text.split("\n")[1].split(" ")[9]
		tempdata2 = text2.split("\n")[1].split(" ")[9]

		temperature = float(tempdata[2:])
		temperature2 = float(tempdata2[2:])

		temperature = temperature / 1000
		temperature2 = temperature2 / 1000
		BCTemp1 = str(temperature)
		BCTemp2 = str(temperature2)

		time.sleep(1)

		return BCTemp1,BCtemp2
