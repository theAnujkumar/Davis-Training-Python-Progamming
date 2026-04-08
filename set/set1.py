# collection of unique elements only and mutable

# 👉 Duplicate insert is ignored (same hash & equality check)
s = {1, 1, 2, 2}
print(s)  # {1, 2}

# 2. Unordered
# No fixed order (based on hash)
# Order may change after operations

# 3. Mutable but Elements Must Be Immutable

# Allowed:

s2 = {1, "abc", (1, 2)}
print(s2)

# Not allowed:

# {[1, 2]}  ❌

# 👉 Same reason as dict: hash must not change

data = {10,20,30,40,50}
data.add(60)
print(data)

data2 = {10,20,30}
#data2.update(30,60)

data2.pop()
print(data2)

data.remove(30)
print(data)