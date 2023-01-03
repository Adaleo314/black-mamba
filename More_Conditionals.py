#!/usr/bin/env python3.7

#Python implementation here

value = int(input("Enter an integer value: "))


#if integer is divisible by 5 and 3. just 3, or just 5. Other number prints integer
if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:   
    print(value)

#