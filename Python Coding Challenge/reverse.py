num = int(input("enter the num : "))

rev = 0
while(num!=0):
    rem = num%10        #contain remainder
    rev = (rev*10) + rem    
    num = num//10
print(rev)