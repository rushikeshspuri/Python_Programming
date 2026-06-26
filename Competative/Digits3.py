def DisplayDigits(No):
    Digit = 0

    while(No != 0):
        Digit = No % 10
        print(Digit)
        No = No // 10

def main():
    print("Enter Number to convert Digit")
    No = int(input())
    DisplayDigits(No)

if __name__ == "__main__":
    main()