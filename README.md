# myweather
My Weather for Raspberry Pi with BMP180 / BMP085 / DS18B20<br/>
<img src="http://blog.unixweb.de/wp-content/uploads/2015/05/bmp180.jpg">
<img src="http://blog.unixweb.de/wp-content/uploads/2015/05/BMP085.jpg"><br/>
<img src="http://blog.unixweb.de/wp-content/uploads/2015/05/ds18b20-pinout.jpg">
<img src="http://blog.unixweb.de/wp-content/uploads/2015/05/DS18B20-e1431072161767.png"><br/>

<img src="https://raw.githubusercontent.com/unixweb/myweather/master/weather-app.png"><br/>

Installation for Adafruit Python-Modules needed:<br/>
<br/>
sudo apt-get update<br/>
sudo apt-get install git build-essential python-dev python-smbus<br/>
git clone https://github.com/adafruit/Adafruit_Python_BMP.git<br/>
cd Adafruit_Python_BMP<br/>
sudo python setup.py install<br/>
<br/>
sudo apt-get install python-mysqldb<br/>
<br/>
<br/>
Insert the required database parameter in "scheduler.py" for WordPress Plugin <br/>
databaseUsername="XXXXX"<br/>
databasePassword="XXXXX"<br/>
databaseName="XXXXX" #do not change unless you named the Wordpress database with some other name<br/>
databaseHost="www.xxx.de"<br/>
Install the WordPress Plugin <br/>
<br/>
Start "./scheduler.py" manually and check if there any errors.<br/>
<br/>
vi /etc/cron.d/weather <br/>
*/15 * * * *   pi    /home/pi/myweather/scheduler.py > /dev/null<br/>
<br/>
Demo: http://blog.joachimhummel.de/category/wetter<br/>
