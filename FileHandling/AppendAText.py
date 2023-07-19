with open("ABC.txt","a+")as file: # to write and read "a+" model is used
    file.write("\nThis is the sixth line")
    file.seek(0)
    print(file.read())