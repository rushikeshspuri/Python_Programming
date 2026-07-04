def ChkDiv(No):
    if(No % 3 == 0 and No % 5 == 0):
        return No
    else:
        return -1
        

def main():
    print("enter Number")
    Value = int(input()) 

    Ret = ChkDiv(Value)

    if(Ret == -1):
        print("Number is Not Divisble by 3 and 5")
    else :
        print("Number is Divisble by 3 and 5")

if __name__ == "__main__":
    main()
