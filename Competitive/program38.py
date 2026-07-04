Multiplication = lambda No1,No2 : No1 * No2


def main():
    Value1 = int(input("Enter First Number"))
    Value2 = int(input("Enter Second Number"))
    
    Ret = Multiplication(Value1,Value2)
    
    print(f"{Value1} * {Value2} : {Ret}")

if __name__ == "__main__":
    main()