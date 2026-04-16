# to read 1 line of data at once

filev = open("firstfile1.txt","r")

if(filev):
    # to read data from file line to line
    data = filev.readline()
    if(data):
        print("content of files : ")
        while(data):
            print(data)
            print("------------------")
            data = filev.readline()
            #print("no. of occurences ",len(data))
    else:
        print("file is empty ")
    # closing file
    filev.close()
else:
    print("unable to open to file")

# where n is number of character in byte

# note -> if number of charcter has not been specified then if read complete content
