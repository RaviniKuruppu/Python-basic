myDict={'a':45,'b':34,'c':67,'d':78,'e':52,'f':97}

# Method 1
newDict={}
myList=[]
#print(myDict)
for k,v in myDict.items():
    myList.append(v)
    
myList.sort()

for x in myList:
    for k,v in myDict.items():
        if(x==v):
            newDict[k]=v
            break
print(newDict)
