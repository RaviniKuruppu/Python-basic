import os;
def renameFile(fileName,newFileName):
    print("Befor remae the file")
    try:
        os.rename(fileName,newFileName)
    except FileNotFoundError:
        print(fileName,"cannot be found.Enter correct file name")
    print("After rename the file line1")
    print("After rename the file line2") 

renameFile("Second.txt", "fifth.txt")   