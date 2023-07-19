# find the second smallest number in an integer list
List=[34,87,56,2,45,678,90,87,11,2,]
List.sort()
List2=[]
print(List)
for y in List:
    if(y not in List2):
        List2.append(y)
print(List2[1])

# method 2
for x  in List:
    if(List[x-1]<List[x]):
        print(List[x])
        break    
    
        
       

        