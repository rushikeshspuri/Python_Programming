import sys

def Copy(f1,f2):
    try:
        fobj1 = open(f1,'r')

        Data = fobj1.read()

        fobj2 = open(f2,'w')

        fobj2.write(Data)

        print(f"{f1} gets copied into {f2}\n")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError as e:
        print("FILE NOT FOUND\n")

def main():

    old = sys.argv[1]
    new =  input("Enter new file name\n")

    Copy(old,new)

if __name__ == "__main__":
    main()