votes = ["A", "B", "A", "C"]
seen = set()
count = {}

for v in votes:
    if v not in seen:
        seen.add(v)
        count[v] = count.get(v, 0) + 1

print("Winner:", max(count, key=count.get))