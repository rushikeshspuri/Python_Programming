import sys

def CompareX(file1,file2):
    try:
        fobj1 = open(file1,'r')

        Data1 = fobj1.read()

        fobj2 = open(file2,'r')

        Data2 = fobj2.read()

        if(Data1 == Data2):
            return True
        else:
            return False
            
    except FileNotFoundError as e:
        print("File not found \n")

def main():
    if(len(sys.argv) == 3):
        file1 = sys.argv[1]
        file2 = sys.argv[2]

    Ret = CompareX(file1,file2)

    if(Ret == True):
        print("SUCCESS\n")
    else:
        print("FAILURE\n")


if __name__ == "__main__":
    main()