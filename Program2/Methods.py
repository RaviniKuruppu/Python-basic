def printTotal():
    b=23
    c=56
    d=b+c
    print(d)
    #printTotal()
    #return d
#s= printTotal()
#print(s)    
printTotal()


def printHello(i):
    if i==0:
        return
    print('Hello..')
    i =i-1
    printHello(i)
printHello(5)

