# Default Argument 
def Area(Radius , Pi = 3.14):
    Ans = Pi * Radius * Radius
    return Ans

def main():
    Ret = Area(10.5)
    print("area of Circle is : ",Ret)

    Ret = Area(10.5 , 7.12)
    print("area of Circle is : ",Ret)
if __name__=="__main__":
    main()