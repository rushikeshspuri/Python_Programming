def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("Enter Fisrt number : ")
    Value1 = int(input())

    print("Enter Second number : ")
    Value2 = int(input())
    
    iRet = Addition(Value1,Value2)
    print("Addition is  : ",iRet)

if __name__ == "__main__":
    main()