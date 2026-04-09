num = int(input("enter the num : "))

rev = 0
while(num!=0):
    rem = num%10        #contain remainder
    rev += 1            #add the digits
    num = num//10
print(rev)