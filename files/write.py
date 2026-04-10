# to write string data into file

#file.write("content")

# program for writing data into file
# opening file for write operation

filev = open("firstfile.txt","w")

# write 3 sentence into file
print("enter 3 sentence : ")
for x in range(3):
    # input daata from user
    sentence = input()

    # writing sentence into file
    filev.write(sentence)
    print("-------------------")

print("data successfully written")
# closing file
filev.close()
