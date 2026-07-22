def Display(Fname):
    try:
        fobj = open(Fname,'r')

        Data = fobj.readlines()

        for lines in Data:
            print(lines)

    except FileNotFoundError as fobj:
        print("404...FILE NOT FOUND\n")

def main():
    name = input("Enter file name to see it contains : \n")

    Display(name)

if __name__ == "__main__":
    main()