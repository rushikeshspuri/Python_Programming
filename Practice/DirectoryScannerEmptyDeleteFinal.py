###################################################################################################################
#
#   Importing required Libraries
#
####################################################################################################################

import sys
import os
import time
import schedule

####################################################################################################################
#
#   Function name   :               DirectoryScanner
#   Input   :                       Name of Directory
#   Description :                   Deletes all empty files periodically
#   date    :                       19/07/2026
#   Author  :                       Rushikesh Sanjay Puri
#
####################################################################################################################

def DirectoryScanner(DirectoryPath):
    Border = "-"*40
    
    timestamp = time.ctime()
    
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    Ret = False

    Ret = os.path.exists(DirectoryPath)
    if(Ret == False):
        print("Marvellous Automation Error : There is no such directory with name ",DirectoryPath)
        return
    
    Ret = os.path.isdir(DirectoryPath)
    if(Ret == False):
        print("Marvellous Automation Error : it is not a directory with name ",DirectoryPath)
        return


    print('Log file gets created with name : ',LogFileName)

    fobj = open(LogFileName,"w")    

    fobj.write(Border+"\n")    
    fobj.write("MARVELLOUS AUTOMATION SCRIPT \n")
    fobj.write(Border+"\n\n")  

    fobj.write(" Files from the directory are : \n\n")
    fobj.write(Border+"\n")  
    
    TotalFiles = 0
    EmptyFiles = 0
    for FolderName,SubFolder, FileName in os.walk(DirectoryPath):
        for fName in FileName:
            TotalFiles = TotalFiles + 1
            
            fName = os.path.join(FolderName,fName)
            fobj.write(f"{fName} : {os.path.getsize(fName)} bytes\n")
            
            if(os.path.getsize(fName) == 0):
                EmptyFiles = EmptyFiles + 1
                os.remove(fName)
            
    fobj.write(Border+"\n")
    fobj.write(f"Total Files Scanned : {TotalFiles}\n")
    fobj.write(f"Total Empty Files found and Deleted : {EmptyFiles}\n")

    fobj.write(Border+"\n")
    fobj.write("Log file gets created at : "+timestamp)    
    fobj.write("\n"+Border+"\n")  
    
    fobj.close()

###################################################################################################################
#
#   Function name   :               main
#   Input   :                       Command line arguments
#   Description :                   It Controls the script
#   date    :                       19/07/2026
#   Author  :                       Rushikesh Sanjay Puri
#
####################################################################################################################

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
           
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            

            while(True):
                schedule.run_pending()
                time.sleep(1)

    else: 
        print("Invalid number of arguments")
        print("please --h or --u for more information")

    print(Border)
    print(" ThankYou for using MARVELLOUS AUTOMATION SCRIPT ")
    print(Border)

###################################################################################################################
#
#   Starter of the automation script
#
####################################################################################################################

if __name__ == "__main__":
    main()