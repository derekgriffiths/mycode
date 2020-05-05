#!/usr/bin/env python3

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# if user set IP of gateway

if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk != "192.168.70.1": # if any data is provided other than the 192 IP address, this will test true
   print("Looks like the IP address was set: " + ipchk) # indented under if
else: # if data is NOT provided
   print("You did not provide input.") # indented under else

