# elements are stored in key value pair
# key is used as index hence it is mutable and 

x = {}          # dictionary
m = set()       # set
student = {}    # blank dict
# insert element 
student['name'] = 'Sher'
student['age'] = 20

# update
# create new entry if no exist
student['name'] = 'Ramesh'
print(student)

student2 = {'name': 'Ramesh', 'age': 20 ,  'sal' : '15k'}
# give keys
for x in student2:
    print(x)

# give values
for x in student2:
    print(student2[x])

# keys -> returns a list of key of elements of dictionary
# values -> returns a list of values of elements of dictionary
# items -> returns a list of elements each element in form of tuple i.e. key , value pair

y = student2.keys()
print(y)

z = student2.values()
print(z)

t = student2.items()
print(t)

# get -> returns the value of the elements for specified keys in 1st parameter.
# if not elements not found then returns 2nd parameter as error message

b = student2.get('age','not found')
print(b)

c = student2.get('hindi','not found')
print(c)

# key -> immutable (col)  , value => mutable (row)