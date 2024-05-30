import threading
import random
import math

def fill_file(filename, size):
    with open(filename, 'w') as f:
        for _ in range(size):
            f.write(str(random.randint(1, 100)) + '\n')
    print("File filled:", filename)

def find_primes(filename, output_filename):
    primes = []
    with open(filename, 'r') as f:
        for line in f:
            number = int(line.strip())
            if is_prime(number):
                primes.append(number)
    write_to_file(output_filename, primes)
    print("Primes found:", len(primes))

def find_factorials(filename, output_filename):
    factorials = []
    with open(filename, 'r') as f:
        for line in f:
            number = int(line.strip())
            factorials.append(math.factorial(number))
    write_to_file(output_filename, factorials)
    print("Factorials found")

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def write_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(str(item) + '\n')

def main():
    filename = input("Enter the path to the file: ")

    t1 = threading.Thread(target=fill_file, args=(filename, 10))
    t1.start()

    t1.join()

    t2 = threading.Thread(target=find_primes, args=(filename, "primes.txt"))
    t2.start()

    t3 = threading.Thread(target=find_factorials, args=(filename, "factorials.txt"))
    t3.start()

if __name__ == "__main__":
    main()