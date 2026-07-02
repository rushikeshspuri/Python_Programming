def DisplayEven(No):
    for i in range(2,No +1 ,2):
        print(i)
        

def main():
    print("enter number")
    value = int(input())

    DisplayEven(value)
if __name__ == "__main__":
    main()