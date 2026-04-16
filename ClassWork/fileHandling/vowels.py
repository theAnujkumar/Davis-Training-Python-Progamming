filev = open("firstfile1.txt","r")

if(filev):
    data = filev.read()

    #if(data != 0):
    vowels = 0
    totalChar = 0

    for i in data:
        totalChar += 1
        # if we get vowels
        if((i=="a") or (i=="e") or (i=="i") or (i=="o") or (i=="u")):
            vowels += 1
        filev.close()

    print("total character are " , totalChar)
    print("vowels are " , vowels)

    #else 
    # no data

else:
    print("unable to open file")