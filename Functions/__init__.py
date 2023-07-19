dept ='C'
def sum(arg1,arg2='E'):
    global dept
    dept+=arg1 +arg2
    return
sum('S')
print(dept)

def myFunc(a):
    a[0]=100
    return
x=[10,20,30]
myFunc(x)
print(x)

def printme(a="Moratuwa",b="University"):
    print(a,b)
    return
printme(b='Campus')