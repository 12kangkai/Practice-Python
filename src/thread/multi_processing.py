"""
Python 多进程教学代码
演示如何使用 multiprocessing 模块进行多进程编程
"""

import multiprocessing
import time
from multiprocessing import Pool, Process, Queue, Pipe, Manager


# 示例 1: 基础进程创建
def worker(name, value):
    """工作函数"""
    time.sleep(1)
    print(f"进程 {name} 执行，值: {value}")


def example_basic_process():
    """基础进程示例"""
    print("=== 基础进程示例 ===")
    p1 = Process(target=worker, args=("P1", 10))
    p2 = Process(target=worker, args=("P2", 20))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print("所有进程完成\n")


# 示例 2: 进程池 (Pool)
def task(x):
    """任务函数"""
    time.sleep(0.5)
    return x * x


def example_pool():
    """进程池示例"""
    print("=== 进程池示例 ===")
    with Pool(processes=4) as pool:
        results = pool.map(task, range(10))
        print(f"结果: {results}\n")


# 示例 3: 队列 (Queue) 进程通信
def producer(queue):
    """生产者进程"""
    for i in range(5):
        queue.put(f"数据 {i}")
        time.sleep(0.5)


def consumer(queue):
    """消费者进程"""
    while True:
        data = queue.get()
        if data is None:
            break
        print(f"消费: {data}")


def example_queue():
    """队列通信示例"""
    print("=== 队列通信示例 ===")
    q = Queue()
    
    p_producer = Process(target=producer, args=(q,))
    p_consumer = Process(target=consumer, args=(q,))
    
    p_producer.start()
    p_consumer.start()
    
    p_producer.join()
    q.put(None)
    p_consumer.join()
    print()


# 示例 4: 管道 (Pipe) 进程通信
def sender(conn):
    """发送端"""
    for i in range(5):
        conn.send(f"消息 {i}")
        time.sleep(0.3)
    conn.close()


def receiver(conn):
    """接收端"""
    while True:
        try:
            msg = conn.recv()
            print(f"接收: {msg}")
        except EOFError:
            break


def example_pipe():
    """管道通信示例"""
    print("=== 管道通信示例 ===")
    parent_conn, child_conn = Pipe()
    
    p_sender = Process(target=sender, args=(child_conn,))
    p_receiver = Process(target=receiver, args=(parent_conn,))
    
    p_sender.start()
    p_receiver.start()
    
    p_sender.join()
    p_receiver.join()
    print()


# 示例 5: 共享资源 (Manager)
def increment_counter(manager_dict, key, times):
    """增加计数器"""
    for _ in range(times):
        manager_dict[key] += 1
        time.sleep(0.1)


def example_manager():
    """Manager 共享资源示例"""
    print("=== Manager 共享资源示例 ===")
    with Manager() as manager:
        shared_dict = manager.dict()
        shared_dict['counter'] = 0
        
        processes = [
            Process(target=increment_counter, args=(shared_dict, 'counter', 5))
            for _ in range(3)
        ]
        
        for p in processes:
            p.start()
        
        for p in processes:
            p.join()
        
        print(f"最终计数器值: {shared_dict['counter']}\n")


# 示例 6: 进程结果返回 (apply_async)
def calculate(x):
    """计算函数"""
    time.sleep(1)
    return x * 2


def example_apply_async():
    """异步执行示例"""
    print("=== 异步执行示例 ===")
    with Pool(processes=2) as pool:
        results = []
        for i in range(5):
            result = pool.apply_async(calculate, (i,))
            results.append(result)
        
        for i, result in enumerate(results):
            print(f"结果 {i}: {result.get()}")
    print()


if __name__ == '__main__':
    # 运行所有示例
    example_basic_process()
    example_pool()
    example_queue()
    example_pipe()
    example_manager()
    example_apply_async()
