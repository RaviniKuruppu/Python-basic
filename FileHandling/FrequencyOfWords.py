def readline(n):
    myDict={}    
    with open(n,"r")as file:
        list=file.read().split( ) # split is used to seperate word by spaces.
        for word in list:
            if(word in myDict.keys()):
                myDict[word]+=1
            else:
                myDict[word]=1
    print(myDict)   
           
readline("ABC.txt")