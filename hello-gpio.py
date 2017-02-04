from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
from time import sleep
global my_pwm

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)


@app.route("/")
def hello():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H-%M")
	templateData = {
		'title': 'Hello',
		'time': timeString
	}
	return render_template('main.html', **templateData)


@app.route("/lede")
def lede():
	GPIO.setup(10, GPIO.OUT)
	
	my_pwm = GPIO.PWM(10,100)

	my_pwm.start(100)
	sleep(3)
	my_pwm.ChangeDutyCycle(50)
	sleep(3)
	my_pwm.ChangeDutyCycle(10)
	sleep(3)
	my_pwm.stop()
	
	return "ON"

@app.route("/ledd")
def ledd():
	GPIO.setup(10, GPIO.OUT)
	GPIO.output(10 , 0)
	return "OFF"

@app.route("/leds/<status>")
def leds(status):
	GPIO.setup(10, GPIO.OUT)
	
	my_pwm = GPIO.PWM(10,100)

	my_pwm.start(100)
	print status
	sleep(3)
	my_pwm.ChangeDutyCycle(int(status))
	sleep(3)
	return "OK"

@app.route("/ledp/<status>")
def ledp(status):
	print status
	GPIO.setup(10, GPIO.OUT)
	GPIO.output(10, int(status))
	
	return "OK"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)