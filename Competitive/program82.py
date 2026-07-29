import schedule
import time
import datetime
import os

def Directory(Dirname):

    if os.path.isdir(Dirname) == False:
        print(f"{Dirname} is not a directory ")
        return
    
    file_count = 0

    for FolderName,SubFolderName,FileName in os.walk(Dirname):
        for fname in FileName:
            file_count = file_count + 1

    time_stamp = datetime.datetime.now().strftime("%d_%M_%Y_%H_%m_%S")

    newname = f"DirectoryCountlog_{time_stamp}.txt"

    fobj = open(newname,'w')

    fobj.write(f"Number of files : {file_count}\n")
    fobj.write(f"{datetime.datetime.now()}\n")
    
    print(f"DirectoryCountlog created.")

    fobj.close()

def main():
    Border = "-"*50

    print(Border)
    print("------------Automation Script Started-------------")
    print(Border)

    name =  input("Enter the name of Directory : ")

    schedule.every(30).seconds.do(Directory,name)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()