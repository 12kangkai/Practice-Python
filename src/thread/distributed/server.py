from multiprocessing.managers import BaseManager
from queue import Queue

task_queue = Queue()
result_queue = Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)

if __name__ == "__main__":
    manager = QueueManager(address=("0.0.0.0", 50000), authkey=b"123")

    server = manager.get_server()
    print("🚀 Server started at port 50000")

    server.serve_forever()

