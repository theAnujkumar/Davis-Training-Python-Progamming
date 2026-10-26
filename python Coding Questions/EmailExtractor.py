import re

with open("data.txt") as f:
    emails = set(re.findall(r"\S+@\S+\.\S+", f.read()))

print(emails)