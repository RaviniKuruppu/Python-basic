# program to generate and print dict that contain number between 1 and n in the form {n:n*n*n}
myDict={}
n =int(input("Enter n value "))
for x in range(1,n+1):
    #myDict.update({x:x**3})
    myDict[x]=x**3
print(myDict)

