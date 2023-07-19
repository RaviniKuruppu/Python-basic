myDict={'a':45,'b':34,'c':67,'d':78,'e':52,'f':67}
newDict={}
print(myDict)
""""myList=[]
for k,v in myDict.items():
    myList.append(v)

newList =[]
for x in myList:
    if(x not in newList):
        newList.append(x)
myList =newList
#print(myList)


for x in myList:
    for k,v in myDict.items():
        if(x==v):
            newDict[k]=v
            break
print(newDict)"""

for k,v in myDict.items():
    if v not in newDict.values():
        newDict[k]=v
print(newDict)
        