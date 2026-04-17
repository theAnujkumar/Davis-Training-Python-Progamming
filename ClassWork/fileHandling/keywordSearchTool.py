keyword = input("Enter keyword: ")

with open("input.txt", "r") as file:
    found = False
    
    for line in file:
        if keyword in line:
            print(line.strip())
            found = True
    
    if not found:
        print("Keyword not found")