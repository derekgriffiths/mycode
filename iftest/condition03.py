#!/usr/bin/env python3

# Asking user for input to define the hostname
hostname = input("What value should we set for hostname?")

## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("Hostname matches expected config") # Added a second line to output if the user enters the matches text

# Output at the end of the script every time
print("Exiting the script")

