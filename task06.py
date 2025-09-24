emails = (("Ali", "ali@gmail.com"), ("Vali", "vali@yandex.ru"), ("Sami", "sami@mail.ru"))

r = []
for name, email in emails:
    domain = email.split("@")[1]
    r.append(domain)
    
print(r)