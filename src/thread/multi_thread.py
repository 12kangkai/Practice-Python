import threading
import time

# 多线程示例：多个线程同时执行任务，并安全访问共享资源


def worker(thread_id, lock, counter):
    for i in range(3):
        time.sleep(0.5)
        with lock:
            counter[0] += 1
            print(f"线程 {thread_id} 第 {i + 1} 次运行，计数器值：{counter[0]}")


if __name__ == "__main__":
    lock = threading.Lock()
    shared_counter = [0]  # 使用可变对象让线程间共享数据

    threads = []
    for thread_num in range(1, 4):
        thread = threading.Thread(target=worker, args=(thread_num, lock, shared_counter))
        threads.append(thread)
        thread.start()
        print(f"主线程：已启动线程 {thread_num}")

    for thread in threads:
        thread.join()

    print("所有线程已完成，最终计数器值：", shared_counter[0])
