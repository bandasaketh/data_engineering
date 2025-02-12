String = " hello, World! "
unique_chars = ""
for char in String:
    if char not in unique_chars:
        unique_chars += char
print(unique_chars)