import schedule 
import time
import os

def DeleteEmpty(directory):
    Ret = os.path.exists(directory)
    if(Ret == False):
        print("Marvellous Automation Error : There is no such directory with name ",directory)
        return
    
    Ret = os.path.isdir(directory)
    if(Ret == False):
        print("Marvellous Automation Error : it is not a directory with name ",directory)
        return

    Directory = os.path.abspath(directory)

    TotalFiles = 0
    EmptyFiles = 0
    Border = "-"*50
    

    for folderName,subFolderName,fileName in os.walk(Directory):
        for fname in fileName:
            TotalFiles += 1
            fName = os.path.join(folderName,fname)
            try:
                if os.path.getsize(fName) == 0 :
                    EmptyFiles += 1
                    os.remove(fName)
            except Exception as e:
                print(e)

    with open("LogEmpty.txt",'a') as fobj:
        fobj.write(Border+"\n")
        fobj.write(f"Total Files Scanned : {TotalFiles}\n")
        fobj.write(f"Total Empty Files found and Deleted : {EmptyFiles}\n")
        fobj.write(Border+"\n")
        fobj.write("\n"+Border+"\n")  
        


def main():
    Folder = input("Enter the directory : ")

    schedule.every(1).minutes.do(DeleteEmpty,Folder)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()