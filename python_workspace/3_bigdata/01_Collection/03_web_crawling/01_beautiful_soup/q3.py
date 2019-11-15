import RPi.GPIO as GPIO
import time

pin_pwm = 18
frequency = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_pwm, GPIO.OUT)

p = GPIO.PWM(pin_pwm, frequency)
p.start(7.5)

p.ChangeDutyCycle(2.5)
time.sleep(3)
p.ChangeDutyCycle(7.5)
time.sleep(3)
p.ChangeDutyCycle(11)
time.sleep(3)

GPIO.cleanup()