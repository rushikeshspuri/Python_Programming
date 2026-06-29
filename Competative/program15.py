def DisplayOdd(No):
    for i in range(1,No +1 , 2):
        print(i)
        

def main():
    print("enter number")
    value = int(input())

    DisplayOdd(value)
if __name__ == "__main__":
    main()