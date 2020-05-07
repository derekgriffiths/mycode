#!/usr/bin/env python3

def add_(x, y):
    sum = x+y
    return sum

def sub_(x, y):
    minus = x-y
    return minus

def mult_(x, y):
    mult = x*y
    return mult

def div_(x, y):
    div = x/y
    return div

print("Pick a number:")
num1 = int(input("> "))

print("Pick a second number:")
num2 = int(input("> "))

print("What would you like to do with these two numbers?")
print("Add?  Subtract?  Multiply?  Divide?")
# usr_pref = str(input.lower("> "))
usr_pref = input("> ").lower()
# input already creates strings, so no need for str(). And .lower() goes after the input, since that is the string.

if usr_pref == "add":
     print(add_(num1, num2))
elif usr_pref == "subtract":
    print(sub_(num1, num2))
elif usr_pref == "multiply":
     print(mult_(num1, num2))
elif usr_pref == "divide":
    print(div_(num1, num2))
else:
    print("Sorry, please try again.")

