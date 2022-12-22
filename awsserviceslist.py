#!/usr/bin/env python3.7

#1 Create an empty list

aws_services = []
 
#2 Add items to the list, 1 at a time, multiple, & to a specific spot

aws_services.append("Cloud9")
aws_services.append("EC2")
aws_services.append("VPC")
aws_services += ["S3", "DyanmoDB", "Lambda", "IAM", "Neptune", "Route 53", "X-Ray"]
aws_services.insert(6, "SNS")
aws_services.insert(9, "Lightsail")

#3 Print the list with the number of services

print("Random 12 AWS Services: ")
print(aws_services)
print("Total Number of Services in List: ", len(aws_services))

#4 Remove 2 specific items from the list
# aws_services.index(#) can be used to determine spot in list

del aws_services[0]
aws_services.remove("X-Ray")

print("Random 10 AWS Services: ")
print(aws_services)
print("Total Number of Services in List: ", len(aws_services))
