def Square(No):
    No = No * No 

    return No

def main():
    print("Enter Number to check Square")
    Value = int(input())

    Ret = Square(Value)

    print("Square of the number is : ",Ret)

if __name__ == "__main__":
    main()