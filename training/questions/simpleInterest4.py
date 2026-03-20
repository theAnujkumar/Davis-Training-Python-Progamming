def simpleInterest(p,r,t):
  ans = (p*r*t)/100
  print("ans is : ",ans)

principle = int(input("Enter principle amount: "))
rate = int(input("Enter rate : "))
time = int(input("Enter time: "))
simpleInterest(principle,rate,time)