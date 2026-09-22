# python ProcessSurvillence.py 2 MarvellousLog
# python ProcessSurvillence.py 2 time_interval Folder_Name
#                   0                 1           2
# len(sys.argv) -> 3

import psutil
import sys
import os
import time
import schedule

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        listprocess.append(info)
        
    return listprocess

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

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName , "Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Logfile gets succesfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("------Marvellous Platform Survillence System------\n")
    fobj.write("Log file gets created at : " +timestamp +"\n")
    fobj.write(Border+"\n\n")

    fobj.write("------------------System Report--------------------\n")

    # CPU information
    fobj.write(f"Number of active CPU cores : {psutil.cpu_count()}\n")
    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    # RAM information
    memory = psutil.virtual_memory()

    fobj.write(f"Ram usage : {memory.percent}% \n")
    fobj.write(f"Total Ram available : {memory.total} Bytes \n")
    fobj.write(Border+"\n")

    # network usage
    netobj = psutil.net_io_counters()

    fobj.write("Network Usage Report")
    fobj.write("\nSent : %.2f MB\n" %(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024)))

    # Process log

    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("Username : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("CPU usage : %.2f\n" %info.get("cpu_percent"))
        fobj.write("RAM usage : %.2f\n" %info.get("memory_percent"))

        fobj.write(Border+"\n")
        
    fobj.write(Border+"\n")
    fobj.write("-----------------End of log file-------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    Border = "-" * 50

    print(Border)
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

        #print("CPU Usage : ",psutil.cpu_percent())
        print("Scheduller started successfully")
        print("Press Ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence,sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments.")
        print("Unable to proceed as arguments are not passing.")
        print("Please use --h or --u flag for getting more details.")

    print(Border)
    print("--- Thank you for using our Automation System ---")
    print("------Marvellous Platform Survillence System------")
    print(Border)

if __name__ == "__main__":
    main()