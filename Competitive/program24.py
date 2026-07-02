def RevDisplay(No):
    for i in range(No,0,-1):
        print(i)

def main():
    print("Enter number")
    value = int(input())

    RevDisplay(value)

if __name__ == "__main__":
    main()