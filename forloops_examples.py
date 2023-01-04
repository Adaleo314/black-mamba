
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

    