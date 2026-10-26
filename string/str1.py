# collection of characters
# immutable , order 

name = "Anil"
for x in name:
    print(x)

print(len(name))

# displaying name 4 times
print(name*4)

nam = "Sher"
# nam[2] = 'G'                      immutable
for x in nam:
    print(x,end=" ")


# list slicing
print(nam[1:3])   # [2, 3]
print(nam[:2])    # [1, 2]