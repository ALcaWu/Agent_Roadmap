# ==========================================
# 导入 math 库，用于数学计算
# ==========================================
import math


# ==========================================
# 定义函数：计算余弦相似度
# ==========================================
def cosine_similarity(vec1, vec2):
    """
    计算两个向量之间的余弦相似度
    返回值范围: -1 到 1
    1 表示完全同向（最相似）
    0 表示正交（无关）
    -1 表示完全反向（相反）
    """
    # 检查向量长度是否一致
    if len(vec1) != len(vec2):
        raise ValueError("向量维度必须相同")

    # zip(vec1, vec2): 将两个向量对应位置的元素打包成元组
    # 例如: zip([1,2], [3,4]) -> [(1,3), (2,4)]
    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    # 计算向量模长 (长度)
    # sqrt(a^2 + b^2 + ...)
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))

    # 避免除以零
    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    # 余弦公式: (A . B) / (|A| * |B|)
    return dot_product / (magnitude1 * magnitude2)


# ==========================================
# 主程序入口
# ==========================================
if __name__ == "__main__":
    print("=== 向量相似度演示 ===\n")

    # 模拟 Embedding 向量
    # 注意：真实向量会有几千维，这里为了演示只用3维
    # 假设：
    # 维度1: 是否是水果
    # 维度2: 是否是红色的
    # 维度3: 价格高低

    apple = [0.9, 0.8, 0.3]  # 苹果：是水果，红，便宜
    banana = [0.9, 0.1, 0.2]  # 香蕉：是水果，不红，便宜
    car = [0.0, 0.5, 0.9]  # 汽车：不是水果，可能是红的，贵

    # 1. 计算苹果和香蕉的相似度
    # 预期：很高，因为都是水果
    sim_apple_banana = cosine_similarity(apple, banana)
    print(f"苹果 vs 香蕉: {sim_apple_banana:.4f}")

    # 2. 计算苹果和汽车的相似度
    # 预期：很低，因为类别完全不同
    sim_apple_car = cosine_similarity(apple, car)
    print(f"苹果 vs 汽车: {sim_apple_car:.4f}")

    # 3. 计算香蕉和汽车的相似度
    # 预期：很低
    sim_banana_car = cosine_similarity(banana, car)
    print(f"香蕉 vs 汽车: {sim_banana_car:.4f}")

    print("\n=== RAG 检索模拟 ===")

    # 模拟知识库
    knowledge_base = [
        {"text": "Android是一种移动操作系统", "vector": [0.8, 0.1, 0.2]},
        {"text": "苹果是一种水果", "vector": [0.9, 0.8, 0.3]},
        {"text": "特斯拉是一家电动汽车公司", "vector": [0.1, 0.6, 0.9]},
    ]

    # 用户查询
    query = "我想买水果"
    Query_vector = [0.9, 0.0, 0.2]  # 假设这是查询的向量

    print(f"用户查询: {query}")

    # 遍历知识库，找出最相似的文本
    best_match = None
    best_score = -1

    for item in knowledge_base:
        score = cosine_similarity(Query_vector, item["vector"])
        print(f"  匹配 '{item['text']}': 得分 {score:.4f}")

        # 如果得分更高，更新最佳匹配
        if score > best_score:
            best_score = score
            best_match = item

    print(f"\n🏆 最佳匹配结果: {best_match['text']} (得分: {best_score:.4f})")
