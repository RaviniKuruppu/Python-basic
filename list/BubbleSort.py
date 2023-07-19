def bubbleSort (List):
    
    x=len(List)
    for i in range (x-1):
        for j in range ((x-1)-i):
            if(List[j+1]<List[j]):
                temp=List[j]
                List[j]=List[j+1]
                List[j+1]=temp
List=[23,90,12,11,56,78]
bubbleSort (List)
      
print(List)             
