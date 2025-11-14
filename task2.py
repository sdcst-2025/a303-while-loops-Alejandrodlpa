#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""

username=""
password=""
while username!="admin" or password!="12345":
    username=input("Enter username: ")
    if username=="admin":
        password=input("Enter Password: ")
        if password!="12345":
            print("Acces denied")
        else:
            print("Acces granted")
    else:
        print("Acces denied")