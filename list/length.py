# number of words longer than 5 letters
text = "My country is Sri Lanka."

mylist =text.split()
n=0
for x in mylist:
    if (len(x)>5) :  # if length of the word x is longer than 5
        n=n+1
        print(x)

print(n)

 




    