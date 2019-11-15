import bluetooth
import RPi.GPIO as GPIO
import time

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_socket.bind(("B8:27:EB:E3:8B:7D",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print("Accepted connection from",address)



while 1:
    data = client_socket.recv(1024)
    data = data.decode('utf-8')
    print("Received:%s" % data)
    if (data == "q"):
        print("quit")
        break

client_socket.close()
server_socket.close()