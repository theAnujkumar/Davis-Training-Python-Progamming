try:
    num1 = float(input("enter first number "))
    num2 = float(input("enter second number "))

    print("-----------------")
    print("on dividing", num1 , "by", num2)
    print("ans is ",num1/num2)
    #print("ans is ",num1/float(num2))
    print("-----------------")

# like if
except TypeError:
    print("unexcepted data type")

except ValueError:
    print("unexcepted value type")

except ZeroDivisionError:
    print("unable to divide by 0")

# finally:
#     print("-----program executed---------")

else:
    print("----------------")

finally:
    print("-----program executed---------")


