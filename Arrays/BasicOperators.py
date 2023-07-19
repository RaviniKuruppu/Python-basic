from array import *

# All the functions in lists are used in arrays
myArray =array('b',[123,-40,89,60,70]) #  here b is the data type if we put 'B'only +values are displaced
print(myArray)
print(myArray[2])
# Add an item 
myArray.append(90)
myArray.insert(3, 70)
print(myArray)

myArray[0]=100
print(myArray)
myArray.remove(89)


# iterate the array
for x in range(len(myArray)):
    print(myArray[x])
    
for y in myArray:
    print(y)



