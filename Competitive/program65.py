def CopyContent(oldfile,newfile):
    try:
        fobj1 = open(oldfile,'r')

        Data1 = fobj1.read()

        fobj2 = open(newfile,'w')

        fobj2.write(Data1)

        fobj1.close()
        fobj2.close()  

        print(f"{oldfile} data copied into {newfile}")     
        
    except FileNotFoundError as fobj1:
        print("404...FILE NOT FOUND\n")

def main():
    Existing = input("Enter existing file name : \n")
    new =  input("Enter new file name : \n")

    CopyContent(Existing,new)

if __name__ == "__main__":
    main()