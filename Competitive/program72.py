import schedule
import time

def DisplaY():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(DisplaY)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()