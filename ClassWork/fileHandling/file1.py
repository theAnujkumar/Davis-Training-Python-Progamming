# write lines :-  writing multiple lines into the files 

#  syntax :- 
# filev.writelines(list of sentences)

# to write string data into file


# program for writing data into file
# opening file for write operation

filev = open("firstfile1.txt","w")

# blank list of sentences
sentences = []

# write 20 sentence into files
print("enter 20 sentence : ")
for x in range(20):
    # input data from user
    sentence = input()

    # inserting the sentence into the list
    # it will insert line by line
    sentences.append(sentence + "\n")
    
    #print("\n")
    # writing sentence into file
    # filev.write(sentence)
    print("-------------------")

# writing data into the file
filev.writelines(sentences)

print("data successfully written")
# closing file
filev.close()
