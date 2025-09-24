students = [
    ("Ali", ["Fizika", "Matematika"]), 
    ("Laylo", ["Ingliz tili"]), 
    ("Jasur", ["Matematika", "Informatika"])       
]

count = 0

for i in students:
    if "Matematika"  in i[1]:
        count += 1

print(f"{count} ta talaba Matematika fanini tanlagan")