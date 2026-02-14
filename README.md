# Python Port Scanner
This is a basic TCP port scanner built using Python.

## Features
- Scans ports 50–85
- Uses TCP connect scan
- Displays open ports
- Handles exceptions
- 
## How It Works
The scanner uses Python's socket module to attempt TCP connections to target ports. If connection succeeds (connect_ex() returns 0), the port is open.

## Learning Objective
Built to understand:
- TCP handshake
- Port scanning
- Network sockets
- Basic cybersecurity reconnaissance
