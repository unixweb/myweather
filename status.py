#!/usr/bin/python

import Adafruit_BMP.BMP085 as BMP085

# Default constructor will pick a default I2C bus.
#
# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
# from the main GPIO header and the library will figure out the bus number based
# on the Pi's revision.
#
# For the Beaglebone Black the library will assume bus 1 by default, which is
# exposed with SCL = P9_19 and SDA = P9_20.
#sensor = BMP085.BMP085()

# Optionally you can override the bus number:
#sensor = BMP085.BMP085(busnum=2)

# You can also optionally change the BMP085 mode to one of BMP085_ULTRALOWPOWER,
# BMP085_STANDARD, BMP085_HIGHRES, or BMP085_ULTRAHIGHRES.  See the BMP085
# datasheet for more details on the meanings of each mode (accuracy and power
# consumption are primarily the differences).  The default mode is STANDARD.
sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

# Please set your locale altitude 
# http://www.latlong.net/  Helps to find your Langitude and Latitude
# http://www.mapcoordinates.net/  Helps to Find the Data in Meter 
locale_altitude = 570


seapFloat = sensor.read_sealevel_pressure(locale_altitude)
pressure = sensor.read_pressure()
psea = pressure / pow(1.0 - locale_altitude/44330.0, 5.255)

print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude(seapFloat))
print 'Pressure = {0:0.2f} hPa'.format(sensor.read_pressure()/100)
print "Pressure NN =%8.2f hPa" % (psea / 100.0)
