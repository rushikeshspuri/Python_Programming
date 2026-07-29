import schedule
import os
import time
import datetime

def Fileinfo(filepath):
    if os.path.isfile(filepath):
        Size = os.path.getsize(filepath)
    else:
        print(f"{filepath} doesnt exist.\n")
        return

    filepath = os.path.abspath(filepath)

    fobj = open("Fileinfolog.txt",'a')

    fobj.write("-"*30 + "\n")
    fobj.write(f"File path : {filepath}\n")
    fobj.write(f"File Size : {Size}\n")
    fobj.write(f"Date time : {datetime.datetime.now()}\n")
    fobj.write("-"*30 + "\n")

    fobj.close()

def main():
    filepath = input("Enter file path: ")

    schedule.every(10).seconds.do(Fileinfo,filepath)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()