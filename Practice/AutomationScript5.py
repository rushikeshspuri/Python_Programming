import sys

def main():
    print("-"*50)
    print("MARVELLOUS AUTOMATION SCRIPT")
    print("-"*50)
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u Flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] ==  "--U"):
            print("PLease Execute the script as ")
            print("python FileName.py DiretoryName")
            print("Directory name should be absolute path")
        else:
            DirectoryName = sys.argv[1]
            print("Directory name is : ",DirectoryName)
    else: 
        print("Invalid number of arguments")
        print("please --h or --u for more information")

    print("-"*50)
    print("ThankYou for using MARVELLOUS AUTOMATION SCRIPT")
    print("-"*50)

if __name__ == "__main__":
    main()