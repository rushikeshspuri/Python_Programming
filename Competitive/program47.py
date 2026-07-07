Lenght = lambda a:  len(a) > 5

def main():
    print("Enter Value")

    string = input().split()

    FData = list(filter(Lenght,string))

    print(FData)

if __name__ == "__main__":
    main()
    