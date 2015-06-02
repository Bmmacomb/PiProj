#pressure sensor import
import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()
# import time
from datetime import datetime
#humidity sensor import
import HTU as Humidity
#therm sensor import
import thermomiter as therm
ther = therm.read_temp()
thermC = ((ther-32)*5)/9
Hum = Humidity.Humid()
press = sensor.read_pressure()
alt = sensor.read_altitude()
SeaPress = sensor.read_sealevel_pressure()
dewpt = thermC-((100-Hum)/5)
dewpt = (((dewpt * 9)/5)+32)
f = open('dataFile.txt', 'a')
x = datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' '  '{:0.2f} {:0.2f} {:0.2f} {:0.2f} {:0.2f} {:0.2f}'.format(Hum,ther,press,alt,SeaPress,dewpt) 
print 'Humidity = {0:0.2f}%'.format(Hum)
print 'Temperature = {0:0.2f} F'.format(ther)
print 'Pressure = {0:0.2f} Pa'.format(press)
print '------------------------'
print 'the following are inexact:'
print ' '
print 'Altitude = {0:0.2f} m'.format(alt)
print 'Sealevel Pressure = {0:0.2f} Pa'.format(SeaPress)
print 'dewpoint = {0:0.2f}'.format(dewpt)
f.write(x+'\n')

