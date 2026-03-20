num = int(input("enter the number"))
if(num < 0):
    print("not factorial possible")

elif(num==0):
    print("factorial is 1")

else:
    fact = 1
    for x in range(1,num+1):
        fact = fact*x

print("factorial is = " , fact)