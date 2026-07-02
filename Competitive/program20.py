def CheckPallindrome(No):
    temp = No
    Rev = 0
    
    while(No != 0):
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10
    
    if(Rev == temp):
        return True
    else:
        return False

def main():
    print("Enter Number")
    Value = int(input())

    Ret = CheckPallindrome(Value)

    if(Ret == True):
        print("Number is Pallindrome")
    else:
        print("Number is not Pallindrome")

if __name__== "__main__":
    main()