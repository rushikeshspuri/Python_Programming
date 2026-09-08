import sys
import os
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("Path is invaid\n")
        return

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print(f"{DirectoryName} is not a Directory\n")
        return

    Duplicate = {}

    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fName in FileName:

            fName = os.path.join(FolderName, fName)

            CheckSum = CalculateCheckSum(fName)
        

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fName)
            else:

                Duplicate[CheckSum] = [fName]

    return Duplicate
                
def main():
    Data = FindDuplicate("Test")

    print(Data)

if __name__ == "__main__":
    main()