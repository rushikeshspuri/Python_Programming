def main():
    try:
        fobj = open("Demo.txt","w")
        print("file gets opened")

        fobj.write("Rushikesh Marvellous Puri...")

        fobj.close()
    
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()