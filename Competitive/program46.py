from functools import reduce

Min = lambda a , b : a if a < b else b

def main():
    print("Enter Value")

    nums = list(map(int,input().split()))

    RData = reduce(Min,nums)

    print(RData)

if __name__ == "__main__":
    main()
    