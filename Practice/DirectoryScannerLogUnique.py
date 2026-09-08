import sys
import os
import time

def DirectoryScanner(DirectoryPath):
    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    print('Log file gets created with name : ',LogFileName)

    fobj = open(LogFileName,"w")
    
    fobj.write("MARVELLOUS AUTOMATION SCRIPT \n")

    fobj.write(" Files from the directory are : \n")
    for FolderName,SubFolder, FileName in os.walk(DirectoryPath):
        for fName in FileName:
            fobj.write(fName+"\n")
    
    fobj.close()

def main():
    Border = "-"*50
    
    print(Border)
    print("MARVELLOUS AUTOMATION SCRIPT")
    print(Border)
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u Flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] ==  "--U"):
            print("PLease Execute the script as ")
            print("python FileName.py DiretoryName")
            print("Directory name should be absolute path")
        else:
            DirectoryScanner(sys.argv[1])

    else: 
        print("Invalid number of arguments")
        print("please --h or --u for more information")

    print(Border)
    print(" ThankYou for using MARVELLOUS AUTOMATION SCRIPT ")
    print(Border)

if __name__ == "__main__":
    main()