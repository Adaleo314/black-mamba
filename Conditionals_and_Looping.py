#basic conditions to be run in REPL

#if statement basics. not true, nothing prints
if 'a' < 'b':
    print("Condition was true")
    
#is, else basic if false or if true
if False:
    print("Was true")
else:
    print("Was false")
    
#elif is else if statements
if 'b' < 'a':
    print("This is true")
elif 'c' < 'd':
    print("Second condition is true")
else:
    print("No conditional was true")    
    
#Learning more conditionals
name = input("What is your name? ")

if len(name) >= 6:
    print("Your name is long")
elif len(name) == 5:
    print("Your name is 5 characters")
elif len(name) >= 4:
    print("Your name us 4 or more characters")
else:
    print("Your name is short")

#if no other if statements, replace if with "pass" under else:
    
#if no other if statements, replace if with "pass" under else:    
