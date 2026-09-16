# python ProcessSurvillence.py 2 MarvellousLog
# python ProcessSurvillence.py 2 time_interval Folder_Name
#                   0                 1           2
# len(sys.argv) -> 3

import psutil
import sys
import os

def PlatformSurvillence(FolderName):
    Border = "-" * 50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to procedd as directory name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the logfile gets created successfully")

def main():
    Border = "-" * 50

    print(Border)
    print("------Marvellous Platform Survillence System------")
    print(Border)

    print(Border)
    print("--- Thank you for using our Automation System ---")
    print("------Marvellous Platform Survillence System------")
    print(Border)

    # --h & --u handling
    if len(sys.argv) == 2:

        if sys.argv[1] == '--h' or sys.argv[1] == '--H':
            print("This automation script is used to perform.")
            print("1 : It fetch the information of running processes.")
            print("2 : It fetch information about the primary storage as RAM.")
            print("3 : It fetch information about the secondary storage as HDD.")
            print("4 : It fetch information about the microprocessor.")
            print("5 : It gets auto scheduled periodically.")
            print("6 : It maintain all records into log file.")
            print("7 : It sends the log file through mail periodically")

        elif sys.argv[1] == '--u' or sys.argv[1] == '--U':
            print("Use the Automation script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of Folder for log file creation")

        else:
            print("Unable to proceed as arguments are not passing.")
            print("Please use --h or --u flag for getting more details.")

    # Actual project code
    elif len(sys.argv) == 3:
        PlatformSurvillence(sys.argv[2])

    else:
        print("Invalid number of arguments.")
        print("Unable to proceed as arguments are not passing.")
        print("Please use --h or --u flag for getting more details.")

if __name__ == "__main__":
    main()