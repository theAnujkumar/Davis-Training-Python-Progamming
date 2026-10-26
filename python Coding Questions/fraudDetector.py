transactions = [("u1", 5000), ("u1", 6000), ("u2", 200)]

threshold = 4000
fraud = {}

for user, amt in transactions:
    if amt > threshold:
        fraud.setdefault(user, []).append(amt)

print(fraud)