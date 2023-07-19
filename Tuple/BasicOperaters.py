#Tuples are immutable
myFirstTuple=() #empty
print(type(myFirstTuple))
mySecondTuple=tuple() #empty
print(type(mySecondTuple))
myThirdTuple=(5,) #must put a ','
print(type(myThirdTuple))
print()

p=(4,'physics',True,23.56) # can insert any data type
print(p)
print(p[0]) # access 0th index
print(p[0:3]) #access range of index
print()

x='saman',  # if you put a ',' then it convert to tuple
y=100,200,300
print(type(x))
print(type(y))
z=x+y  #can contaminate add 2 tuples
print(z)
print()


# convert a list to a tuple
List = [1,0,3,2]
print('A tuple created using a list',tuple(List))
print()

# unpacking
Tuple = ('Dept','of','CSE')
print(Tuple)
a,b,c = Tuple  # for this we should kwon exactly the no of elemnts
print(a,b,c) # access the elements one by one
print()


# adding tuples
Tuple1 = (True,False,True)
Tuple2 = (1,2,3)
print(Tuple1+Tuple2)
Tuple3 = (Tuple1,Tuple2,(4,5),(6,7)) # tuples are added seperatly
print(Tuple3)
print()

#Slicing of Tuple
Tuple1 = ('CS1033PF')
print(Tuple1)
Tuple = tuple('CS1033PF') 
print(Tuple)
print("Tuple[6:]=",Tuple[6:])
print("Tuple[-2:]=",Tuple[-2:])
print("Tuple[:-6]=",Tuple[:-6])
print()

# swapping values using tuples.
a = 'Alpha'
b = 'Bravo'
print((a,b))
(a,b) = (b,a)
print((a,b))

#Delete a tuple
del Tuple

# built in functions for tuples
tuple1=(True,False,True)
print(all(tuple1))
print(any(tuple1))
print()

tuple2=(7,3,9,4,8,1,5,6,2,9)
print("tuple2:",tuple2)
print("length:",len(tuple2))
print("Maximum:",max(tuple2))
print("Minimum:",min(tuple2))
print("Sum:",sum(tuple2))
print("sorted:",sorted(tuple2))
print()


proc = [(),(),(),(),()]
proc[0] = 'i9-99000K', 8, 3.6, 16, 2018
proc[1] = 'i7-9700K', 8, 3.7, 12, 2018
proc[2] = 'i5-9600F', 6, 2.9, 9, 2019
proc[3] = 'i3-9350KF', 4, 4.0, 8, 2019
proc[4] = 'i7-8086K', 6, 4.0, 12, 2018
for index, item in enumerate(proc):
    print("Processor",item[0],"released in",item[4])

