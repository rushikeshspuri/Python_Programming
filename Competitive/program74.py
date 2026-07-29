import schedule
import time

def PrintX():
    print("coding kar...")

def main():
    str = "Coding kar"

    schedule.every(30).minutes.do(PrintX)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()