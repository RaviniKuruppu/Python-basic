myDict={}    # empty dictionary
myDict1=dict() # empty dictionary
E =dict([('imperative','C'),('functional','Lisp'),('procedural','Pascal')])
print(E)
myDict2={'name':'Saman','Age':20,'Address':'Colombo','phone':'071111111','phone':'077777777'}
print(myDict2)     # only the second phone number is displaced
print(myDict2['name']) # only the name is displayed
print(myDict2['Address'])



print('Name' in myDict2)  # no key as Name
print()

print(len(myDict2))  # no of keys
print()

for k,v in myDict2.items(): # iterate the dictionary
    print(k,'= ',v)

print()  
print(myDict2.keys())     # print all the keys   this is printed as a list
print(myDict2.values())  # print all the values  this is printed as a list
print(myDict2.items())   # print all the items   this is printed as a list
print()


#add a key and value
myDict2['District']='Kaluthara'
myDict2.update({'A/l Results':'AAA'})
myDict2.update([("Subject",'Mechanics')])

print(myDict2)
print()
    
# Iterating
for x in myDict2:
    print(x,myDict2[x])

print()    
# remove a dictionary
A = {1:'Alice',2:'Bob',3:'Charlie',4:'Dave'}
print(A)
del A # the whole dict is removed

B = {1:'Alice',2:'Bob',3:'Charlie',4:'Dave',5:{'Eve':'Apple','Frank':'Huawei'}}
del B[3] # remove the key(3)
print("del B[3] ",B)

del B[5]['Frank'] # delete the key(Frank)
print("del B[5]['Frank'] ",B)

print()
B[6] ='George'# add a value
value = B.pop(2)  # remove the value with the key (2)
print("B.pop(2)=",value,",new dictionary",B)

val=B.popitem()
print("B.popitem()=",val,",new dictionary",B) # val is given as a tuple

B.clear()
print(B) # remain the empty list
print()


# get a certain value from the dictionary
storage = {1:'Register',2:'Cache',3:'Memor',4:'Disk'}
print(storage)
print("storage[2]=",storage[2]) # only the vale in the key(2) is displayed this gives a run-time error if the given key does not exist
print("storage.get(2)=",storage.get(2)) # get function is used
print("storage.get(6)=",storage.get(6)) # return None becuz no such element
print()

storage.update([(2,{2.1:'L1Cache',2.2:'L2Cache',2.3:'L3Cache'})])
print(storage)
print("storage[2][2.2]=",storage[2][2.2])
print()

# copy a dict
copy=myDict2.copy()
print(copy)

# sort the dict
print("sorted(myDict2)=",sorted(myDict2)) # sort the keys all the should be strings

#fromkeys()
myDict3=myDict2.fromkeys(["nick name","real Name"],"Saman") # second value is optional
print(myDict3)

# setdefalt()
#myDict3=myDict2.setdefault("nick name","Piyal")
#print(myDict3)



