import threading
import time

# custom context manager
class acquire():
    def __init__(self, *locks):
        self.locks = sorted(locks, key=lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, ty, val, tb):
        for lock in reversed(self.locks):
            lock.release()
        return False

# The philospher thread:
def philospher(left, right):
    while True:
        with acquire(left, right):
            print(f"Philospher at {threading.current_thread()} is eating")

N_FORKS = 5

# locks
forks = [threading.Lock() for _ in range(N_FORKS)]

# threads(philosphers)
phils = [threading.Thread(
    target=philospher,
    args=(forks[n], forks[(n + 1) % N_FORKS])
    ) for n in range(N_FORKS)]

start = time.time()

for p in phils:
    p.start()

for p in phils:
    p.join()

print("Took: %0.4f seconds" % (time.time() - start))
