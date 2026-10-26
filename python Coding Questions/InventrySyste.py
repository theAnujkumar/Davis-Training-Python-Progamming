inv = {}

def add(name, qty):
    inv[name] = inv.get(name, 0) + qty

add("pen", 10)
add("pen", 5)
print(inv)