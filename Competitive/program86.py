import schedule
import time

def ReadDisplay(file):
    try:
        fobj = open(file,'r')

        Data = fobj.read()

        if Data == "":
            print("file is empty\n")
        else:
            print("\nfile contents:\n")
            print(Data)

    except FileNotFoundError as fobj :
        print("file doesnt exist")

    except PermissionError  as fobj:
        print("permission not given")

    except OSError as fobj:
        print("file cannot be opened")

def main():
    File = input("Enter the file name : ")

    schedule.every(1).minutes.do(ReadDisplay, File)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()