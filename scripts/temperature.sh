TEMP=`python /home/pi/myweather/temperature.py |head -1`

mosquitto_pub -h mqtt.unixweb.de -p 1883  -t abcde/temp1 -m $TEMP
