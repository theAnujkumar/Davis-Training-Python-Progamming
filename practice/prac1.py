for x in range(1,6):
    print("*" * x)

n = 5
for i in range(n, 0, -1):
    print("*" * i)

m = 5
for j in range(1,m+1):
    print(" "*(n-j) , "*"*j)
# m = 4
# for i in range(1,m):
#     for j in range(1,4):
#         print("X")
#     print(end="")