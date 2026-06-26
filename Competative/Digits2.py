def main():
    No = 751
    Digit = 0

    while(No != 0):
        Digit = No % 10
        print(Digit)
        No = No // 10

if __name__ == "__main__":
    main()