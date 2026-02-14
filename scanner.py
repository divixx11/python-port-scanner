#!/bin/python3
'''This is called a shebang.
It tells Linux to run the script using Python 3 when executed directly.'''

import sys  # Allows us to enter command line arguments
import socket  # Used for network communication,connecting to ports, getting IP addresses
from datetime import datetime  # Used to print the current time

# Define our target
if len(sys.argv) == 2:  # If user gives exactly 1 argument then continue 
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

''' It’s the starting template of a port scanner. Right now it: Accepts an IP, Prints scan info, Shows start time '''

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #This creates a TCP socket, AF_INET = IPv4 and socket.SOCK_STREAM = TCP Protocol | Therefore this is a virtual network cable 
        socket.setdefaulttimeout(1)  #This means if connection takes more than 1 second then give up.| We use socket inside loop because each port needs a fresh TCP connection
        result = s.connect_ex((target, port))  #It tries to connect to (target IP, Port No), Internally the computer tries to perform a TCP Handshake and 0 mean success | connect_ex() = returns error code insteade of crashing and it performs full TCP connection scan 
        print("Checking port {}".format(port))
        
        if result == 0:
            print("Port {} is open".format(port))

        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()





