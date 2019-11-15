from socket import *
import bluetooth
import RPi.GPIO as GPIO
import time
import threading
import ctypes

# client_socket3 = BluetoothSocket(RFCOMM)
# client_socket3.connect(("B8:27:EB:29:9A:57",3))

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER =  18
GPIO_ECHO =  21
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_socket.bind(("B8:27:EB:E3:8B:7D",port))
server_socket.listen(1)

pin_pwm = 23
frequency = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_pwm, GPIO.OUT)

p = GPIO.PWM(pin_pwm, frequency)
p.start(7.5)

client_socket, address = server_socket.accept()
print("Accepted connection from", address)


def terminate_ai_mode():
    if not ai_scheduler.isAlive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def Ultrasonic_sensor():
    print("Ultrasonic Distance Measurement")

    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    try:
        while True:
            stop = 0
            start = 0
            GPIO.output(GPIO_TRIGGER, False)
            time.sleep(2)

            GPIO.output(GPIO_TRIGGER, True)
            time.sleep(0.00001)
            GPIO.output(GPIO_TRIGGER, False)

            while GPIO.input(GPIO_ECHO) == 0:
                start = time.time()

            while GPIO.input(GPIO_ECHO) == 1:
                stop = time.time()

            elapsed = stop - start

            if (stop and start):
                distance = (elapsed * 34000.0) / 2
                print("Distance : %.1f cm" % distance)
                if distance < 30:
                    pass
                    # client_socket3.send('start')
                    # server_socket.send("start")

    except KeyboardInterrupt:
        print("Ultrasonic Distance Measurement End")


while 1:

    data = client_socket.recv(1024)
    data = data.decode('utf-8')
    print("Received:%s" % data)

    if (data == "q"):
        print("quit")
        GPIO.cleanup()
        while ai_scheduler.is_alive():
            try:
                terminate_ai_mode()
            except:
                pass
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
    elif (data == "7"):
        ai_scheduler = threading.Thread(target=Ultrasonic_sensor)
        ai_scheduler.daemon = True
        ai_scheduler.start()
        print("good")

    elif (data == "8"):
        while ai_scheduler.is_alive():
            try:
                terminate_ai_mode()
            except:
                pass
        print("good!!")

GPIO.cleanup()
client_socket.close()
server_socket.close()

