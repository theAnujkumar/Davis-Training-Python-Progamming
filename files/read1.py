# read data from file

#read()
# to read specified number of character from current postion in a file

filev = open("firstfile1.txt","r")

if(filev):
    # to read data from file
    data = filev.read()
    print(data)
    print("------------------")
    print("no. of occurences ",len(data))
    # closing file
    filev.close()
else:
    print("unable to open to file")

# where n is number of character in byte

# note -> if number of charcter has not been specified then if read complete content
