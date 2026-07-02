def CheckPerfect(No):
    Sum = 0
    for i in range(1 ,No//2 +1):
        if(No % i == 0):
            Sum = Sum + i
       
    if(Sum == No):
        return True
    else:
        return False
    
   
def main():
    print("enter Number to check factors")
    value = int(input())
    
    Ret = CheckPerfect(value)

    if(Ret == True):
        print("Number is Perfect")
    else:
        print("Number is not Perfect")

if __name__=="__main__":
    main()