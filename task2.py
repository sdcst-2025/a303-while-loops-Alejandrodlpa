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
while username!="admin" and password!="12345":
    username=input("Enter username: ")
    if username!="admin":
        print("Access denied")
    else:
        password=input("Enter password: ")
        if password!="12345":
            print("Access denied")
        else:
            print("Access granted")
    