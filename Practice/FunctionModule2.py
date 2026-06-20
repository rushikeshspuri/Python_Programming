import Marvellous as MI

def main():
    print("Enter Fisrt number : ")
    Value1 = int(input())

    print("Enter Second number : ")
    Value2 = int(input())
    
    iRet = MI.Addition(Value1,Value2) 
    
    print("Addition is  : ",iRet)

if __name__ == "__main__":
    main()