#! /usr/local/bin/python3

import threading
import socket

nickname = input('Choose the nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == "NICK":
				client.send(nickname.encode('ascii'))
			else:
				print(message)
		except:
			print('An errorr occurred!')
			client.close()
			break
		
def write():
	while True:
		message = f'{nickname}: {input("")}'.encode('ascii')
		client.send(message)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


