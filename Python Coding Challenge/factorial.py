num = int(input("enter the num : "))
fact = 1

if(num==0 or num==1):
    print("factorial is 1")


else:
    for i in range(1,num+1):
        fact = fact*i

print("fact is ",fact)