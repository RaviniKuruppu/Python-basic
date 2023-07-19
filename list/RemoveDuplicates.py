 #remove duplicate from a list

List=[11,2,34,56,11,33,78]
newList =[]
for x in List:
    if(x not in newList):
        newList.append(x)
List =newList
print(List)