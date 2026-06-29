def CountDigits(No):
    Count  = 0
    while(No != 0):
        Digit = No % 10 
        Count = Count + 1
        No = No // 10
    
    return Count


def main():
    print("Enter number")
    value = int(input())

    Ret = CountDigits(value)

    print(Ret)

if __name__== "__main__":
    main()