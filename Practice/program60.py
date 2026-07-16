def Length(str):
    Count = 0
    Count = len(str)
    return Count

def main():
    print("Enter String")
    str = input()

    Ret = Length(str)

    print(Ret)

if __name__ == "__main__":
    main()