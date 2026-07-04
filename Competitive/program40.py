Largest = Largest = lambda No1, No2, No3: max(No1, No2, No3)


def main():
    Value1 = int(input("Enter First Number"))
    Value2 = int(input("Enter Second Number"))
    Value3 = int(input("Enter Third Number"))
    
    Ret = Largest(Value1,Value2,Value3)
    
    print(f"{Value1} {Value2} {Value3} largest is : {Ret}")

if __name__ == "__main__":
    main()