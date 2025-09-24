words = ("apple", "banana", "strawberry", "kiwi")

mx_words = words[0]
for word in words:
    if len(word) > len(mx_words):
        mx_words = word

print(mx_words)