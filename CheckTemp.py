import Adafruit_DHT
import time

sensor=Adafruit_DHT.DHT11
gpio=4
dir='/home/pi/TempMonitor'
while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
	# print('Reading done', flush=True)
	if humidity is not None and temperature is not None:
		print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity), flush=True)
		ft = open('{0}/temp.now'.format(dir), 'w')
		ft.writelines('{0:0.1f}'.format(temperature))
		ft.close()

		fh = open('{0}/hum.now'.format(dir), 'w')
		fh.writelines('{0:0.1f}'.format(humidity))
		fh.close()
	else:
		print('Failed to get reading. Try again!', flush=True)
	time.sleep(5)
