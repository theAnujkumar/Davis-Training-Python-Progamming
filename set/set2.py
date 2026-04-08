s = set()
s.add(10)
s.add(20)
s.add(30)

print(s)

# Step-by-step:
# hash(10) → index 2 → store
# hash(20) → index 5 → store
# hash(30) → index 2 → collision
# → move to next empty slot