import random 
import string
import sys


#Generate a 6 character code of lowercase letters and numbers
def generated_name(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
    

print("EC2 Name Generator Designed for Accounting, Marketing, & FinOps ONLY") 
        
verifydep = input("Do you work in Marketing, Accounting, or FinOps? Enter yes or no: ")
    
for v in verifydep:
    if verifydep == 'Yes, yes':
        continue
    elif verifydep == 'No, no':
        sys.exit() 
        break

department = input(" Enter Marketing, Accounting, or FinOps: ")

for d in department:
    
    if department == "Marketing" or department.lowercase() == "marketing":
            print("You have selected Marketing")
            print("Your EC2 Name is: " + generated_name(6))
            break
    if department == "Accounting" or department.lowercase() == "accounting":
            print("You have selected Accounting")
            print("Your EC2 Name is: " + generated_name(6))
            break
    if department == "FinOps" or department.lowercase() == "finops":
                print("You have selected FinOps")
                print("Your EC2 Name is: " + generated_name(6))
                break
    
        

departments = []
departments += ('Marketing', 'Accounting', 'FinOps')










