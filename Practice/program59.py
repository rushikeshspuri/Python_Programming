def DisplayEven(No):
    for i in range(No,21,2):
        print(i)
    
def main():
    No = int(input("Enter Number"))

    DisplayEven(No)

if __name__ == "__main__":
    main()