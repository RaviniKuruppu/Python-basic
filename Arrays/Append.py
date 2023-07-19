from array import array
myList=[12,90,78,56,46,72]
myArray=array('b',[])

# method 1
for x in myList:
    myArray.append(x)
print(myArray)



# method 2
myArray.fromlist(myList)