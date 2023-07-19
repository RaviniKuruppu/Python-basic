def readFile(file):
    myList=[]
    with open(file,'r') as F:
        myvar=F.read()
        myList=myvar.split(",")
        
for ch in 