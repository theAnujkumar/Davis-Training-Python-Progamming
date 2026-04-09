year = int(input("enter the year : "))

if((year%4==0) and (year % 400==0)): #and (year % 1 != 0)
    print("leap year",year)
else:
    print("not leap year")