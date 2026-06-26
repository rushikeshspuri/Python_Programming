def Addition(no1 , no2):
    Sum = no1 + no2
    return Sum

def main():
    print("Enter first number")
    no1 = int(input())
    
    print("Enter Second number")
    no2 = int(input())

    iRet = Addition(no1 , no2)
    print("Addition is : ",iRet)

if __name__ == "__main__":
    main()