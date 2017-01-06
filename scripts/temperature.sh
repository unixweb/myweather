TEMP=`python /home/pi/myweather/tmperature.py |head -1`

mosquitto_pub -h mqtt.unixweb.de -p 1883  -t abcde/temp1 -m $TEMP
