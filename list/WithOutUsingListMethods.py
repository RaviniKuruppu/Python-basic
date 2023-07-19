L=[11,12,3,97,74]
L[0]=-L[0]
print(L)
L=L+[10]
print(L)
L[2:2]=[22]
print(L)
L[1:2]=[]
print(L)
L=L+[122,121]
print(L)
for i in range(len(L)):
    if(L[i]==3):
        print("Index of 3 is ",i)