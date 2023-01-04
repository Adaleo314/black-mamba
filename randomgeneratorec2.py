from random import choice

def select_dep():

    print("Enter the Department name that requires EC2 generated name: ")
    print("Available Deparments for EC2 names: ")
    print("Marketing")
    print("Accounting")
    print("FinOps")
        
    assigned_dep = input("Enter your assigned department: ")
    
    
print(select_dep)    
    match assigned_dep:
        
        case 'Marketing'
            return 'Marketing'
        case 'Accounting'
            return 'Accounting
        case 'FinOps'
            return 'FinOps'
        case 
            print(Please select an applicable department. Responses are case-sensitive.)

departments = []
departments += ('Marketing', 'Accounting', 'FinOps')



assigned_dep = input("Do you work in Marketing, Accounting, or FinOps? ")






