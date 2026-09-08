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

def DeleteDuplicate(DirectoryName):
    MyDict = FindDuplicate(DirectoryName)

    Result =  list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    TotalDeleted = 0

    for value in Result:
        for SubValue in value:
            Count = Count +  1
            if(Count > 1):
                os.remove(SubValue)
                TotalDeleted = TotalDeleted + 1
        Count = 0

    print(f"Total Deleted files : {TotalDeleted}")


                
def main():
    DeleteDuplicate("Test")

if __name__ == "__main__":
    main()