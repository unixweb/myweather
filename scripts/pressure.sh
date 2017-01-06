PRESS1=`python /home/pi/myweather/pressure.py`

mosquitto_pub -h mqtt.unixweb.de -p 1883  -t abcde/p1 -m $PRESS1
