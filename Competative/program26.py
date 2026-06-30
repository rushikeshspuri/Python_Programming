def Area(Length, Breadth):
    return Length * Breadth

def main():
    print("Enter Lenght")
    Value1 =int(input())

    print("Enter width")
    Value2 =int(input())

    Ret = Area(Value1, Value2)

    print("Area of rectangle is :",Ret)

if __name__ == "__main__":
    main()