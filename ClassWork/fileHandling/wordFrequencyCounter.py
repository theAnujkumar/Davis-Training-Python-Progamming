# opening file in reading mode
file1 = open("article.txt","r")

if(file1):
    data = file1.read()
    
    word = 0
    if(data):
        for i in data:
            word += 1

        print("total character are " , word)
    
    else:
        print("file is empty")

else:
    print("unable to open file")

# list of words