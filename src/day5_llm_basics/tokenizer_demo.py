# ==========================================
# 导入 tiktoken 库
# 这是 OpenAI 官方提供的用于计算 Token 数量的工具
# ==========================================
import tiktoken


# ==========================================
# 定义函数：计算并打印 Token 信息
# ==========================================
def count_tokens(text, model_name="gpt-4o"):
    """
    计算文本的 Token 数量
    text: 输入的文本
    model_name: 模型名称（不同模型使用的编码方式不同）
    """
    print(f"--- 分析文本 (模型: {model_name}) ---")
    print(f"原始文本: {text}")

    # encoding_for_model: 获取指定模型的编码器
    # 类似于获取特定版本的编译器配置
    encoding = tiktoken.encoding_for_model(model_name)

    # encode: 将文本转换为 Token ID 列表
    # 类似于将源代码编译成字节码
    tokens = encoding.encode(text)

    # decode: 将 Token ID 列表还原为文本
    # 类似于反编译或字节码转源码
    decoded_text = encoding.decode(tokens)

    # 打印 Token ID 列表（前10个，避免太长）
    print(f"Token IDs (前10个): {tokens[:10]}...")

    # len(tokens): 计算列表长度，即 Token 数量
    token_count = len(tokens)
    print(f"Token 总数: {token_count}")

    # 计算字符数
    char_count = len(text)
    print(f"字符总数: {char_count}")

    # 计算比例
    ratio = char_count / token_count if token_count > 0 else 0
    print(f"字符/Token 比例: {ratio:.2f} (平均每个Token代表多少个字符)")

    # 简单的费用估算 (假设价格: $0.03 / 1K tokens)
    cost = (token_count / 1000) * 0.03
    print(f"预估输入成本: ${cost:.6f}")

    print("-" * 30 + "\n")


# ==========================================
# 主程序入口
# ==========================================
if __name__ == "__main__":
    # 测试用例 1: 英文
    # 英文通常 1 个单词 ≈ 0.75-1 个 Token
    english_text = "Hello, Android developer! Welcome to the world of AI."
    count_tokens(english_text, "gpt-4o")

    # 测试用例 2: 中文
    # 中文通常 1 个汉字 ≈ 1-2 个 Token (因为中文词汇丰富)
    chinese_text = "你好，Android开发者！欢迎来到人工智能的世界。"
    count_tokens(chinese_text, "gpt-4o")

    # 测试用例 3: 代码
    # 代码通常包含大量空格和符号，Token 数量可能会比字符少
    code_snippet = """
    class Agent:
        def __init__(self, name):
            self.name = name
    """
    count_tokens(code_snippet, "gpt-4o")
