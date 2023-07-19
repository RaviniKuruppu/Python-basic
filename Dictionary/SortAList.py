myDict={'a':[1,4,3],'b':[123,78,98],'c':[25,78,11]}
newDict={}
# Method 1

for k,v in myDict.items():
    newDict[k]=sorted(v)
print(newDict)

#method 2

for k,v in myDict.items():
    myList =v           # Here v comes as a list. so can't create a list and append values.
    myList.sort()
    newDict[k]=myList
    
print(newDict)
