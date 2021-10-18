from math import sqrt

import asyncio

async def is_prime(x):
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
            elif i % 100000 == 1:
                # print("here")
                await asyncio.sleep(0)
        print("%i is a prime number" % x)

async def main():
    task1 = loop.create_task(is_prime(9637529763296797))
    task2 = loop.create_task(is_prime(4279203319283))
    task3 = loop.create_task(is_prime(427920331928))
    task4 = loop.create_task(is_prime(1579023845))
    task5 = loop.create_task(is_prime(427920331))
    task6 = loop.create_task(is_prime(3948923))
    task7 = loop.create_task(is_prime(23939))
    task8 = loop.create_task(is_prime(157))

    await asyncio.wait([task1, task2, task3, task4, task5, task6, task7, task8,])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except Exception as e:
        print("Problem encountered:", str(e))
    finally:
        loop.close()
