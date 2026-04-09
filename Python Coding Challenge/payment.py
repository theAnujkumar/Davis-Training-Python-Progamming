# A payment system processes only numbers divisible by both 3 and 5. 
# Task: 
# Write a program to check if a number satisfies this condition. 
# Example: 
# Input: 15 
# Output: Yes

num = int(input("enter the number"))
if num%5==0 & num%7==0:
    print("yes satisfy condition")

else:
    print("not satisfy condition")