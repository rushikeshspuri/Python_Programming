import schedule
import time
import datetime

def Display():
    print(f"Jay Ganesh...{datetime.datetime.now()}")

def main():                    
    print("Automation Script started...")

    schedule.every(1).minute.do(Display)
    
    #infinte loop to run this program continuosly
    while(True):
        schedule.run_pending()
        time.sleep(1)           # main thread should not tired so we write time.sleep(1) sleep 1 sec

    print("End of Automation Script...")

if __name__ == "__main__":
    main()
