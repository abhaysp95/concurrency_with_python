import threading

# the philospher thread
def philospher(left, right):
    while True:
        with left:
            with right:
                print(f"Philospher at {threading.current_thread()} is eating")


N_FORKS = 5

# locks
forks = [threading.Lock() for _ in range(N_FORKS)]

# create all the philosphers(threads)
phils = [threading.Thread(
    target=philospher,
    args=(forks[n], forks[(n + 1) % N_FORKS])
    ) for n in range(N_FORKS)]

# start the philosphers
for p in phils:
    p.start()

for p in phils:
    p.join()
