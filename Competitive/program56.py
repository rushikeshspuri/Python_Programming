def ChkPositive(No):
    if No == 0:
        print("Zero")
    elif No > 0:
        print("Positive")
    else:
        print("Negative")

def main():
    No = int(input("Enter Number"))

    ChkPositive(No)

if __name__ == "__main__":
    main()