myList=[(3,5,7,8),(2,2,67,5,6),(78,90,67)]
mylist=[]
for x in myList:
    lst =list(x)
    lst[len(lst)-1]=1000
    y=tuple(lst)
    mylist.append(y)
    
print(mylist)    
print()   
  
# method 2   
for i,j in enumerate(myList):
    lst =list(j)
    lst[len(lst)-1]=1000
    myList[i]=tuple(lst)
print(myList)

