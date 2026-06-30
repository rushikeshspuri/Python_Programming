def DisplayGrade(Marks):
    if(Marks >= 75):
        print(f"you achived Distinction for {Marks}")
    elif(Marks >= 60):
        print(f"you achived First Class for {Marks}")
    elif(Marks >= 50):
        print(f"you achived Second Class for {Marks}")
    else:
        print(f"You are Failed for {Marks}")

def main():
    print("Enter Marks to Check the grade")
    value = int(input())

    DisplayGrade(value)

if __name__ =="__main__":
    main()