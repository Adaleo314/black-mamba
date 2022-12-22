#Using lists to add/edit info

#1 Set the users variable to an empty list
users = []

#2 Add users Kevin, Bob, Alice to list in that order
users.append('Kevin')
users.append('Bob')
users.append('Alice')

#3 Remove Bob from list
del users[1]

#4 Reverse the list of users
rev_users = list(reversed(users))

#5 Add user 'Melody' where 'Bob" used to be
users.insert(1, 'Melody')

#6 Add users Andy, Wanda, & Jim in a single command
users += ['Andy', 'Wanda', 'Jim']

#7 Slice the users lists to return the 3rd and 4th items and assign the result to 'Center_Users'
center_users = users[2:4] 


