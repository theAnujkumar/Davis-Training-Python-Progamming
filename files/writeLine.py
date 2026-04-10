# write lines :-  writing multiple lines into the files 

#  syntax :- 
# filev.writelines(list of sentences)

# to write string data into file


# program for writing data into file
# opening file for write operation

filev = open("firstfile.txt","w")

# blank list of sentences
sentences = []

# write 3 sentence into file
print("enter 3 sentence : ")
for x in range(3):
    # input daata from user
    sentence = input()

    # inserting the sentence into the list
    sentences.append(sentence)

    # writing sentence into file
    # filev.write(sentence)
    print("-------------------")

# writing data into the file
filev.writelines(sentences)

print("data successfully written")
# closing file
filev.close()
