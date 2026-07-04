def SumNatural(No):
    Sum = 0

    for i in range(1, No +1):
        Sum = Sum + i

    return Sum

def main():
    print("Enter a number")
    Value = int(input())

    Ret = SumNatural(Value)

    print("Sum of first", Value, "natural numbers is :", Ret) 

if __name__ == "__main__":
    main()
    
