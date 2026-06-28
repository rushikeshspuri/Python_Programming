# hybrid application  contains both def procedural & lambda function

CheckEven = lambda No : (No % 2 == 0)
          
def main():
    Value = int(input("Enter Number : "))

    Ret = CheckEven(Value)  # internally CheckEven = (Value % 2 == 0)
        
    if(Ret == True):
        print("Its even number")
    else:
        print("its Odd number")    


if __name__ == "__main__":
    main()