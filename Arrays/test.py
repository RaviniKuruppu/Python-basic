# cs 2019
x="asdqwbnme"
y=['asd','qwb','nme']
z='m'
print(z in x and z in y)

n=0b10001011
print(n)

m=0b11110000
print(m)

a=0
for b in range(-100,1000,5):
    #print('b= ',b)
    for c in range(-1,2):
        #print('c= ',c)
        a+=c
print(a)

count=1
sum=0
for count in range(0,10,2):
    sum=sum +1
    
else:
    sum=sum+10
    
sum=sum+20
print(sum)
print()

i=0
while i<5:
    i+=1
    if i==3:
        print(i)
        break
else:
    print(i)

''''x=0
p=2
while (p<10):
    q=2
    while(q<p):
        if not(p%q): q=p
        q+=1
    if(q>p): x+=p
    p+1
print(x)'''

list =['a','b','c','d','e','f','g']
list[-3]='x'
print(list[3])

x='university.of.moratuwa'
print(x[6]+x[7]+x[-6:-4]+x[-14:-16])

for i in range(6,5,-1):print(str(i)*i)

def myFunc(a):
    a[0]=100
    return
x=[10,20,30]
myFunc(x)
print(x)

dept ='C'
def sum(arg1,arg2='E'):
    global dept
    dept+=arg1 +arg2
    return
sum('S')
print(dept)

def printme(a="Moratuwa",b="University"):
    print(a,b)
    return
printme(b='Campus')

''''def addnum(*q):
    sum=1
    for a in q:
        sum*=a
    return
print(addnum()*addnum(5,6,7))'''

print('%s%o'%('age',15))

''''s="c b e f a d"
myData=s.spilt( )
myData.sort()
print(myData)'''