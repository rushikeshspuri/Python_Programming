def ChkNum(number):
    if number % 2 == 0:
        return True
    else :
        return False

def main():
    print("Enter Number")
    
    No  = int(input())
    
    Chk = ChkNum(No)

    if(Chk == True):
        print("Number is Even")
    else:
        print("Number is Odd")
        
if __name__ == "__main__":
    main()
