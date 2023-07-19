# Remove a set of elements from a set
set1={10,20,30,40,50,300,500}
set2={10,20,30}
set1.difference_update(set2)
print(set1)


set1.difference_update({10,20,30})
