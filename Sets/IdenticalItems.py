myList1=[12,45,78,12,34,90]
myList2 =[12,23,32,89,78]

# Method 1
mySet=set()
for x in range(len(myList1)):
    for y in range(len(myList2)):
        if(myList1[x]==myList2[y]):
            mySet.add(myList2[y])
print(mySet)

# Method 2
set1=set(myList1)
set2 =set(myList2)
NewSet =set1 & set2  # intersection
print(list(NewSet))

# Method 3
mySet2 =set()
for x in myList1:
    if x in myList2:
        mySet2.add(x)
print(mySet2)
        



