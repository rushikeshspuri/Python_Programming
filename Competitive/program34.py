Minimum = lambda No1,No2 : min (No1,No2) 


def main():
    Value1 = int(input("Enter First Number"))
    Value2 = int(input("Enter Second Number"))
    Ret = Minimum(Value1,Value2)
    
    print(f"Minimum Number : {Ret}")

if __name__ == "__main__":
    main()