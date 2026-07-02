def ChkPerfect(No):
    Sum = 0

    if (No <= 0):
        return False

    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i
    
    if(Sum == No):
        return True
    else:
        return False

def main():
    print("Enter number")
    value = int(input())

    Ret = ChkPerfect(value)

    if (Ret == True):
        print(f"{value} is a Perfect Number")
    else:
        print(f"{value} is NOT a Perfect Number")

if __name__ == "__main__":
    main()