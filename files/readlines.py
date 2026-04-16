# to read the data of files and returns in form of list
# each line data will be present as each element of list

filev = open("firstfile1.txt","r")

if(filev):
    # to read data from file line to line
    data = filev.readlines()
    
