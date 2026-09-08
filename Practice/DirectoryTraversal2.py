import  os

def main():
    for FolderName,SubFolder,FileName in os.walk("Marvellous"):
        print("Folder name : ",FolderName)

        for SubF in SubFolder:
            print("Subfolder name : ",SubF)


if __name__ == "__main__":
    main()