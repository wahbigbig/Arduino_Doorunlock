#!/usr/bin/env python

import requests
import bluetooth
import time

server_address = "http://10.1.1.3:3000" 
bd_addr = "30:14:12:04:30:52" 
port = 1
sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
sock.connect((bd_addr,port))
 
while 1:
	r = requests.get(server_address + "/status")
	if r.content == "1":
		print "unlock"
		requests.get(server_address + "/lock")
		sock.send("1")
	else:	
		print "nothing to do"
	time.sleep(1)
 
sock.close()
