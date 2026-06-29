"""

Python 协程 asyncio 教学代码

重点理解：

1. async def：定义协程函数

2. await：暂停当前协程，把执行权还给事件循环

3. asyncio.run：启动事件循环

4. asyncio.create_task：创建并发任务

5. asyncio.gather：并发等待多个任务完成

6. task.cancel：取消任务

"""

import asyncio
import time



# ------------------------------------------------------------
# 1. 普通函数：调用后立即执行
# ------------------------------------------------------------
def normal_func():
    print("[普通函数] 开始执行")
    print("[普通函数] 执行结束")

# ------------------------------------------------------------
# 2. 协程函数：async def 定义
# ------------------------------------------------------------
async def coroutine_func():
    """
    async def 定义的是“协程函数”

    注意：
    调用 coroutine_func()时，函数体不会立刻执行
    而是返回一个coroutine协程对象

    必须通过：
    1. await coroutine_func()
    2. asyncio.run(coroutine_func())
    3. asyncio.create_task(cotoutine_func())

    才会真正执行
    """
    print("[协程函数] 开始执行")
    print("[协程函数] 执行结束")


# -----------------------------------------------------------
# 3. await：等待协程完成
# ------------------------------------------------------------
async def get_data():
    print("[get_data] 开始获取数据")

    # 关键点：await asyncio.sleep(1) 不会阻塞线程。
    # 它表示：当前协程暂停1秒。把执行权交还给事件循环

    # 事件循环可以趁这个等待时间去执行其他协程
    await asyncio.sleep(1)

    print("[get_data] 数据获取完成")
    return "这是数据"

async def await_demo():
    print("\n========== await 示例 ==========")

    # await 的作用：
    # 1.等待 get_data() 执行完成 
    # 2. 拿到get_data() 的返回值 
    # 3. 等待期间，当前协程可以暂停，让事件循环去调度其他协程
    result = await get_data()

    print("[await_demo] 获取到结果：", result)


# ------------------------------------------------------------
# 4. 顺序执行：总耗时 = 任务1 + 任务2
# ------------------------------------------------------------
async def show_task(name, delay):
    print(f"[{name}] 开始，预计耗时{delay}秒")

    # 这里模拟 I/O 等待，例如：网络请求、数据库查询、设备响应、文件读取等
    await asyncio.sleep(delay)

    print(f"[{name}] 结束")
    return f"{name} 的结果"

async def sequential_demo():
    print("\n========== 顺序执行示例 ==========")

    start = time.perf_counter()

    # 这里是顺序执行： 必须等A完成后，才会执行B
    result_a = await show_task("任务A", 2)
    result_b = await show_task("任务B", 1)

    end = time.perf_counter()

    print("[sequential_demo] 结果：", result_a, result_b)
    print(f"[sequential_demo] 总耗时：{end - start:.2f} 秒")

# ------------------------------------------------------------
# 5. create_task：创建并发任务
# ------------------------------------------------------------
async def create_task_demo():
    print("\n========== create_task 并发示例 ==========")

    start = time.perf_counter()

    # 关键点：asyncio.create_task 会把协程包装成 Task，并提交给事件循环调度。
    # 这意味着任务A和任务B 会尽快开始执行，不需要等待A完成后再开始B
    task_a = asyncio.create_task(show_task("任务A",2))
    task_b = asyncio.create_task(show_task("任务B",1))

    # 注意：create_task 只是创建任务，不代表这里立刻拿到了结果
    # 如果要拿到结果，仍然需要 await task
    result_a = await task_a
    result_b = await task_b

    end = time.perf_counter()

    print("[create_task_demo] 结果:", result_a, result_b)

    # 因为 A 和 B 并发执行，所以总耗时约等于最大任务耗时 2 秒，
    # 而不是 2 + 1 = 3 秒。
    print(f"[create_task_demo] 总耗时：{end - start:.2f} 秒")



# ------------------------------------------------------------
# 6. gather:并发运行多个协程，并等待全部完成
# ------------------------------------------------------------
async def gather_demo():
    print("\n========== gather 并发示例 ==========")

    start = time.perf_counter()

    # gather适合这种场景：
    # 我有一组协程任务，我希望它们并发执行 
    # 并且等待它们全部完成后拿到结果列表

    results = await asyncio.gather(
        show_task("任务A", 2),
        show_task("任务B", 1),
        show_task("任务C", 3)
    )

    end = time.perf_counter()

    print("[gather_demo] 所有结果:", results)
    # 总耗时约等于最长任务的耗时，也就是3s
    print(f"[gether_demo] 总耗时：{end - start:.2f} 秒")

# ------------------------------------------------------------
# 7. 错误示例：在协程里使用 time.sleep
# ------------------------------------------------------------
async def bad_sleep_task(name, delay):
    print(f"[{name}] 开始 bad sleep")

    # 错误示范：
    # time.sleep 会阻塞当前线程。
    # 因为 asyncio 的事件循环通常运行在单线程中
    # 所以这里会把整个事件循环卡住
    # 其他协程也无法继续执行
    time.sleep(delay)
    print(f"[{name}] 结束 bad sleep")

async def good_sleep_task(name, delay):
    print(f"[{name}] 开始 good sleep")

    # 正确写法：
    # asyncio.sleep 是异步等待
    # 当前协程暂停，但事件循环不会被阻塞
    await asyncio.sleep(delay)

    print(f"[{name}] 结束 good sleep")

