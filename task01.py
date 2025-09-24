people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

oldest = people[0]
for old in people:
    if old[1] > oldest[1]:
        oldest = old

print(oldest)