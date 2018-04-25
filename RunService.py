from flask import Flask
from flask import request
app = Flask(__name__)

dir = '/home/pi/TempMonitor'
@app.route("/")
def index():
	f_temp = open('{0}/temp.now'.format(dir), 'r').readlines()[0].strip()
	f_hum = open('{0}/hum.now'.format(dir), 'r').readlines()[0].strip()
	html_para = "Humidity: {0}\nTemperature: {1}".format(f_hum, f_temp)
	return "<html><body><h1>Flask Service on Temperature and Humidity</h1><h3>{0}</h3</body></html>".format(html_para)

@app.route('/service')
def service():
	if request.args.get('measure') == 'temperature':
		return open('{0}/temp.now'.format(dir), 'r').readlines()[0].strip()
	elif request.args.get('measure') == 'humidity':
		return open('{0}/hum.now'.format(dir), 'r').readlines()[0].strip()
	else:
		return 'Unsupported operation'

if __name__ == "__main__":
	app.run(host='192.168.3.250')
