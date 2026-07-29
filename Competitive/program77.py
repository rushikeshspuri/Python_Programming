import schedule
import datetime
import time
import shutil
import os

def COPYX(sourcefile,Destination):
    if(os.path.isfile(sourcefile) == False):
        print("Source file does not exist.")
        return

    if(os.path.isdir(Destination) == False):
        print("Destination folder does not exist.")
        return
   
    now = datetime.datetime.now()

    file_time = now.strftime("%d_%m_%Y_%H_%M_%S")
     
    base_name = os.path.basename(sourcefile)

    name_part, ext_part = os.path.splitext(base_name)

    new_name = name_part+"_"+file_time+ext_part

    full_dest_path = os.path.join(Destination,new_name)

    shutil.copy(sourcefile,full_dest_path)

    log_timestamp = now.strftime("%d-%m-%Y %I:%M:%S %p")

    with open("backup_log.txt",'a') as log_file:
        log_file.write("backup completed at "+ log_timestamp +"\n")


def main():
    sourcef = input("Enter sourcefile name\n")
    dest = input("Enter the destination\n")
       
    COPYX(sourcef,dest)

    schedule.every(1).minutes.do(COPYX,sourcef,dest)

    while(True):
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()
