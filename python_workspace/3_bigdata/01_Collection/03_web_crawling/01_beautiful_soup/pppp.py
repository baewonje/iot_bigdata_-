import RPi.GPIO as GPIO
import time

pin_pwm = 18
frequency = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_pwm, GPIO.OUT)

p = GPIO.PWM(pin_pwm, frequency)
p.start(5)

p.ChangeDutyCycle(5)
time.sleep(1)
p.ChangeDutyCycle(10)
time.sleep(1)

,
 

GPIO.cleanup()

print("asd")