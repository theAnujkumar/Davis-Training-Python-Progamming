# collection of any data items and mutable

list = [20,[30,60],87,'hello']
list[2] = 0
#list[3] = 'hero'
list.append(5)

print(list)
print(list[1][1])

data2 = (40,30,90,60,20)


# for loop move in 1 direction from left to right

# indexing list,tuple,string


list1 = [20,87,50]
# append for adding element at last position
list1.append(39)
list1.append([6,4])
print(list1)

# extend 
# to insert each element of specified sequence datatype seperately at the end of list 
# list1.extend(30,50,[70,38])
# print(list1)

data = [40,90,30]
data.extend([80,20,10])
print("data is ",data)

#insert -> to insert element at specified index
data3 = [30,90,60,20]
data3.insert(2,50)
data3.insert(3,[60,20,10])
print(data3)

# pop -> to remove element from list from specified index
data4 = [40,90,70,30,20]
print(data4)
data4.pop()
print(data4)
data4.pop(2)
print(data4)

# remove() -> to remove the specified element from position of its first occurence
# starting from left to right
data5 = [40,70,90,70,30,20]
print(data5)
data5.remove(70)
print(data5)
data5.remove(10)
print(data5)

