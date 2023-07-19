with open("ABC.txt","w")as file: # creating a file and writing in it 
    file.write("This is the first line")
    file.write("\nThis is the second line")
    file.write("\nThis is the third line")
    file.write("\nThis is the fourth line")
    file.write("\nThis is the fifth line")



file= open("ABC.txt","r")  # reading the file and Dispay it
print(file.read())
file.close()


