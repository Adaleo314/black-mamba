"""
Using Python Generators
"""

#Define the 'char_range' generator here
def char_range(start, stop, step=1):
    start_code = ord(start)
    yield start
    



#Tests to verify the implementation of char_range
# * Do not Modify
##################################################

#Ensure the 'char_range' is a generator function
from inspect import isgeneratorfunction

assert isgeneratorfunction(char_range), f"Expected char_range to be a generator function but was not."

