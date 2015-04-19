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

def saveToDatabase(temperature,humidity):

	con=mdb.connect("localhost", databaseUsername, databasePassword, databaseName)
        currentDate=datetime.datetime.now().date()

        now=datetime.datetime.now()
        midnight=datetime.datetime.combine(now.date(),datetime.time())
        minutes=((now-midnight).seconds)/60 #minutes after midnight, use datead$


        with con:
                cur=con.cursor()

                cur.execute("INSERT INTO temperatures (temperature,humidity, dateMeasured, hourMeasured) VALUES (%s,%s,%s,%s)",(temperature,humidity,currentDate, minutes))

		print "Saved temperature"
		return "true"


def readInfo():
	temperatureSaved="false" #keep on reading till you get the info

	while(temperatureSaved=="false"):
  	# Run the DHT program to get the humidity and temperature readings!

	  	output = subprocess.check_output(["/home/pi/myweather/wetter.py"]);
  		print output
  		matches = re.search("Temp =\s+([-]?[0-9.]+)", output)
  		if (not matches):
			time.sleep(3)
			continue
	  	temp = float(matches.group(1))

  		# search for humidity printout
  		matches = re.search("Press =\s+([0-9.]+)", output)
  		if (not matches):
			time.sleep(3)
			continue
  		humidity = float(matches.group(1))
		#humidity=str(humidity)+"%"

  		print "Temperature: %.1f C" % temp
  		print "Pressure:    %s %%" % humidity

		return saveToDatabase(temp,humidity)

#check if table is created or if we need to create one
try:
	queryFile=file("createTable.sql","r")

	con=mdb.connect("localhost", databaseUsername,databasePassword,databaseName)
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
