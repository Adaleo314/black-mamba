#!/usr/bin/env python3.7

#Set emails variable to be an empty dictionary

emails = {}

#Adding names to email list
emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'

#Delete user from dictionary

del emails['craig']

#Add another user to emails
emails['dalton'] = 'dalton@example.com'

#Return list of keys and assign to users varible
users = list(emails.keys())

#Return list of values as email list

email_list = list(emails.values())

#Return a list of tuples w/ Key/Pairs
pairs = list(emails.items())


print(emails)
print(users)
print(email_list)
print(pairs)




