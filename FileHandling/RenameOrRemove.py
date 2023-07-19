import os;

def renameFile(fileName,newFileName):  # (fileName,newFileName)
    os.rename(fileName,newFileName)
    
renameFile("newFile","newFile.txt")


def removeFile(fileName):
    os.remove(fileName)
removeFile("newFile.txt")

