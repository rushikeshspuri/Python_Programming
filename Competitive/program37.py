Divisible = lambda No1: No1 % 5 == 0

def main():
    Value1 = int(input("Enter First Number"))
    Ret = Divisible(Value1)
    
    print(Ret)

if __name__ == "__main__":
    main()