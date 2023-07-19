# remove the values from the first list which are in the second list

# Method 1
myList1=[12,45,78,12,34,90]
myList2 =[12,23,32,89,78]
set1=set(myList1)
set2 =set(myList2)
for x in myList1:
    if x in myList2:
        set1.discard(x)
print(set1)


# Method 2
set1.difference_update(set2)
print(set1)