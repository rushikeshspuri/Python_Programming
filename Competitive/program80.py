import schedule
import time
import os
import datetime

def DirScan(DirName):
    if not os.path.isdir(DirName):
        print("Directory does not exist.")
        return

    entries = os.listdir(DirName)

    file_count = 0
    dir_count = 0

    for entry in entries :
        full_path = os.path.join(DirName , entry)
        if os.path.isfile(full_path):
            file_count = file_count + 1
        elif os.path.isdir(full_path):
            dir_count = dir_count + 1

    scan_time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print(f"Directory Scanned: {DirName}")
    print(f"Total Files: {file_count}")
    print(f"Total Subdirectories: {dir_count}")
    print(f"Scan Time: {scan_time}")
    print()
          
def main():
    Dir = input("Enter the Directory name you want to scan : ")

    schedule.every(1).minutes.do(DirScan,Dir)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()