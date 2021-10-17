#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Rasanjaya Subasinghe
# Created Date: Sun October 17 19:32:00 PDT 2021
# =============================================================================
"""The script has been crate for chat room"""

import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
	for client in clients:
		client.send(message)


def handle(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f'{nickname} left the chat.'.endcode('ascii'))
			nicknames.remove(nickname)
			break


def receive():
	print('sssss')
	while True:
		client, address = server.accept()
		print(client, address)
		print(f'Connected with the {str(address)}')

		client.send("NICK".encode('ascii'))
		nickname = client.recv(1024).decode('ascii')
		nicknames.append(nickname)
		clients.append(client)

		print(f'Nickname of the client is {nickname}!')	
		broadcast(f'{nickname} joined the chat!'.encode('ascii'))
		client.send(f'Connected to the server!'.encode('ascii'))

		thread = threading.Thread(target=handle, args=(client, ))
		thread.start()

receive()