# Scenario: 
# A system validates login credentials. 
# Task: 
# Write a program to verify username and password. 
# Example: 
# Input: admin, 1234 
# Output: Login Successful

username = input("enter user name : ").lower()
password = int(input("enter the password "))

confirmUserName = input("enter user name : ").lower()
confirmPassword = int(input("enter the confirm password "))

if username == confirmUserName & password == confirmPassword:
    print("valid username and password")
else:
    print("Invalid username and password")