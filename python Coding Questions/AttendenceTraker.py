data = {}

with open("att.txt") as f:
    for line in f:
        emp, d, s = line.strip().split(",")
        data.setdefault(emp, []).append(s)

for emp, rec in data.items():
    p = rec.count("P")
    per = p / len(rec) * 100
    if per < 75:
        print(emp, "Low attendance")