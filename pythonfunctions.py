#!usr/bin/env python3.7

#1. Write a 'split_name' function that takes a string and returns a dictionary with first_name last_name.

def split_name(name):
    first_name, last_name = name.split(maxsplit=1)
    return {'first_name': first_name, 'last_name': last_name}
    
assert split_name('Kevin Bacon') == {'first_name': 'Kevin', 'last_name': 'Bacon'}


#2. Ensure the 'split_name' can handle multi-word names. (Add maxsplit of 1 to only split the name once.)

assert split_name('Victor Von Doom') == {'first_name': 'Victor', 'last_name': 'Von Doom'}


#3 Write an 'is_palindome' function to check if a string is a palidrome 

def is_palindrome(item):
    item = str(item)
    return item == item[::-1]
    
assert is_palindrome('hannah') == True
assert is_palindrome('adam') == False
    
#4 Make 'it_plaindrome' function work with numbers

assert is_palindrome(101) == True
assert is_palindrome(10) == False


#5 Write a 'build_list' function that takes an items and a number to include in a list
def build_list(item, count=1):
    items = []
    for x in range(count):
        items.append(item)
    return(items)    
    
assert build_list('Apple', 3) == ['Apple', 'Apple', 'Apple']
assert build_list('Orange', 1) == ['Orange']

