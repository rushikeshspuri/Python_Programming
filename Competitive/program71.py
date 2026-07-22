def Frequency(file,word):
    Count = 0

    try:
        fobj = open(file,'r')

        Data = fobj.read()

        Words = Data.split()

        for i in Words:
            if word == i :
                Count += 1
        
        return Count
    except FileNotFoundError as e:
        print("File not found \n")
    
def main():
    name = input("Enter file name : \n")
    word = input("Enter desired word, to find its frequency \n")

    Ret = Frequency(name,word)

    print(Ret)

if __name__ == "__main__":
    main()