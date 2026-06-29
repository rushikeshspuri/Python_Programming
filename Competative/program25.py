def ChkFactors(No):
    for i in range(2,No +1):
        if(No % i == 0):
            print(i)

def main():
    print('Enter Number')
    value =  int(input())

    ChkFactors(value)

if __name__ == "__main__":
    main()