# map 2 list in to a dictionay
Lst1 =['Name','age','phone','Email']
Lst2 =['Saman',20,'07777777','Saman@gmail.com']

# Method 1
myDict={}
for i in range(len(Lst1)):    # Here i starts from zero 
    myDict[Lst1[i]] =Lst2[i]
print(myDict) 

# Method 2
newDict={}
for x,y in enumerate(Lst1):
    myDict[y]=Lst2[x]
print(myDict)


# Method 3
myDict2={}
for i,j in zip (Lst1,Lst2):
    myDict2[i]=j
print(myDict2)


# Method 4
print(dict(zip(Lst1,Lst2)))
