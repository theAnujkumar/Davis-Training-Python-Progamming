vowels = ["a","e","i","o","u"]

string = input("enter the string ")

count = 0

for i in string :
    if i in vowels:
        count+=1

print ("total vowels are " , count)