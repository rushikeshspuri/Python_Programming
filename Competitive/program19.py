def displayRev(No):
    Rev = 0
    while(No != 0):
        Digit = No % 10
        Rev = Rev * 10 + Digit 
        No = No // 10
    
    return Rev



def main():
    print("Enter Number")
    Value = int(input())

    Ret = displayRev(Value)

    print("The Reverse of ",Value,"is :",Ret)

if __name__== "__main__":
    main()