async def sleep_compare_demo():
    print("\n========== time.sleep vs asyncio.sleep 示例 ==========")

    print("\n--- 错误示例：time.sleep 会阻塞事件循环 ---")
    start = time.perf_counter()

    await asyncio.gather(
        bad_sleep_task("bad-A", 2),
        bad_sleep_task("bad-B", 2),
    )

    end = time.perf_counter()
    print(f"[bad sleep] 总耗时: {end - start:.2f} 秒")
    print("说明：两个任务看似 gather 并发，但 time.sleep 阻塞了事件循环，所以接近 4 秒。")

    print("\n--- 正确示例：asyncio.sleep 不阻塞事件循环 ---")
    start = time.perf_counter()

    await asyncio.gather(
        good_sleep_task("good-A", 2),
        good_sleep_task("good-B", 2)
    )

    end = time.perf_counter()
    print(f"[good sleep] 总耗时: {end - start:.2f} 秒")
    print("说明：两个任务真正并发等待，所以接近 2 秒。")


# ------------------------------------------------------------
# 8. 协程异常处理
# ------------------------------------------------------------
async def error_task():
    print("[error_task] 开始")
    await asyncio.sleep(1)

    # 协程中的异常和普通函数一样， 可以 raise
    raise ValueError("模拟协程执行异常")

async def exception_demo():
    print("\n========== 协程异常处理示例 ==========")

    try:
        await error_task()
    except ValueError as ex:
        print("[exception_demo] 捕获到异常：", ex)


# ------------------------------------------------------------
# 9. 取消任务
# ------------------------------------------------------------
async def long_running_task():
    try:
        print("[long_running_task] 开始执行")

        # 模拟一个长时间任务
        for i in range(10):
            print(f"[long_running_task] 正在执行第 {i + 1} 步")
            await asyncio.sleep(1)

        print("[long_running_task] 正常结束")
    except asyncio.CancelledError:
        # 关键点：
        # task.cancel() 不是强制杀死任务
        # 它会在协程下一次await 恢复时，向协程内部抛出 CancelledError
        # 所以协程可以在这里做清理工作，例如：
        # 释放资源、记录日志、回滚状态等
        print("[long_running_task] 收到取消信号，开始清理资源")

        # 一般建议重新 raise 让外层知道任务确实被取消了
        raise

async def cancel_demo():
    print("\n========== 取消任务示例 ==========")

    task = asyncio.create_task(long_running_task())

    # 让任务先执行3s
    await asyncio.sleep(3)

    print("[cancel_demo] 准备取消任务")

    # 发出取消请求
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("[cancel_demo] 确认任务已取消")


# ------------------------------------------------------------
# 10. async for：异步迭代
# ------------------------------------------------------------
class AsyncCounter:
    """
    自定义异步迭代器。

    普通 for 使用：
        __iter__
        __next__

    async for 使用
        __aiter__
        __anext__
    """

    def __init__(self, max_count):
        self.current = 0
        self.max_count = max_count

    def __aiter__(self):
        # 返回异步迭代器对象本身
        return self
    
    async def __anext__(self):
        # 如果没有更多数据， 抛出StopAsyncIteration
        if self.current >= self.max_count:
            raise StopAsyncIteration
        
        # 模拟异步获取下一个数据
        await asyncio.sleep(1)

        self.current += 1
        return self.current
    
async def async_for_demo():
    print("\n========== async for 示例 ==========")

    # async for 用于遍历“异步产生数据” 的对象
    # 比如：
    # 分页读取远程数据
    # 异步读取消息队列
    # 异步读取网络流
    async for number in AsyncCounter(3):
        print("[async_for_demo] 获取到：", number)


# ------------------------------------------------------------
# 11. async with：异步上下文管理器
# ------------------------------------------------------------
class AsyncResource:
    """
    自定义异步上下文管理器

    普通 with 使用：
        __enter__
        __exit__

    async with 使用：
        __aenter__
        __aexit__
    """
    async def __aenter__(self):
        # 进入资源时可能需要异步操作
        # 比如打开连接、建立会话、申请远程资源等
        print("[AsyncResource] 异步打开资源等")
        await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        # 退出资源时也可能需要异步操作
        #比如关闭连接、提交事务、释放远程连接等
        print("[AsyncResource] 异步释放资源")
        await asyncio.sleep(1)

async def async_with_demo():
    print("\n========== async with 示例 ==========")

    async with AsyncResource():
        print("[async_with_demo] 正在使用资源")




# ------------------------------------------------------------
# 12. 主入口
# ------------------------------------------------------------
async def main():
    """
    main 本身也是一个协程函数

    asyncio.run(main())会启动事件循环，并运行main
    """
    # print("========== 普通函数 vs 协程函数 ==========")

    # # 普通函数：调用后立即执行
    # normal_func()

    # # 协程函数：调用后不会立即执行，而是得到一个协程对象
    # coro = coroutine_func()
    # print("[main] 调用 coroutine_func() 后得到:", coro)

    # # 真正执行协程，需要 await
    # await coro

    # await await_demo()
    # await sequential_demo()
    # await create_task_demo()
    # await gather_demo()
    # await sleep_compare_demo()
    # await exception_demo()
    # await cancel_demo()
    # await async_for_demo()
    await async_with_demo()


if __name__ == "__main__":
    asyncio.run(main())

    
