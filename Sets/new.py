# Merge by removing duplicates
myList1=[12,45,78,12,34,90]
myList2 =[12,23,32,89,78]
set1=set(myList1)
set2 =set(myList2)
NewSet =set1 | set2 # Union
print(list(NewSet))