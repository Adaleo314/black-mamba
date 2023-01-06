import random 
import string
import sys


#Generate a 6 character code of lowercase letters and numbers
def generated_name(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
    

print("**EC2 Name Generator Designed for Marketing, Accounting, & FinOps ONLY**") 
        
verifydep = input("Do you work in Marketing, Accounting, or FinOps? Enter yes or no: ")
    
for v in verifydep:
    if v == 'Yes, yes':
        continue
    elif v == 'No, no':
        print("Name Generator not needed if outside listed departments. Exiting..")
        raise SystemExit
        sys.exit()     


number = int(input("Enter the number of Generated EC2 names needed: "))

if number < 0:
    print("Number of Generated EC2 Names must be more than 0")
    
    

department = input(" Enter Marketing, Accounting, or FinOps: ")

for d in department:
    
    if department == "Marketing" or department.lower() == "marketing":
            print("You have selected Marketing")
            print("Your EC2 Name is: " + generated_name(6))
            break
    if department == "Accounting" or department.lower() == "accounting":
            print("You have selected Accounting")
            print("Your EC2 Name is: " + generated_name(6))
            break
    if department == "FinOps" or department.lower() == "finops":
            print("You have selected FinOps")
            print("Your EC2 Name is: " + generated_name(6))
            break
    





