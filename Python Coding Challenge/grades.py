# Scenario: 
# An exam system assigns grades. 
# Task: 
# Write a program to assign grade based on marks. 
# Example: 
# Input: 82 
# Output: B

marks = int(input("enter your marks"))
if(marks > 85):
    print("A")
elif(marks<=85 & marks>=60):
    print("B")
elif(marks<=60 & marks>34):
    print("C")
else:
    print("D")