DiviBy = lambda no :  no % 3 == 0 and no % 5 == 0

def main():
    print("Enter Value")

    nums = list(map(int,input().split()))

    FData = list(filter(DiviBy,nums))

    print(FData)

if __name__ == "__main__":
    main()
    