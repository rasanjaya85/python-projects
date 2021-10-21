import requests

BASE = "http://127.0.0.1:5000/"

#data = [{'name': 'How to make REST API', 'views': 50000, 'likes': 1000},
#		{'name': 'How to make Flask app', 'views': 90000, 'likes': 1500},
#		{'name': 'Make Django with MySql ', 'views': 10000, 'likes': 19000}]
#
#for i in range(len(data)):
#	response = requests.put(BASE + "video/" + str(i), data[i])
#	print(response.json())
#
#input()
response = requests.get(BASE + "video/2")
print(response.json())
#input()
#response = requests.patch(BASE + "video/2", {'likes' : 50})
#print(response.json())
input()
response = requests.delete(BASE + "video/2")
print(response)