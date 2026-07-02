def ChkGreater(No1 , No2):
    if(No1 > No2):
        return No1
    else:
        return No2
        

def main():
    print("Enter first Number")
    Value1 = int(input())

    print("Enter second Number")
    Value2 = int(input())

    Ret = ChkGreater(Value1,Value2)

    print(Ret)

if __name__ == "__main__":
    main()