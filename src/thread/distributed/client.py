from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

if __name__ =="__main__":
    manager = QueueManager(address=("127.0.0.1", 50000), authkey=b"123")
    manager.connect()

    task_q = manager.get_task_queue()
    result_q = manager.get_result_queue()

    # 提交任务
    for i in range(5):
        task_q.put({
            "id":i,
            "op":"resize"
        })

    # 结束信号
    task_q.put("STOP") # 注意这里只传入了一个STOP信号

    # 收集结果
    for i in range(5):
        result = result_q.get()
        print("📦 result:", result)