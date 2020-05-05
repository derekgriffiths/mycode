#!/usr/bin/env python3

# creating a small string

lilstring = "Alta3 Research offers classes on Python coding"

newlist = lilstring.split(" ") # this turns lilstring into a list

print(newlist)

# creating a list of strings

myiplist = ["192", "168", "0", "12"]

#Now set singleip as the result of joining the list myiplist around the "."

singleip = ".".join(myiplist)

#displays the singleip

print(singleip)
