from math import sqrt

import asyncio
import time

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
    # AbstractEventLoop.create_task(): schedule a coroutine object, return a
    # task object
    # this method is called by an event loop. It adds input to the current task
    # queue of the calling event loop; the input is typically a coroutine (a
    # function with async keyword)
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
    # Return an asyncio event loop
    # When called from routine or callback (eg., scheduled with call_back or
    # similar API), this function will always return the running event
    # loop
    # If there is no running event loop set, the function will return the
    # result of 'get_event_loop_policy().get_event_loop()' call
    loop = asyncio.get_event_loop()
    try:
        start = time.time()
        # Run until the Future is done
        # If the argument is coroutine, it is wrapped in a task
        # It takes in main coroutine of an asynchronous program and executes
        # until the corresponding future for the coroutine is returned. While
        # method initiates the event loop execution, it also blocks all
        # subsequent code following it, until the futures are complete
        loop.run_until_complete(main())
        print("took: %0.4f seconds" % (time.time() - start))
    except Exception as e:
        print("Problem encountered:", str(e))
    finally:
        loop.close()

## Some other methods:
# AbstractEventLoop.run_forever(): somewhat similar to 'run_until_complete()'
# except that the calling event loop will run forever (even after the
# completion of all futures), unless the 'AbstractEventLoop.stop()' is
# called.
# AbstractEventLoop.stop(): the method causes the calling event loop to stop
# execution and exit at nearest appropriate oppurtunity, without causing whole
# program to crash
# asyncio.sleep(): while in itself a coroutine, the function itself creates an
# additional coroutine that completes after a given time (mentioned as its
# argument). It is typically used as 'asyncio.sleep(0)' to cause an
# immediate task switching event
# asyncio.wait(): this function is also a coroutine, hence it used to switch
# tasks. It takes in a sequence (usually a list) of futures and wait for them
# to complete their execution
