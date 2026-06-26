def ChkEvenOdd(Value):
    if(Value % 2 == 0):
        return True
    else:
        return False

def main():
    print("Enter Number")
    No = int(input())
    Ret = False
    
    Ret = ChkEvenOdd(No)

    if(Ret == True):
        print("Number is Even :",No)
    else:
        print("Number is Odd :",No)

if __name__ == "__main__":
    main()

