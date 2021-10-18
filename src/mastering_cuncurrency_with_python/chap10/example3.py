from math import sqrt

import time

def is_prime(x):
    print("Processing %i..." % x)

    if x < 2:
        print("%i is not a prime number" % x)
    elif x == 2:
        print("%i is a prime number" % x)
    elif x % 2 == 0:
        print("%i is a not prime number" % x)
    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 1):
            if x % i == 0:
                print("%i is a prime number" % x)
                return
        print("%i is a prime number" % x)

if __name__ == "__main__":
    start = time.time()
    is_prime(9637529763296797)
    is_prime(4279203319283)
    is_prime(427920331928)
    is_prime(1579023845)
    is_prime(427920331)
    is_prime(3948923)
    is_prime(23939)
    is_prime(157)
    print("took: %0.4f seconds" % (time.time() - start))
