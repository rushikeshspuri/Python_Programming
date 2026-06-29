def ChKPrime(No):
    for i in range(2,No):
        if(No % i == 0):
            return False

    return True

def main():
    print('Enter number to Check Prime')
    value = int(input())

    Ret = ChKPrime(value)

    if(Ret == True):
        print("number is Prime")
    else:
        print("Number is Not Prime")

if __name__== "__main__":
    main()