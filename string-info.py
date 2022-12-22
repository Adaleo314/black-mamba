#!/usr/bin/env python3.7

#message from user
message = input("Enter a message: ")

#printing out first and last character

print("First Character: ", message[0])
print("Last Character: ", message[-1])

#middle character

print("Middle Character: ", message[int(len(message) / 2)])

#even and odd characters

print("Even Index Characters:", message[0::2])
print("Odd Index Characters:", message[1::2])

#reverse the string

print("Reversed Message:", message[::-1])

#Split and Join

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
