def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False
          
def main():
    Value = int(input("Enter Number : "))

    Ret = CheckEven(Value)

    print(Ret)
        
    if(Ret == True):
        print("Its even number")
    else:
        print("its Odd number")    


if __name__ == "__main__":
    main()