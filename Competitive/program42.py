Even = lambda no: no % 2 == 0

def main():
    print("Enter Values")
    nums = list(map(int, input().split()))

    FData = list(filter(Even, nums))

    print(FData)

if __name__ == "__main__":
    main()