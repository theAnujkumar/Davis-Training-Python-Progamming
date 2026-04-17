my_list = [1, 2, 3, 4]
names = ["Anuj", "Rahul", "Priya"]
mixed = [1, "hello", 3.5, True]

# list slicing
print(my_list[1:3])   # [2, 3]
print(my_list[:2])    # [1, 2]

# 2. Remove Elements
my_list.remove(3)   # removes value
my_list.pop()       # removes last element

# 3. Update Elements
my_list[0] = 100

# Loop Through List
for item in my_list:
    print(item)

#🔹 Useful Functions
print(len(my_list))      # length
print(max(my_list))      # maximum
print(min(my_list))      # minimum
print(sum(my_list))      # sum

#🔹 List Methods
print(my_list.sort())        # sort list
print(my_list.reverse())     # reverse list
print(my_list.copy())        # copy list

#🔹 List Comprehension (Important 🔥)
squares = [x*x for x in range(5)]
# Output: [0, 1, 4, 9, 16]
print(squares)