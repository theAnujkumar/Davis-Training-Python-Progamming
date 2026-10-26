from collections import Counter

stop = {"the", "is", "and"}

with open("data.txt") as f:
    words = f.read().lower().split()

words = [w for w in words if w not in stop]

print(Counter(words).most_common(10))