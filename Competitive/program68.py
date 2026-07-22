def DisplaY(file):
    try:
        fobj = open(file,'r')

        Data = fobj.read()

        print(Data)

    except FileNotFoundError as e:
        print("file not found")

def main():
    fname = input("Enter file name : \n")

    DisplaY(fname)

if __name__ == "__main__":
    main()