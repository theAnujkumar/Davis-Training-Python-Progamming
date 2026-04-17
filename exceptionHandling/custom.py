# input

#create Custom Exception class
class AgeException(Exception):
   pass

try:
  a=int(input("Enter the age "))
  if (a < 0):
     raise AgeException()
  
  elif a>=18 :
     print("You are eligible for vote")

  else:
     print("You are not eligilbe for vote")

# except ValueError as e:
#    print(e)
except ValueError:
   print("unexcepted data type")

except AgeException:
   print("age cannot be negative")