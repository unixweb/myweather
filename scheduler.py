#!/usr/bin/python

import subprocess
import re
import os
import sys
import time
import MySQLdb as mdb
import datetime
from weather import *

databaseUsername="XXXXX"
databasePassword="XXXXX"
databaseName="XXXXX" #do not change unless you named the Wordpress database with some other name
databaseHost="www.xxx.de"


#check if table is created or if we need to create one
try:
    queryFile=file("createTable.sql","r")

    con=mdb.connect(databaseHost,databaseUsername,databasePassword,databaseName)
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

def saveToDatabase(temp1, temp2, temp3, temp4, humidity, pressure, sea_pressure, altitude):
    #print "SaveToDatabase Hit"

    con=mdb.connect(databaseHost, databaseUsername, databasePassword, databaseName)
    currentDate=datetime.datetime.now().date()
    print currentDate
    now=datetime.datetime.now()
    midnight=datetime.datetime.combine(now.date(),datetime.time())
    minutes=((now-midnight).seconds)/60 #minutes after midnight, use datead$
    print "Minutes",minutes

    with con:
            cur=con.cursor()
            query = ("INSERT INTO `temperatures`(`temperature_1`, `temperature_2`, `temperature_3`, `temperature_4`, `humidity`, `dateMeasured`, `hourMeasured`, `pressure`, `pressure_sea`, `altitude`)"
                        "VALUES (%s,%s,%s,%s,%s,'%s',%s,%s,%s,%s)"% (temp1, temp2, temp3, temp4, humidity, currentDate, minutes, pressure, sea_pressure, altitude))
            cur.execute(query)

    print "Saved temperature"
    return "false"


def readInfo():
    #print "ReadInfo Hit"
    temperatureSaved="false"
    while(temperatureSaved=="false"):
         temp1 = Temp1
         temp2 = Temp2
         temp3 = Temp3
         temp4 = Temp4
         humidity=Humidity
         altitude =  Altitude
         pressure =  Pressure
         sea_pressure  =  Sea_pressure
         print "Temp1 : ",temp1
         print "Temp2 : ",temp2
         print "Temp3 : ",temp3
         print "Temp4 : ",temp4
         print "Humidity : ",humidity
         print "Altitude : ",altitude
         print "Pressure : ",pressure
         print "Sea Pressure : ",sea_pressure
	 #return "false"
         #temperatureSaved="true"
         return saveToDatabase(temp1, temp2, temp3, temp4, humidity, pressure, sea_pressure, altitude)

status=readInfo()



