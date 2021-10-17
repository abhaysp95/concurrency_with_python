import multiprocessing as mp
import time

class ReductionConsumer(mp.Process):
    def __init__(self, task_queue, result_queue):
        mp.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        pname = self.name

        while True:
            num1 = self.task_queue.get()
            if num1 is None:
                print("Exiting process %s" % pname)
                self.task_queue.task_done()
                break
            self.task_queue.task_done()

            num2 = self.task_queue.get()
            if num2 is None:
                print("Reaching the end with process %s and number %i" % (pname, num1))
                self.task_queue.task_done()
                self.result_queue.put(num1)
                break

            print("Running process %s on number %i and %i" % (pname, num1, num2))
            self.task_queue.task_done()
            self.result_queue.put(num1 + num2)

def reduce_sum(arr):
    tasks = mp.JoinableQueue()
    results = mp.JoinableQueue()

    n_consumers = mp.cpu_count()

    result_size = len(arr)

    for x in arr:
        results.put(x)

    while result_size > 1:
        tasks = results
        results = mp.JoinableQueue()

        consumers = [ReductionConsumer(tasks, results) for _ in range(n_consumers)]

        for consumer in consumers:
            consumer.start()

        for _ in range(n_consumers):
            tasks.put(None)

        tasks.join()
        result_size = result_size // 2 + (result_size % 2)
        print('-' * 40)

    return results.get()

def reduce_sequentially(arr):
    new_arr = arr
    old_arr = []
    n_len = len(arr)

    while n_len > 1:
        # print("old arr:", old_arr)
        # print("new_arr:", new_arr)
        old_arr = new_arr
        new_arr = []
        n_old_arr = len(old_arr)
        for i in range(0, len(old_arr), 2):
            if i == n_old_arr - 1:
                new_arr.append(old_arr[i])
                break;
            new_arr.append(old_arr[i] + old_arr[i + 1])
        n_len = n_len // 2 + (n_len % 2)
    return new_arr[0]

if __name__ == "__main__":
    my_arr = [i for i in range(1000000000 + 1)]
    start = time.time()
    # res = reduce_sum(my_arr)
    res = reduce_sequentially(my_arr)
    end = time.time() - start
    print("Final result:", res)
    print(f"Total time taken {end: 0.4f}")
