# ordered , immutable , allow duplicates

fruits = (1,"apple",3.14,True)

# for i in range fruits:
#     print i

tuplex = (2,4,5,6)
# tuplex[2] = 3                 immutable
list1 = list(tuplex)
print(tuplex)

list1.append(8)                 # add at end
print(list1)

x,y,z,t = tuplex                # assignment
print(x,y,z,t)

t1 = ("hel")*3
print(t1)

num = (1,1,2,2,2,3,3,3,4,4,5,6)
print(num.count(2))                 # count no. of times

print(len(num))                     # length of num

let = ["a","b","c"]                  # find index of element
let1 = let.index("c")
print(let1)