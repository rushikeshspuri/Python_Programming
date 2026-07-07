from functools import reduce

Product = lambda a,b :  a * b

def main():
    print("Enter Value")

    nums = list(map(int,input().split()))

    RData = reduce(Product,nums)

    print(RData)

if __name__ == "__main__":
    main()
    