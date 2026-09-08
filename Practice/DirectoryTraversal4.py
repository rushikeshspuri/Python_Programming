import  os

def main():
    for FolderName,SubFolder,FileName in os.walk("Marvellous"):

        for Fname in FileName:
            print("File name :",FileName)

if __name__ == "__main__":
    main()