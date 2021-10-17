import asyncio
from math import sqrt
from timeit import default_timer as timer
from concurrent.futures import ProcessPoolExecutor

def is_prime(x):
    print("processing %i..." % x)

    if x < 2:
        print("%i is not a prime number" % x)
    elif x == 2:
        print("%i is a prime number" % x)
    elif x % 2 == 0:
        print("%i is not a prime number" % x)
    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 1):
            if x % i == 0:
                print("%i is not a prime number" % x)
                return
        print("%i is a prime number" % x)

async def main():
    # task1 = loop.run_in_executor(executor, is_prime, 9637529763296797)
    # task2 = loop.run_in_executor(executor, is_prime, 427920331)
    # task3 = loop.run_in_executor(executor, is_prime, 157)
    # await asyncio.gather(*[task1, task2, task3])

    # above things are essentially adding tasks to task queue of event loop and
    # waiting for futures to complete, which could also be written in this way

    res_futures = [loop.run_in_executor(
            executor,
            is_prime,
            args
        ) for args in [9637529763296797, 427920331, 157]]

    # Return the future aggregating results from the given coroutines/futures.
    # Co-routines will be wrapped in a future and scheduled in the event loop,
    # they will not necessarily be scheduled in the same order as passed in.
    # All futures must share the same event loop. If all the tasks are done
    # successfully, returned future's result is a sequence of results (in the
    # order of original sequence, not necessarily in the order of
    # arrival). If 'return_exceptions' is True, exceptions in the tasks
    # are treated the same as successful result, and gathered in the result
    # list, otherwise, the first raised exception will be propagated to the
    # returned future.
    # Cancellation: if the outer Future is cancelled, all the children (that
    # have not completed yet) are also cancelled. If any child is
    # cancelled, this is treated as if it raised CancelledError -- the outer
    # future is 'not' cancelled in this case. (This is to prevent the
    # cancellation of one child to cause other children to be
    # cancelled)
    await asyncio.gather(*res_futures)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        start = timer()
        executor = ProcessPoolExecutor(max_workers=3)
        loop.run_until_complete(main())
        print('Took %0.4f seconds' % (timer() - start))
    except Exception as e:
        print("Problem occured:", str(e))
    finally:
        loop.close()

# AbstractEventLoop.run_in_executor(): takes in an executor, a coroutine
# (though, again it doesn't have to be actual coroutine), and arguments for the
# coroutines to be executed in seperate thread/process
