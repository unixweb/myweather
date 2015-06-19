#!/usr/bin/python

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

import Adafruit_BMP.BMP085 as BMP085

# Default constructor will pick a default I2C bus.
#
# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
# from the main GPIO header and the library will figure out the bus number based
# on the Pi's revision.
#
# For the Beaglebone Black the library will assume bus 1 by default, which is
# exposed with SCL = P9_19 and SDA = P9_20.
sensor1 = BMP085.BMP085()
sensor2 = "/sys/bus/w1/devices/w1_bus_master1/28-041470306aff/w1_slave"
sensor3 = "/sys/bus/w1/devices/w1_bus_master1/28-0414709c63ff/w1_slave"
sensor4 = ""

# Optionally you can override the bus number:
#sensor = BMP085.BMP085(busnum=2)

# You can also optionally change the BMP085 mode to one of BMP085_ULTRALOWPOWER,
# BMP085_STANDARD, BMP085_HIGHRES, or BMP085_ULTRAHIGHRES.  See the BMP085
# datasheet for more details on the meanings of each mode (accuracy and power
# consumption are primarily the differences).  The default mode is STANDARD.
#sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)


# getTemp1() method
# Sensor1 = BMP085
# Output= Temp1
def getTemp1():
     temperature1 = format(sensor1.read_temperature())
     if(temperature1==0):
         return 0
     else:
         return temperature1

# getTemp2() method
# Sensor2 = DS18B20
# Output= Temp2

def getTemp2():
        while 1:
            if sensor2:
                tempfile=open(sensor2)
                thetext=tempfile.read()
                tempfile.close()
                tempdata=thetext.split("\n")[1].split(" ")[9]
                temperature2=float(tempdata[2:])
                temperature2=temperature2/1000
		temperature2=round(temperature2, 1)
            else:
                temperature2=0
            if(temperature2==0):
                return 0
            else:
                return temperature2

# getTemp3() method
# Sensor3 = DS18B20
# Output= Temp3

def getTemp3():
        while 1:
            if sensor3:
                tempfile=open(sensor3)
                thetext=tempfile.read()
                tempfile.close()
                tempdata=thetext.split("\n")[1].split(" ")[9]
                temperature3=float(tempdata[2:])
                temperature3=temperature3/1000
		temperature3=round(temperature3, 1)
            else:
                temperature3=0
            if(temperature3==0):
                return 0
            else:
                return temperature3

# getTemp4() method
# Sensor4 = DS18B20
# Output = Temp4

def getTemp4():
        while 1:
            if sensor4:
                tempfile=open(sensor4)
                thetext=tempfile.read()
                tempfile.close()
                tempdata=thetext.split("\n")[1].split(" ")[9]
                temperature4=float(tempdata[2:])
                temperature4=temperature4/1000
		temperature4=round(temperature4, 1)
            else:
                temperature4=0
            if(temperature4==0):
                return 0
            else:
                return temperature4

# getPressure() method
# Sensor1 = BMP085
# Output = Pressure

def getPressure():
    pressure=format(sensor1.read_pressure()/100)
    pressure = round((sensor1.read_pressure()/100))
    if(pressure==0):
        return 0
    else:
        return pressure

# getSeaPressure() method
# Sensor1 = BMP085
# Output = Sea_Pressure

def getSeaPressure():
    sea_pressure = format(sensor1.read_sealevel_pressure()/100)
    sea_pressure = round((sensor1.read_sealevel_pressure()/100))
    if(sea_pressure==0):
        return 0
    else:
        return sea_pressure

# getAltitude() method
# Sensor1 = BMP085
# Output = Altitude

def getAltitude():
    altitude =  format(sensor1.read_altitude())
    altitude =  round((sensor1.read_altitude()))
    if(altitude==0):
        return 0
    else:
        return altitude

# getHumidity() method
# Sensor1 = BMP085
# Output = Humidity

def getHumidity():
    humidity= 57

    if(humidity==0):
        return 0
    else:
        return humidity

Temp1=getTemp1()
#print Temp1

Temp2=getTemp2()
#print Temp2

Temp3=getTemp3()
#print Temp3

Temp4=getTemp4()
#print Temp4

Pressure=getPressure()
#print Pressure

Sea_pressure=getSeaPressure()
#print Sea_pressure

Altitude =getAltitude()
#print Altitude

Humidity=getHumidity()
#print Humidity

