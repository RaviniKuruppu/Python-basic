
# Find the minimum and maximum values
myDict={1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
myList=myDict.values()

print(myList)
print(max(myList))
print(min(myList))
print(sum(myList))  # print the sum

# print the sum of all values in the dictionary
s=0
for x in myList:
    s+=x
print(s)
    
    