def CheckFactors(No):
    for i in range(1 , No):
        if(No % i == 0):
            print(i)

def main():
    print('Enter number to check factors')
    value = int(input())

    CheckFactors(value)

if __name__ == "__main__":
    main()