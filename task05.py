numbers = (3, 6, 7, 8, 10, 11)

r = []
for num in numbers:
    if num % 2 == 0:
        r.append(num)
print(r)