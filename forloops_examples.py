
#Python For Loops
#For Loops count from beginning of index to end

#while statements
count = 1

while count <= 4:
    print("looping")
    count += 1
    
#for statements
#for TEMP_VARIABLE in SEQUENCE
colors = ['blue', 'green', 'red', 'purple']

for color in colors:
    print(color)
    
#for loops in dictionaries    
ages = {'adam':35, 'mike':28, 'bill':17}
for key in ages:
    print(key)
for key, value in ages.items():
    print(key, value)

#for loop with a string
strings = "Happy Birthday"
for x in strings:
    print(x)


#nesting loops and conditionals
#counter is less than 25 & divisible by 4, print it, otherwise add 1 until 
# it equals 25
counter = 1
while counter <= 25:
    if counter % 4 == 0:
        print(counter)
    counter += 1
    
#break and continue with loops
#break will stop the loop
#continue will skip the current iteration of the loop
#this will count 3,5,7,9
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}")
    count += 1
    
#break will stop entire loop
#this will only count to 1 
count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"We're counting numbers: {count}")
    count += 1
    
#else with loops
for i in [1, 2, 3, 4, 5,]:
    print(i)
else:
    print("For loop completed")  
    
#break in loop    

colors = ['red', 'pink', 'blue,', 'orange', 'green']
for color in colors:
   if color == 'orange':
       print("Orange is in the list")
       break
else:
    print("Orange is not in the list")

#using ranges (do not need counter at end)
for x in range(10):
    print("looping")
    
    
#list comprehensions (list of changes at end)
colors = ['red', 'blue', 'orange', 'green', 'yellow']

#items before the "for" are ones to be processed
#items after the "for" each item in list
uppercase_colors = [color.upper() for color in colors]
print(uppercase_colors)    

#get me each color for colors variable, if that color is 
#red, orange, or yellow, to create warm_colors variable  
warm_colors = [color for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors)
    