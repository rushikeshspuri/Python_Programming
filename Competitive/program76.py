# 1 file : Marvellous.txt
# mdhe time ani date tak without overriding
import datetime
import schedule
import time 

def File():
    timestamp = datetime.datetime.now()

    fd = open("Marvellous.txt",'a')

    fd.write(f"task executed at : {timestamp}\n")

    fd.close()
    
def main():
    schedule.every(5).seconds.do(File)

    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()