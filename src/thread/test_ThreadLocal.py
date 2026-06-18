import threading
import time

thread_local_data = threading.local()


def worker(name):
    thread_local_data.name = name
    time.sleep(0.1)
    print(f"Thread {threading.current_thread().name} has name {thread_local_data.name}")


if __name__ == "__main__":
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(f"worker-{i}",), name=f"T{i}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
