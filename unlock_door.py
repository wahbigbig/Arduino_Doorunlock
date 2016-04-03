#!/usr/bin/env python

import requests
import bluetooth
import time

def connectBT():
	bd_addr = "30:14:12:04:30:52" 
	port = 1
	try:
		sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
		sock.connect((bd_addr,port))
		return sock
	except bluetooth.btcommon.BluetoothError as err:
		print err
		print "BT Error, wait 5sec to retry"
		time.sleep(5)
		connectBT()	

sock = connectBT()
server_address = "http://localhost:3000" 

while 1:
	r = requests.get(server_address + "/status")
	if r.content == "1":
		print "unlock"
		requests.get(server_address + "/lock")
		try:	
			sock.send("1")
		except bluetooth.btcommon.BluetoothError:
			print "Cannot send signal, retry connect"
			sock = connectBT()
			sock.send("1")
	else:	
		print "nothing to do"
	time.sleep(1)
 
sock.close()

