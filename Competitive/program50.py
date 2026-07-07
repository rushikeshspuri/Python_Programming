CountEven = lambda No : No % 2 == 0
    
def main():
    print("Enter Value")

    nums = list(map(int,input().split()))

    FData = list(filter(CountEven,nums))
    
    count = len(FData)
    print(count)

if __name__ == "__main__":
    main()
    