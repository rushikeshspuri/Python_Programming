import schedule
import time
import datetime

def Display():
    print(f"Jay Ganesh...{datetime.datetime.now()}")

def main():                    
    print("Automation Script started...")

    schedule.every(1).minute.do(Display)
    #issuee

if __name__ == "__main__":
    main()
