import random 
import string
import sys

#Generate a 6 character code of lowercase letters and numbers
def generated_name(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
    

print("**EC2 Name Generator Designed for Marketing, Accounting, & FinOps ONLY**") 

#verify users work in appropriate departments        
verifydep = input("Do you work in Marketing, Accounting, or FinOps? Enter yes or no: ")
    
for v in verifydep:
    if verifydep == 'yes':
        continue
    elif verifydep == 'no':
        print("Name Generator not permitted if outside listed departments. Exiting...")
        sys.exit() 
    else:
        print("Please enter yes or no. Exiting...")
        sys.exit()


#Select which department they work in
department = input("Enter Marketing, Accounting, or FinOps: ")

for d in department:
    
    if department == "Marketing" or department.lower() == "marketing":
            print("You have selected Marketing")
            break
    if department == "Accounting" or department.lower() == "accounting":
            print("You have selected Accounting")
            break
    if department == "FinOps" or department.lower() == "finops":
            print("You have selected FinOps")
            break
    else:
        print("Invalid Department. Please try again.")
        sys.exit()
        
        
#number of EC2 names needed
number = int(input("Enter the number of Generated EC2 names needed: "))

if number == 0:
    print("Number of Generated EC2 Names must be more than 0. Exiting...")
    sys.exit()
    
elif number > 0:
    print()        


for _ in range(1, number + 1):
    EC2_Name = department + generated_name(6)
    print("Your EC2 Name is/are: ", EC2_Name)
   
print("Thank you for your Service! Have a Great Day!")


