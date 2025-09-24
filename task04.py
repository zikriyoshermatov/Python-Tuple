orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

r = []
for order in orders:
    if order[0] % 2 == 0:
        r.append(order)

print(r)