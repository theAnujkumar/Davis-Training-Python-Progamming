#Q1. discount

price = int(input("enter the price"))
discount = int(input("enter the discount"))

discount_amount = (price*discount)/100
total_bill = price-discount_amount

print("discount amount : " , discount_amount)
print("total bill : " , total_bill)
