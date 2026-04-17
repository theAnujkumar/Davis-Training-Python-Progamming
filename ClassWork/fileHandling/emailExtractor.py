import re

with open("data.txt", "r") as file1, open("emails.txt", "w") as file2:
    content = file1.read()
    
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+', content)
    
    for email in emails:
        file2.write(email + "\n")

print("Emails extracted")