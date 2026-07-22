def SearchWord(FName,word):
    try:
        fobj = open(FName,'r')

        Data = fobj.read()

        if word in Data:
            return True
        else:
            return False
        
    except FileNotFoundError as fobj:
        print("FILE NOT FOUND")


def main():
    Name = input("Enter the file name \n")
    Word = input("Enter the word you want to search \n")

    Ret = SearchWord(Name,Word)

    if(Ret == True):
        print(f"{Word} is present in {Name}")
    else:
        print(f"{Word} is not present in {Name}")

if __name__ == "__main__":
    main()