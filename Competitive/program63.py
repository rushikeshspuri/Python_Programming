def CountWords(file):
    Count = 0

    try:
        fobj = open(file,'r')

        Data = fobj.read()

        Words = Data.split()

        for x in Words:
            Count += 1

        return Count

    except FileNotFoundError as fobj:
        print("FILE NOT FOUND")

def main():
    fname = input("Enter the file name : \n")

    Ret = CountWords(fname)

    print(f"count of words in file is : {Ret}")

if __name__ == "__main__":
    main()
