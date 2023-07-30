#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('cls', shell=True)

# Ask for input
remoteServer = input("macbook-pro")
# remoteServer = input("192.168.1.85") right now neither are working
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()



# Using the range function to specify ports

#changing the port numbers to scan
for port in range(1, 1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #setting up the timeout to be half a second
    sock.settimeout(0.5)
    result = sock.connect_ex((remoteServerIP, port))
    if result == 0:
        print ("Port {}: 	 Open".format(port))
    sock.close()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print('Scanning Completed in: ', total)