import socket
import sys
import os

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except(socket.error, msg):
    print("Failed to create socket. Error code : " + str(msg[0]) + ", Error message : " + msg[1])
    sys.exit()

print("Socket created!")

host = "Triptane"
port = 9100
remote_ip = "15.74.42.136"

print('Ip address of ' + host + ' is ' + remote_ip)

s.connect((remote_ip , port))
print('Socket Connected to ' + host + ' on ip ' + remote_ip)

## message = "GET / HTTP/1.1\r\n\r\n"
file_path = "C:\\Users\\zhangjuh\\Desktop\\"
file_name = "mayin.jpg"
print(file_path)
file_size = os.path.getsize(file_path + file_name)

fp = open(file_path + file_name, 'rb')
file_data = fp.read(file_size)

try :
	#Set the whole string
    s.send(file_data)
except socket.error:
    #Send failed
    print('Send failed')
    sys.exit()