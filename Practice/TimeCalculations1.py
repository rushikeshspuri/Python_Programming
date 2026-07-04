# 5 : 1 * 2 * 3 * 4 * 5 

def Factorial(No):
    Fact = 1

    for i in range(1,No +1):
        Fact = Fact * i

    return Fact

def main():
    print("Enter number")
    value =  int(input())

    Ret = Factorial(value)

    print("fadctorial are : ",Ret)

if __name__ == "__main__":
    main()