firstTuple =(100,20,30,40,60,70,40)
myList=list(firstTuple)
x=len(myList)
#print(x)
index=0
for i in range (x-1) :
    if(myList[i]==40):
        index=i
        print("index=",i)
        break
    
    
print(firstTuple.index(40))    
print(firstTuple.index(40,4,len(firstTuple)))   # index(value,start,stop)    
    