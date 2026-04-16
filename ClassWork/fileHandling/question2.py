# a file with name student.txt contains records in the format name,marks,sit
# extract and sit only the student data whose marks is greater than 75 into a new file

# opening file1 in reading mode
file1 = open("student.txt","r")

# opening file2 in reading mode
file2 = open("firstfile2.txt","w")

if(file1):
    # read data line by line
    data = file1.readline()

    if(data):
        for line in file1:
            # remove extra spaces , new line
            line = line.strip()

             # split data
            name, marks, sit = line.split(",")

            # convert marks into integer
            if int(marks) > 75:
                # write only name and sit
                file2.write(name + "," + sit + "\n")

        print("filtered data written successfully")
    else:
        print("file is empty")

else:
    print("unable to open file")