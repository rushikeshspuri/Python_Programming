# using time module in which using time method

import time

def Factorial(No):
    Fact = 1

    for i in range(1,No +1):
        Fact = Fact * i

    return Fact

def main():
    print("Enter number")
    value =  int(input())

    start_time = time.time()

    Ret = Factorial(value)

    end_time = time.time()

    print(f"Factorial of {value} is : {Ret} ")
    print(f"Time Required is : {end_time - start_time} seconds")


if __name__ == "__main__":
    main()