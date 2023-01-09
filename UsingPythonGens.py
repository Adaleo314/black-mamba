"""
Using Python Generators
"""

#Define the 'char_range' generator here
def char_range(start, stop, step=1):
    start_code = ord(start)
    stop_code = ord(stop)
    for value in range(start_code, stop_code, +1, step):
        yield chr(value)
    



#Tests to verify the implementation of char_range
# * Do not Modify
##################################################

#Ensure the 'char_range' is a generator function
from inspect import isgeneratorfunction

assert isgeneratorfunction(char_range), f"Expected char_range to be a generator function but was not."

