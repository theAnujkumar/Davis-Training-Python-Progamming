sales = {}
max_prod = ("", 0)

with open("sales.txt") as f:
    for line in f:
        try:
            p, c, price, q = line.strip().split(",")
            total = float(price) * int(q)
            sales[c] = sales.get(c, 0) + total

            if total > max_prod[1]:
                max_prod = (p, total)

        except:
            pass

print(sales, max_prod)