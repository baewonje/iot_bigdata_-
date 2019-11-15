import bluetooth
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER =  18
GPIO_ECHO =  21
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

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
def sub_motor():

    while 1:

        data = client_socket.recv(1024)
        data = data.decode('utf-8')
        print("Received:%s" % data)

        if (data == "q"):
            print("quit")
            GPIO.cleanup()
            break
        elif (data == "1"):
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
    except KeyboardInterrupt:
        print("Ultrasonic Distance Measurement End")
        GPIO.cleanup()

    GPIO.cleanup()
client_socket.close()
server_socket.close()
