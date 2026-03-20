
# num1 = int(input("enter 1st number"))
num1 = 3723
max_digit = 0

while(num1 != 0):
  digit = num1 % 10   # take last digit
  if(digit > max_digit):
    max_digit = digit
  
  num1 = num1 // 10   # remove last digit

print("ans is : " , max_digit)