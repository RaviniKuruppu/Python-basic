name=['kamal','nimal','amal','saman']
subject=['programming','maths','mechanic']
marks=[[87,79,99],[67,89,89],[63,55,43],[90,44,23]]
print("marks of nimal:",marks[name.index("nimal")])
print("marks of Saman:",marks[name.index("saman")])

#Maths marks
print('maths marks:')
for i in range(len(name)):
    print(name[i],marks[i][1])
    
print("Names of the students whose mechanic marks are less than 50:")
for m in range (len(name)):
    if(marks[m][2]<50):
        print(name[m])