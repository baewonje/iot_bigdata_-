import RPi.GPIO as GPIO
import time

sensor = 18
led = 22

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.OUT)

print ("Waitig for sensor to settle")
time.sleep(2)
print ("Detecting motion")
GPIO.output(22, GPIO.HIGH)
while True:
	if GPIO.input(18):
		print ("Motion Deteyycted")
		GPIO.output(22, GPIO.HIGH)
		time.sleep(2)
	else:
		GPIO.output(22, GPIO.HIGH)
		print ("M")
	GPIO.output(22, GPIO.LOW)
	time.sleep(2)
