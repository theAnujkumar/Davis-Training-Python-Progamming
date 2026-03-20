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
# to insert each element of specified sequence datatype seperatelu at the end of list 
# list1.extend(30,50,[70,38])
# print(list1)

data = [40,90,30]
data.extend([80,20,10])
print(data)

#insert -> to insert element at specified index
data3 = [30,90,60,20]
data3.insert(2,50)
data3.insert(3,[60,20,10])
print(data3)