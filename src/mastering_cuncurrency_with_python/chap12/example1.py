import threading
import time

def thread_a():
    print("Thread A is starting...")

    print("Thread A is waiting to acquire lock A")
    lock_a.acquire()
    print("Thread A acquired lock A, performing some calculations...")

    time.sleep(2)

    print("Thread A is waiting to acquire lock B")
    lock_b.acquire()
    print("Thread A acquired lock b, performing some calculations...")

    time.sleep(2)

    print("Thread A releasing both locks")
    lock_a.release()
    lock_b.release()

def thread_b():
    print("Thread B is starting...")

    print("Thread B is waiting to acquire lock B")
    lock_b.acquire()
    print("Thread B acquired lock B, performing some calculations...")

    time.sleep(2)

    print("Thread B is waiting to acquire lock A")
    lock_a.acquire()
    print("Thread B acquired lock A, performing some calculations...")

    time.sleep(2)

    print("Thread B releasing both locks")
    lock_a.release()
    lock_b.release()


lock_a = threading.Lock()
lock_b = threading.Lock()

thread1 = threading.Thread(target=thread_a)
thread2 = threading.Thread(target=thread_b)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done")
