def SumDigits(No):
    Sum = 0
    
    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
    
    return Sum

def main():
    print("Enter number")
    value = int(input())

    Ret = SumDigits(value)

    print("Sum of Digits of",value ,"is :",Ret)

if __name__ == "__main__":
    main()