from multiprocessing.managers import BaseManager
import time

class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

if __name__ == "__main__":
    manager = QueueManager(address=("127.0.0.1",50000), authkey=b"123")
    manager.connect()

    task_q = manager.get_task_queue()
    result_q = manager.get_result_queue()

    print("🟢 Worker started...")

    while True:
        task = task_q.get() #阻塞等待任务

        if task == "STOP":
            break

        image_id = task["id"]
        op = task["op"]

        print(f"⚙️ processing {image_id} with {op}")

        # 模拟处理耗时
        time.sleep(1)

        result = {
            "id":image_id,
            "status":"done",
            "op":op
        }

        result_q.put(result)
