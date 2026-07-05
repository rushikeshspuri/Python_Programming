import time
import threading

def SumEven(No):
    print("Tid of Sumeven is : ",threading.get_ident())

def SumOdd(No):
    print("Tid of SumDdd is : ",threading.get_ident())

def main():
    print("Tid of Main thread is : ",threading.get_ident())
    start_time = time.perf_counter()

    t1 = threading.Thread(target=SumEven, args=(1000000,))
    t2 = threading.Thread(target=SumOdd, args=(1000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()  

    print(f"Time Required : {end_time-start_time:.4f}")  

if __name__== "__main__":
    main()