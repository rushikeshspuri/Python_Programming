EvenOdd = lambda No1: No1 % 2 == 0

def main():
    Value1 = int(input("Enter First Number"))
    Ret = EvenOdd(Value1)

    if(Ret == True):
        print(f'{Value1} is Even')
    else:
        print(f"{Value1} is Odd")

if __name__ == "__main__":
    main()