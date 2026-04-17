shift = 3

def encrypt(text):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            result += chr((ord(ch) - ord(base) + shift) % 26 + ord(base))
        else:
            result += ch
    return result

with open("input.txt") as f1, open("encrypted.txt", "w") as f2:
    for line in f1:
        f2.write(encrypt(line))

print("File encrypted")