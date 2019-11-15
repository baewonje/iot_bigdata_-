from socket import *
import bluetooth
import RPi.GPIO as GPIO
import time
import threading
import ctypes

# client_socket3 = BluetoothSocket(RFCOMM)
# client_socket3.connect(("B8:27:EB:29:9A:57",3))

GPIO.setmode(GPIO.BCM)
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
0
port = 1
server_socket.bind(("B8:27:EB:E3:8B:7D",port))
server_socket.listen(1)

pin_pwm = 18
frequency = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_pwm, GPIO.OUT)

p = GPIO.PWM(pin_pwm, frequency)
p.start(7.5)

client_socket, address = server_socket.accept()
print("Accepted connection from", address)


while 1:

    data = client_socket.recv(1024)
    data = data.decode('utf-8')
    print("Received:%s" % data)

    if (data == "q"):
        print("quit")
        GPIO.cleanup()
        break
    elif (data == "1"):
        print('1111111111')
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
    elif (data == "2"):
        p.ChangeDutyCycle(4)
        time.sleep(1)
    elif (data == "3"):
        p.ChangeDutyCycle(6)
        time.sleep(1)
    elif (data == "4"):
        p.ChangeDutyCycle(8)
        time.sleep(1)
    elif (data == "5"):
        p.ChangeDutyCycle(10)
        time.sleep(1)
    elif (data == "6"):
        p.ChangeDutyCycle(11.9)
        time.sleep(1)


GPIO.cleanup()
client_socket.close()
server_socket.close()

