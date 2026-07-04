# using time module in which using perf_counter method , prefer this method

import time

def Factorial(No):
    Fact = 1

    for i in range(1,No +1):
        Fact = Fact * i

    return Fact

def main():
    print("Enter number")
    value =  int(input())

    start_time = time.perf_counter()

    Ret = Factorial(value)

    end_time = time.perf_counter()

    print(f"Factorial of {value} is : {Ret} ")
    print(f"Time Required is : {end_time - start_time:.5f} seconds")


if __name__ == "__main__":
    main()