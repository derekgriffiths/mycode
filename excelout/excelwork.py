#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

col3 = input("\nWhat would you like the column 3 header to be? ")
col4 = input("What would you like the column 4 header to be? ")

# Request data from user
def get_ip_data():
    input_ip = input("What is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    input_col3 = input("What " + col3 + " value do you want to enter? ")
    input_col4 = input("What " + col4 + " value do you want to enter? ")

    d = {"IP": input_ip, "driver": input_driver, col3:input_col3, col4:input_col4}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}] {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")


# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue, or  enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")
if filename.endswith(".xls"):
    try:
        print(filename + "shouldn't end in xls.  Pls try again.")
    except:
        break
elif  # I left off here



pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")

