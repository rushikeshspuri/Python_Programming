import os
import schedule
import time
import shutil

def Copy(source, destination):
    if not os.path.isdir(source):
        print("Source directory doesn't exist")
        return
    elif not os.path.isdir(destination):
        print("Destination directory doesn't exist")
        return

    for file in os.listdir(source):
        if file.endswith(".txt"):
            sourcePath = os.path.join(source,file)
            destinationPath = os.path.join(destination,file)
            try:
                shutil.copy2(sourcePath,destinationPath)
                with open("CopyLogfile.txt",'a')as fobj:
                    fobj.write(f"{file} copied successfully : \n")
            except Exception as e:
                print(e)
def main():
    Source = input("Enter source directory : ")
    Destination = input("Enter destination directory: ")

    schedule.every(15).seconds.do(Copy,Source,Destination)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()