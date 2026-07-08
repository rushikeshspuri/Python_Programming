def Add(No1, No2):
    return No1 + No2

def main():
    print("Enter first Number")
    No1  = int(input())

    print("Enter secont Number")
    No2  = int(input())
    
    Ret = Add(No1,No2)

    print(f"Addition is {Ret}")
        
if __name__ == "__main__":
    main()
