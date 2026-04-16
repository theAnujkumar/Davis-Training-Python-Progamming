# opening file1 in reading mode
file1 = open("firstfile1.txt","r")

# opening file2 in reading mode
file2 = open("firstfile2.txt","w")

if(file1):
    # read data from lines to lines
    data = file1.readlines()

    # if data get
    if(data):
        print("content of file")

        while(data):
            print(data)

            # write data into file2 line by line
            file2.writelines(data)
            print("------------")
            # for next line
            data = file1.readlines()


    else:
        print("file is empty")

    file1.close()
    file2.close()

# file1 not exist
else:
    print("unable to open file")