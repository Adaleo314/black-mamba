name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))

#NAME is AGE years old and loves the color COLOR.
#on 3 lines 

print(name)
print("is " + str(age) + "years old")
print("and loves the color " + color + ".")

#Same on 1 line

print(name, end=" ")
print("is " + str(age) + " years old", end=" ")
print("and loves the color " + color + ".", end=" ")

#Code and output on 1 line including separator

print(name, 'is', age, 'years old and loves the color', color + '.', sep="$")
