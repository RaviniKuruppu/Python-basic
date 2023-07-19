# ordered, iterable collection Lists are mutable,can contain values of different data types
# List is a mutable data structure
List = [] # blank list
print("Blank List: ", List)
print()

# length of a list
inp_lst = ['Python','Java','Kotlin','Machine Learning','Keras']
size = len(inp_lst)
print(size)


myList=[10,200,40,59,2000]
print(myList)
List = ['A', "list with", 4, "values"] # List can contain different data types
print("List of values: ", List)
print()

#add  values.
myList.append(50)
print(myList)
print()

# Insert value
myList.insert(6, 3000)
myList.insert(8, 200)
print(myList)


# Remove value
myList.remove(200)     # first 200 is removed
print(myList)
for i in range(4,6): # Removing elements using iterator method
    myList.remove(myList[i])
print("List after removal: ",myList)
print()

# Pop value 
myList.pop(2) # to remove the an element by index
myList.pop() # remove the last element of the list
print("List after poping values:",myList)
print()

# Reverse
myList.reverse()
print("reverse the list:",myList)
print()

# extend
myList.extend([98,14,200,30000,200,98]) # adding of multiple values to the end of the list.
print("Extened list:",myList)
List2 = [76,200,98,200]
myList.extend([List2])
print("Extened list 2:",myList)
print()

# Delete
del myList[1]
print("After deleting myList[1]:",myList)
del myList[7 : 9]
print("List after deleting myList[7 : 9]: ",myList)
print()

# find Index
print(myList)
print("Index of 98:",myList.index(98)) # to find the index of a value
print("Index of 200:",myList.index(200)) # returns the lowest index where the element appears.
print()

# count
print("count of 200:",myList.count(200)) # number of time the value 200 is in the list
print()

#sort
print(myList)
myList.sort()
print("sorted list:",myList)
print()

# calculations
Data =[4, 8, 9, 6]
print("no of elements ",len(Data))
print('Sum of Elements ',sum(Data))
print('Max of Elements ',max(Data))
print('Min of Elements ',min(Data))
print()

#Slicing of a List
list1 = [0,1,2,3,4,5,6,7,8,9]
print(list1[:5])
print(list1[:-7]) # slice a sequence of elements from the end, back to a range denoted by an index value
print(list1[5:])
print(list1[3:7]) # [Start Index:End Index]
print(list1[:])  # A new copy of a list can be created using slicing
print(list1[::-1]) # reverse the whole list
print()

# Looping over Lists
for item in list1:
    print(item)
print()

for index, item in enumerate(myList):
    print(index, item)
print()

for index in range(len(myList)):
    print(myList[index])
print()

# change a element
myList[0]="A"
print(myList)
print()


# Clear a list
List = [1,2,3,4,5]
print("List before clearing: ", List)
List.clear()
print("List after clearing: ", List)
print()


# Copy
List1 = [1,2,3,4,5]
print("Original list: ", List1)
List2 = List1.copy()
print("List copy: ", List2)
print()

# Accessing elements
List = [1,2,3,[4,5,[6,7],8,9],10,11]
print("List is: ", List)
print("Access element at pos 4:",List[3])
print("Access element at pos 4[3]:",List[3][2])
print("Access element at pos 4[3[2]]:",List[3][2][1])
print("Access element at pos -1: ", List[-1])
print("Access element at pos -5: ", List[-5])
print()

# List Concatenation and Repetition
L1 = [1,2]
L2 = [30,40]
print(L1)
print(L2)
print("L1+L2:",L1+L2)
print("L1*4:",L1*4)
print()

# Lists and Strings
print(list("ABCDE"))
print()

# The any(iterable) and all(iterable) Functions
list1 = [3,6,9,12,15]
list2 = []
for i in range(0,5):
    list2.append(list1[i]%2 == 0)
print(list1,"divisible by 2 is:",all(list2))
print(list1,"has elements div by 2 is:",any(list2))
print()
