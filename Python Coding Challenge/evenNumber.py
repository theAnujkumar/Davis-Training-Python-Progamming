num = int(input("enter the number : "))

for i in range(1,num+1):
    if(i%2 == 0):       # check even or not
        print(i,",",end="")