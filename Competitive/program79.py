import schedule
import time

def DisplayMessage(msg):
    print(msg)

def main():
    txt = input("Enter the message you want to print : ")

    schedule.every(5).seconds.do(DisplayMessage,txt)

    while(True):
        schedule.run_pending()
        time.sleep(1)

   
if __name__ == "__main__":
    main()