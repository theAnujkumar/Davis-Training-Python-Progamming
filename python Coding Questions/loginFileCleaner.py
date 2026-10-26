seen = set()
errors = {}

with open("log.txt") as f:
    for line in f:
        if "ERROR" in line and line not in seen:
            seen.add(line)
            errors[line] = errors.get(line, 0) + 1

print(errors)