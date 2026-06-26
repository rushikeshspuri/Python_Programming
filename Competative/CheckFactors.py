def DisplahFactors(No):
    for i in range(1 ,No//2 +1):
        if(No % i == 0):
            print(i)

def main():
    print("enter Number to check factors")
    value = int(input())
    DisplahFactors(value)

if __name__=="__main__":
    main()