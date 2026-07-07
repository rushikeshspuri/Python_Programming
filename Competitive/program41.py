Square = lambda no : no * no

def main():
    print("Enter Values")
    nums = list(map(int ,input().split()))

    mData = list(map(Square,nums))

    print(mData)

if __name__ == "__main__":
    main()