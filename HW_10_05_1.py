import threading
import random
import time

def fill_list(lst, size):
    for _ in range(size):
        lst.append(random.randint(1,100))
    print("List filled", lst)

def calculate_sum(lst):
    total_sum = sum(lst)
    print("Sum: ", total_sum)

def calculate_average(lst):
    avg = sum(lst) / len(lst)
    print("Avg: ", avg)

def main():
    my_list = []
    t1 = threading.Thread(target=fill_list, args=(my_list, 10))
    t1.start()

    t1.join()

    t2 = threading.Thread(target=calculate_sum, args=(my_list,))
    t2.start()

    t3 = threading.Thread(target=calculate_average, args=(my_list,))
    t3.start()

if __name__ == '__main__':
    main()