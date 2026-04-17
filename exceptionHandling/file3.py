# input
try:
  a=int(input("Enter the age "))
  if a>=18 :
     print("You are eligible for vote")
  else:
     print("You are not eligilbe for vote")
except ValueError as e:
   print(e)