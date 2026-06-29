def Cube(No):
    No = No * No * No

    return No

def main():
    print("Enter Number to check Cube")
    Value = int(input())

    Ret = Cube(Value)

    print("Cube of the number is : ",Ret)

if __name__ == "__main__":
    main()