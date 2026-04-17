from collections import deque

n = int(input("Enter number of last lines: "))

with open("input.txt") as file:
    last_lines = deque(file, maxlen=n)

print("Last", n, "lines:")
for line in last_lines:
    print(line.strip())