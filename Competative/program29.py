def DisplayBinary(No):
    Binarystr = bin(No)[2:]

    return Binarystr

def main():
    print("Enter number to check binary value")
    value = int(input())

    Ret = DisplayBinary(value)

    print(f"Binary Equvialent of {value} is {Ret}")

if __name__ == "__main__":
    main()