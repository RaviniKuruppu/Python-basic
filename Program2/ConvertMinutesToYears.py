# convert minutes to years
x=3456789
y =x//(60*24*365)
print("Year "+str(y))
x=x%(60*24*365)
days =x//(60*24)
print("days "+str(days))
 
