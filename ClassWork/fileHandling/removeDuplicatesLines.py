seen = set()

with open("firstfile1.txt", "r") as file1, open("output.txt", "w") as file2:
    
    for line in file1:
        # remove extra spaces/newline for comparison
        clean_line = line.strip()
        
        if clean_line not in seen:
            file2.write(line)   # original line write karo
            seen.add(clean_line)

print("Duplicate lines removed successfully")