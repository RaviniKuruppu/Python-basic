from _io import UnsupportedOperation
def division(n):
    try:
        ans=n/0
        print(ans)
    except ZeroDivisionError as e:
        print("division by zero error ",e)   
    print("AAA")
        
#division(5)

list=[1,2,3,4,5]
def findSum(list):
    sum=0
    try:
        for x in range(0,len(list)+1):
            sum+=list[x]
            
    except IndexError as E:
        print("Error occured ",E)       
    
    except :
        print("Error occured")
        
    print(sum)
    print("AAAA")
#findSum(list)

def writeFile(file):
    with open(file)as F:
        try:
            F.write("Test")
        except :
            print("Error occured")
        print("test")
   
writeFile("ABC.txt")

