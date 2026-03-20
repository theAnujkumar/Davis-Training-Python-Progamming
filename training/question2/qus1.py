# create a list of 10 number and sort them into descending without using library method in python
arr = [5, 2, 9, 1, 7, 3, 8, 6, 4, 0]
n = len(arr)

for i in range(n):
    for j in range(0,n-i-1):
        # if previous element is smaller then next one
        if arr[j]<arr[j+1]:
            #swap
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)

