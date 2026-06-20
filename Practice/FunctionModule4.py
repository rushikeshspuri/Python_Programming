from Marvellous import Addition,Substraction

def main():
    print("Enter Fisrt number : ")
    Value1 = int(input())

    print("Enter Second number : ")
    Value2 = int(input())
    
    iRet = Addition(Value1,Value2) 
    print("Addition is  : ",iRet)

    iRet = Substraction(Value1,Value2) 
    print("Substraction is  : ",iRet)


if __name__ == "__main__":
    main()