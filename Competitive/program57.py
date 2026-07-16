def ChkDivisible(No):
    if(No % 5 == 0):
        return True
    else:
        return False
    
def main():
    No = int(input("Enter Number"))

    Ret = ChkDivisible(No)

    print(Ret)

if __name__ == "__main__":
    main()