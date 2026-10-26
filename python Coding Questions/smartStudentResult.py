def grade(p):
    if p >= 90: return "A"
    elif p >= 75: return "B"
    elif p >= 50: return "C"
    else: return "F"

toppers = {}

with open("students.txt") as f:
    for line in f:
        try:
            i, name, m1, m2, m3 = line.strip().split(",")
            m1, m2, m3 = int(m1), int(m2), int(m3)
            total = m1 + m2 + m3
            per = total / 3
            g = grade(per)

            if g not in toppers or per > toppers[g][1]:
                toppers[g] = (name, per)

        except:
            print("Invalid row skipped")

print("Toppers:", toppers)