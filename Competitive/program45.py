from functools import reduce

Addition = lambda a , b : a + b

def main():
    print("Enter Value")

    nums = list(map(int,input().split()))

    RData = reduce(Addition,nums)

    print(RData)

if __name__ == "__main__":
    main()