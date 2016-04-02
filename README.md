# Arduino_Doorunlock
Arduino Client + Raspbarry Pi Host Doorunlock

doorlock - Nodejs Webservice for control unlock door/Python client check need to send signal to Arduino
bluetooth_relay_door.ino - Arduino client program, Bluetooth listen for signal from Raspberry Pi
unlock_door.py - Raspberry Pi Python Daemon, keep monitor Nodejs webservice for send signal to Adruino via BT
