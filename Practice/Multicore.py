import os  # important module named as os and sys

def main():
    print("Number of cores are : ",os.cpu_count())

if __name__=="__main__":
    main()