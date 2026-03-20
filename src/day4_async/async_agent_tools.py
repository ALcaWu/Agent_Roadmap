# ==========================================
# 导入必要的库
# ==========================================
import asyncio  # 导入Python的异步I/O库（核心库）
import random  # 导入随机数库，用于模拟不确定的耗时
import time  # 导入时间库，用于计算程序运行总时长


# ==========================================
# 定义 AgentTools 类
# 作用：模拟 Agent 可以使用的各种外部工具（搜索引擎、数据库、计算器）
# ==========================================
class AgentTools:
    """Agent工具类：包含各种耗时操作"""

    # 定义异步方法 search_web
    # async 关键字：告诉 Python 这是一个协程函数（类似 Kotlin 的 suspend fun）
    # 调用这个函数不会立即执行，而是返回一个协程对象
    async def search_web(self, query):
        """模拟网络搜索 (耗时 1-2秒)"""

        # random.uniform(1.0, 2.0) 生成 1.0 到 2.0 之间的随机浮点数
        # 模拟网络请求的随机延迟
        delay = random.uniform(1.0, 2.0)

        # await asyncio.sleep(delay)
        # await 关键字：表示"等待"这个操作完成
        # asyncio.sleep(delay) 是一个非阻塞的延迟函数（类似 Kotlin 的 delay）
        # 当程序运行到这一行时，它会挂起当前协程，把控制权交还给事件循环，
        # 让事件循环去执行其他任务。延迟结束后，再回到这里继续执行。
        await asyncio.sleep(delay)

        # 返回结果字符串
        return f"搜索结果: 关于'{query}'找到了5个相关网页"

    # 定义异步方法 query_database
    async def query_database(self, sql):
        """模拟数据库查询 (耗时 0.5-1秒)"""
        # 模拟数据库查询的随机延迟
        delay = random.uniform(0.5, 1.0)

        # 挂起当前协程，等待延迟结束
        await asyncio.sleep(delay)

        # 返回查询结果
        return f"数据库查询结果: {sql} -> 返回10行数据"

    # 定义异步方法 calculate_math
    async def calculate_math(self, expression):
        """模拟复杂计算 (耗时 0.2-0.5秒)"""
        # 模拟计算的随机延迟
        delay = random.uniform(0.2, 0.5)

        # 挂起当前协程
        await asyncio.sleep(delay)

        # 返回计算结果
        return f"计算结果: {expression} = 42"


# ==========================================
# 定义 AsyncAgent 类
# 作用：模拟一个智能体，它能够并发调度上面的工具来完成任务
# ==========================================
class AsyncAgent:
    """异步 Agent：能够并发调用工具"""

    # 构造函数
    def __init__(self):
        # 初始化工具实例，这样 Agent 就可以使用这些工具了
        self.tools = AgentTools()

    # 定义核心处理方法 process_query
    async def process_query(self, user_query):
        """处理用户查询 - 并发调用所有工具"""

        # 打印开始处理的日志
        print(f"🤖 Agent 正在处理查询: {user_query}")

        # 记录开始时间，用于计算总耗时
        start_time = time.time()

        # ==========================================
        # 核心逻辑：并发执行 (重点！)
        # ==========================================

        # asyncio.gather(...)
        # 这是实现并发的关键。它接受多个协程对象作为参数。
        # 它会同时启动这些协程，并等待它们全部完成。
        # 类似于 Kotlin 中的: val results = awaitAll(async1, async2, async3)

        # 这里我们传入了三个任务：
        # 1. self.tools.search_web(user_query)  -> 搜索工具
        # 2. self.tools.query_database(...)     -> 数据库工具
        # 3. self.tools.calculate_math(...)     -> 计算工具
        results = await asyncio.gather(
            self.tools.search_web(user_query),
            self.tools.query_database(
                f"SELECT * FROM knowledge WHERE topic='{user_query}'"
            ),
            self.tools.calculate_math("100 * 0.42"),
        )

        # 记录结束时间
        end_time = time.time()

        # 打印总耗时
        # 你会发现这个时间接近于最慢的那个任务（约2秒），而不是三个任务时间的总和（约3秒）
        print(f"✅ 所有工具执行完毕，总耗时: {end_time - start_time:.2f} 秒")

        # ==========================================
        # 结果整合
        # ==========================================

        # results 是一个列表，包含了 gather 中所有任务的返回值
        # results[0] 是 search_web 的返回值
        # results[1] 是 query_database 的返回值
        # results[2] 是 calculate_math 的返回值

        # 拼接最终的回答字符串
        final_answer = f"""
        === Agent 最终回答 ===
        1. {results[0]}
        2. {results[1]}
        3. {results[2]}
        
        综合以上信息，为您解答关于 '{user_query}' 的问题。
        """

        # 返回最终答案
        return final_answer


# ==========================================
# 定义 main 函数
# 作用：程序的入口，模拟用户发送多个请求
# ==========================================
async def main():
    """主函数"""

    # 创建 Agent 实例
    agent = AsyncAgent()

    # 定义一个包含多个用户问题的列表
    queries = ["什么是人工智能?", "Python异步编程的优势", "Agent开发最佳实践"]

    # ==========================================
    # 外层循环：串行处理每个用户问题
    # ==========================================

    # for 循环遍历每个问题
    # 注意：这里我们使用普通的 for 循环，意味着 Agent 处理完第一个问题后，才会处理第二个。
    # 但在处理每个问题内部（process_query 函数内），工具的调用是并发的。
    for q in queries:
        # 打印分隔线
        print("\n" + "=" * 50)

        # 调用 Agent 的处理方法
        # await 表示等待当前问题处理完成
        answer = await agent.process_query(q)

        # 打印答案
        print(answer)

        # 稍微等待一下，模拟用户思考时间
        await asyncio.sleep(0.5)


# ==========================================
# 程序执行入口
# ==========================================
if __name__ == "__main__":
    # asyncio.run(main())
    # 这是启动 Python 异步程序的标准方式。
    # 它负责创建事件循环，运行 main() 协程，并在结束后关闭循环。
    # 类似于 Kotlin 中的: runBlocking { main() }
    asyncio.run(main())


# 1. 程序启动
#    └─> asyncio.run(main())

# 2. 进入 main() 函数
#    └─> 遍历问题列表 [问题1, 问题2, ...]

# 3. 处理 "问题1" (串行开始)
#    └─> agent.process_query("问题1")
#        └─> asyncio.gather( 任务A, 任务B, 任务C )  <-- 并发点！
#            ├─> 任务A (搜索) ... 等待 1.5秒 ...
#            ├─> 任务B (查库) ... 等待 0.8秒 ...
#            └─> 任务C (计算) ... 等待 0.3秒 ...
#        └─> [结果A, 结果B, 结果C] (全部完成，耗时约 1.5秒)
#    └─> 返回答案

# 4. 处理 "问题2" (串行继续)
#    └─> ... 重复上述流程 ...
