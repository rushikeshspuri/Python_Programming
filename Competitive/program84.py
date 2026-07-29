import schedule
import time
import datetime

def CrtFile(name):
    new_name =(f"{name}_{datetime.datetime.now().strftime("%d_%M_%Y_%H_%m_%S")}.txt\n")

    fobj = open(new_name,'w')

    fobj.write(f"file name : {new_name} \n")
    fobj.write(f"Creation date : {datetime.datetime.today()}\n")
    fobj.write(f"Creation time : {datetime.datetime.now()}\n")

    fobj.close()

def main():
    schedule.every(10).seconds.do(CrtFile,"log")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()