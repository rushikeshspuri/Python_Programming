Addition = lambda No1, No2 : No1 + No2
Subtraction = lambda No1, No2 : No1 - No2
Multiplication = lambda No1, No2 : No1 * No2
Division = lambda No1, No2 : No1 // No2

def main():
    print("Enter first number")
    Value1 =  int(input())

    print("Enter second number")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)
    print("addition is :",Ret)

    Ret = Subtraction(Value1,Value2)
    print("Subtraction is :",Ret)

    Ret = Multiplication(Value1,Value2)
    print("Multiplication is :",Ret)

    Ret = Division(Value1,Value2)
    print('Division is :',Ret)

if __name__ == "__main__":
    main()