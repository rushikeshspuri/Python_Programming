# Positional Argument 
def Area(Radius , Pi):
    Ans = Pi * Radius * Radius
    return Ans

def main():
    Ret = Area(10.5 , 3.14)
    print("area of Circle is : ",Ret)

    Ret = Area(13.6 , 7.12)
    print("area of Circle is : ",Ret)

if __name__=="__main__":
    main()