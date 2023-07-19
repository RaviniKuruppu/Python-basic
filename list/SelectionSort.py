A = [5, 6, 8, 4, 1, 3, 9, 2, 7, 6] 

for i in range(len(A)):  
    minIndex = i 
    for j in range(i+1, len(A)): 
        if A[minIndex] > A[j]: 
            minIndex = j 
    temp = A[i]       
    A[i] = A[minIndex] 
    A[minIndex] = temp 
 
print (A)
