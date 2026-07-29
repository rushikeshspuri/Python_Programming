import schedule
import time
import datetime

def log(name):
    time_stamp = datetime.datetime.now().strftime("%d_%M_%Y_%H_%m_%S")

    newname = f"{name}_{time_stamp}.txt"

    fobj = open(newname,'w')

    fobj.write("Log file created successfull.\n")
    fobj.write(f"Creation time {datetime.datetime.now()}")

    print(f"{newname} created.")

    fobj.close()

def main():
    Border = "-"*50

    print(Border)
    print("------------Automation Script Started-------------")
    print(Border)

    name =  input("Enter the name for log file : ")

    schedule.every(30).seconds.do(log,name)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()