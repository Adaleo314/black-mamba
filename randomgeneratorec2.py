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

print("Enter your assigned department: ")
    
        

departments = []
departments += ('Marketing', 'Accounting', 'FinOps')










