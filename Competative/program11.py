def DisplayTable(No):
    for i in range(1,11):
        print(No * i)

def main():
    print("enter number to print the table")
    value = int(input())

    DisplayTable(value)

if __name__ == "__main__":
    main()