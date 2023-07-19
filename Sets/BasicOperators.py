#it is iterable,it is mutable, and it has no duplicate elements.
myEmptySet=set()  # Empty set
print('This is an empty set:',myEmptySet)
print('This is an empty set:',{})
print(type(myEmptySet))
print()

mySet ={"Jan","Feb","March","Feb"}
print(mySet)   # Duplicate elements are not printed


# Add a value to the set
mySet.add("Dec")  
mySet.update({"April","May"}) # Add more than one value at once
mySet.add(('Oct','Oct')) # this is added to the set as a single element
mySet.update(('Nov','Nov')) # only one 'Nov' is added to the set
print(mySet)
print()

set1 = set()
set1.update([1,0,3,2])
set1.update('CSE')
print(set1)
set1.add('CSE')
print(set1)
print()


mySet.discard(('Oct','Oct'))   # Delete a value from a set
print("delete ('Oct','Oct') from the set:",mySet)
print()

#get the length
print(len(mySet))

# convert a set to a list
myList=list(mySet)

# iterate a set
print("iterate a set")
for x in mySet:
    print(x)
print()

#Removing elements from a Set
set1 = {1,2,3,4,5,6,7,4,3,1}
print(set1)
set1.remove(5)
print(set1)
set1.discard(7)
print(set1)
set1.discard(17)
print(set1)
set1.clear() # remove all the elements in the set
print(set1)
print()


set1 = set('CSE')
print('Set created with a string:',set1)
set1 = set(['C','S','E'])
print('Set created with a list:',set1)
set1 = set(['CS',1032,'S1',2020,9.89])
print('Set with mixed data types:',set1)
set1 = set([2,9,0,4,2,0,2,0,1,7])
print('Set with duplicate integer values:',set1)  
set2 = set1.copy() # copying a set
print("set2:",set2)
print()

A = set('COMPUTER')
B = set('SCIENCE')
print('A = COMPUTER','B = SCIENCE')
print("Set A:",A)
print("Set B:",B)
# Set Operation of Union
print('Set Union:',A.union(B)) # All the duplicates are removed
print('Set Union:',A | B)
C = {1,0,3,2,1,0,3,2}
print('Set Union:',A.union(B,C)) # get the uion of all the three sets
print()

# Set Operation of Difference
print('Set Difference: ',A.difference(B))
print('Set Subtraction:',A - B)
print("Set A:",A)
print('Set Differ. Update:',A.difference_update(B)) # get the difference and update the set 'A'
print('The updated set A:',A)
print('The set B:',B)
print()


A = set('COMPUTER1234')
B = set('SCIENCE3456')
C = set('12345678')
print('A = COMPUTER1234','B = SCIENCE3456','C = 12345678')
print("Set A:",A)
print("Set B:",B)
print("Set C:",C)
# Set Operation of Intersection
print('Set Intersection:',A.intersection(B))
print('Set Intersection:',A & B)
print('Set Intersection:',A.intersection(B,C)) ## get the intersection of all the three sets
print('Set Inter. Update:',B.intersection_update(C))
print('The updated set:',B)
print()


# Set Operation of Symmetric Difference
A = set('COMPUTER')
B = set('SCIENCE')
print('A = COMPUTER','B = SCIENCE')
print("Set A:",A)
print("Set B:",B)
print('Set Symm Diff: ',A.symmetric_difference(B))
print('Set Symm Diff:',A ^ B)
print('Update:',A.symmetric_difference_update(B))
print('The updated set:',A)
print()

# isdisjoint() function
A = {1,3,5,7,9}
B = {0,2,4,6,8}
print("is disjoint:",A.isdisjoint(B)) # check whether the two sets are disjoined or not
print("is disjoint:",len(A & B) == 0)
print()

# issubset() function
A = {1,3,5,7,9}; B = {0,2,4,6,8}
C = {0,4}
C.update(A)
C.update(B)
print("Set C:",C)
print("is subset:",B.issubset(A))
print("is subset:",B.issubset(C))
print("is subset:",B <= C)
print("is proper subset:",B < C)
print()

# issuperset() function
print("is superset:",A.issuperset(B))
print("is superset:",C.issuperset(B))
print("is superset:",C >= B)
print("is proper superset:",C > B)