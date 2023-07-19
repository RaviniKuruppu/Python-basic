List=['This is the first line\n', 'This is the second line\n', 'This is the third line\n', 'This is the fourth line']
with open("ABCD.txt","w")as file:
    for i in List:
        file.write(i)

file= open("ABCD.txt","r")  # reading the file
print(file.read())
file.close()