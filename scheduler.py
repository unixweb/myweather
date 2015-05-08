#!/usr/bin/python

import subprocess
import re
import os
import sys
import time
import MySQLdb as mdb
import datetime

databaseUsername="XXXX"
databasePassword="XXXX"
databaseName="XXXX" #do not change unless you named the Wordpress database with some other name
databaseHost="XXXXX.domain.de"


idef saveToDatabase(temp1, temp2, temp3, temp4, humidity, pressure, sea_pressure, altitude):

    con=mdb.connect("blog.joachimhummel.de", databaseUsername, databasePassword, databaseName)
    currentDate=datetime.datetime.now().date()
    print currentDate
    now=datetime.datetime.now()
    midnight=datetime.datetime.combine(now.date(),datetime.time())
    minutes=((now-midnight).seconds)/60 #minutes after midnight, use datead$


    with con:
            cur=con.cursor()
            query = ("INSERT INTO `temperatures2`(`temperature-1`, `temperature-2`, `temperature-3`, `temperature-4`, `humidity`, `dateMeasured`, `hourMeasured`, `pressure`, `pressure-sea`, `altitude`)"
                        "VALUES (%s,%s,%s,%s,%s,'%s',%s,%s,%s,%s)"% (temp1, temp2, temp3, temp4, humidity, currentDate, minutes, pressure, sea_pressure, altitude))
            cur.execute(query)

    print "Saved temperature"
    return "true"


def readInfo():
    temperatureSaved="false" #keep on reading till you get the info

    while(temperatureSaved=="false"):
    # Run the DHT program to get the humidity and temperature readings!

        source = "/home/pi/dev/krishwebs/myweather/weather.py"

        # search for tempretures , continue to search untill it do not found
        temp1 = search_attr('Temp1', source)
        temp2 = search_attr('Temp2', source)
        temp3 = search_attr('Temp3', source)
        temp4 = search_attr('Temp4', source)

"scheduler.py" 108 lines, 3613 characters

        print "Temperature-1: %.1f C" % temp1
        print "Temperature-2: %.1f C" % temp2
        print "Temperature-3: %.1f C" % temp3
        print "Temperature-4: %.1f C" % temp4
        print "Humidity:    %s %%" % humidity
        print "Pressure:    %s %%" % pressure
        print "Pressure-Sea: %s %%" % sea_pressure
        print "Altitude:    %s ft" % altitude
        return saveToDatabase(temp1, temp2, temp3, temp4, humidity, pressure, sea_pressure, altitude)


def search_attr(val, source):
    output = subprocess.check_output([source]);
    matches = re.search(("%s =\s+([-]?[0-9.]+)" % val), output)
    if (not matches):
        print "searching for %s"% (val)
        time.sleep(3)
        search_attr(val, source)
    return float(matches.group(1))

#check if table is created or if we need to create one
try:
    queryFile=file("createTable.sql","r")

    con=mdb.connect("blog.joachimhummel.de", databaseUsername,databasePassword,databaseName)
    currentDate=datetime.datetime.now().date()

    with con:
        line=queryFile.readline()
        query=""
        while(line!=""):
            query+=line
            line=queryFile.readline()

        cur=con.cursor()
        cur.execute(query)

            #now rename the file, because we do not need to recreate the table everytime this script is run
        queryFile.close()
        os.rename("createTable.sql","createTable.sql.bkp")


except IOError:
    pass #table has already been created

status="false"
while(status!="true"):

    status=readInfo()
