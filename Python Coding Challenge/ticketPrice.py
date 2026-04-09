sunday = 200
monday = 150
tuesday = 99
wednesday = 159
thursday = 159
friday = 145
saturday = 145

day = input("enter the day").lower()
if(day == "sunday"):
    print("ticket price is 200")
elif((day=="monday") or (day=="tuesday")):
    print("ticket price is 150")
elif((day=="wednesday") or (day=="thursday")):
    print("ticket price is 250")
else:
    print("ticket price is 350")
