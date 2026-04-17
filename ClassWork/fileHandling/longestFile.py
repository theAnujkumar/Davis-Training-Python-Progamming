with open("input.txt", "r") as file:
    longest_line = ""
    
    for line in file:
        if len(line) > len(longest_line):
            longest_line = line

print("Longest line length:", len(longest_line.strip()))
print("Content:", longest_line.strip())