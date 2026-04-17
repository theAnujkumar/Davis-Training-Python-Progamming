with open("file1.txt") as f1, open("file2.txt") as f2:
    set2 = set(line.strip() for line in f2)
    
    for line in f1:
        if line.strip() not in set2:
            print(line.strip())