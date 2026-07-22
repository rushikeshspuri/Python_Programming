import os

def CheckFile(Name):
    if os.path.exists(Name):
        print("File exists")
    else:
        print("File does not exist")

def main():
    name = input("Enter file name : \n")

    CheckFile(name)

if __name__ == "__main__":
    main()