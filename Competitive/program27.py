from math import pi

def AreaCircle(Radius):
    Area = pi * Radius * Radius
    return Area

def main():
    print("Enter Radius")
    Value1 =float(input())

    Ret = AreaCircle(Value1)

    print("Area of Circle is :",Ret)

if __name__ == "__main__":
    main()