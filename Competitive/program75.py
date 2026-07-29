import schedule
import time

def Namaskar():
    print("Namaskar")

def main():
    schedule.every().day.at("09:00").do(Namaskar)

    while(True):
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()