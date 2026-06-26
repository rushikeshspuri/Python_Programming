def ChkDivi(No):
    if(No % 3 == 0 and No % 5 == 0):
        return True
    else:
        return False
    
def main():
    print("Enter Number")
    Value = int(input())

    bRet = ChkDivi(Value)

    if(bRet == True):
        print("Number is Divisible by 3,5")
    else:
        print("Number is Not Divisible by 3,5")

if __name__== "__main__":
    main()