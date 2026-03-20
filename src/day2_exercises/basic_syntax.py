# basic_syntax.py - Python基础语法练习
import random

def main():
    """主函数"""
    print("=== Python基础语法练习 ===")
    
    # 1. 变量定义
    print("\n1. 变量定义:")
    name = "Python Learner"
    age = 25
    height = 1.75
    is_learning = True
    
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"身高: {height}")
    print(f"是否在学习: {is_learning}")
    
    # 2. 数据类型
    print("\n2. 数据类型:")
    print(f"name的类型: {type(name)}")
    print(f"age的类型: {type(age)}")
    print(f"height的类型: {type(height)}")
    print(f"is_learning的类型: {type(is_learning)}")
    
    # 3. 类型转换
    print("\n3. 类型转换:")
    num_str = "100"
    num_int = int(num_str)
    print(f"字符串 '{num_str}' 转整数: {num_int}")
    
    # 4. 字符串操作
    print("\n4. 字符串操作:")
    text = "Hello, Python!"
    print(f"原始字符串: {text}")
    print(f"大写: {text.upper()}")
    print(f"小写: {text.lower()}")
    print(f"长度: {len(text)}")
    print(f"切片(0:5): {text[0:5]}")
    
    # 5. 条件语句
    print("\n5. 条件语句:")
    score = 85
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
    
    print(f"分数: {score}, 等级: {grade}")
    
    # 6. 循环语句
    print("\n6. 循环语句:")
    print("for循环打印1-5:")
    for i in range(1, 6):
        print(f"  i = {i}")
    
    print("\nwhile循环打印5-1:")
    count = 5
    while count > 0:
        print(f"  count = {count}")
        count -= 1
    
    print("\n=== 练习完成 ===")



    #猜数字游戏
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 7
    print("=== 猜数字游戏 ===")
    print(f"我想了一个1-100之间的数字，你有{max_attempts}次机会")
    while attempts < max_attempts:
        try:
            guess = int(input(f"第{attempts + 1}次尝试，请输入你的猜测: "))
        except ValueError:
            print("请输入有效的数字！")
            continue
        attempts += 1
        if guess > secret_number:
            print("数字太大了，请再猜。")
        elif guess < secret_number:
            print("数字太小了，请再猜。")
        else:
            print(f"恭喜！你猜对了，数字是{secret_number}。")
            break

    if attempts == max_attempts:
        print(f"游戏结束，你没有机会了。数字是{secret_number}。")


def student_grade_system():
    """学生成绩管理系统"""
    students = []
    while True:
        print("\n=== 学生成绩管理系统 ===")
        print("1. 添加学生成绩")
        print("2. 查看所有学生")
        print("3. 计算平均分")
        print("4. 查找最高分")
        print("5. 退出")

        choice = input("请选择操作 (1-5): ")

        if choice == "1":
            name = input("请输入学生姓名: ")
            try:
                score = float(input("请输入学生成绩 (0-100): "))
                if 0 <= score <= 100:
                    students.append({"name": name, "score": score})
                    print(f"✅ 成功添加 {name}: {score}分")
                else:
                    print("❌ 成绩必须在0-100之间")
            except ValueError:
                print("❌ 请输入有效的数字")
                
        elif choice == "2":
            if not students:
                print("暂无学生数据")
            else:
                print("\n学生列表:")
                for i, student in enumerate(students, 1):
                    print(f"{i}. {student['name']}: {student['score']}分")
                    
        elif choice == "3":
            if not students:
                print("暂无学生数据")
            else:
                total = sum(student["score"] for student in students)
                average = total / len(students)
                print(f"📊 平均分: {average:.2f}")
                
        elif choice == "4":
            if not students:
                print("暂无学生数据")
            else:
                best_student = max(students, key=lambda x: x["score"])
                print(f"🏆 最高分: {best_student['name']} - {best_student['score']}分")
                
        elif choice == "5":
            print("感谢使用，再见！")
            break
            
        else:
            print("❌ 无效的选择，请重新输入")


def simple_calculator():
    """简易计算器"""
    print("🧮 简易计算器")
    print("支持操作: +, -, *, /, %, ** (幂)")
    
    while True:
        try:
            num1 = float(input("请输入第一个数字: "))
            operator = input("请输入操作符 (+, -, *, /, %, **): ")
            num2 = float(input("请输入第二个数字: "))
            
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("❌ 错误：除数不能为0")
                    continue
                result = num1 / num2
            elif operator == "%":
                result = num1 % num2
            elif operator == "**":
                result = num1 ** num2
            else:
                print("❌ 不支持的操作符")
                continue
                
            print(f"✅ 结果: {num1} {operator} {num2} = {result}")
            
        except ValueError:
            print("❌ 请输入有效的数字")
        
        # 询问是否继续
        again = input("是否继续计算？ (y/n): ").lower()
        if again != "y":
            print("感谢使用计算器！")
            break

#数字统计
def getNum():
    num = 0
    for i in range(1,1000):
        if i%3==0:
            num+=1
        elif i%5 == 0:
            if i%3 == 0:
                break
            else:
                num+=1
    print(f"统计 1-1000 中能被 3 或 5 整除的数字个数{num}")  

    count = len([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])
    print(count)  # 输出: 467


#奇偶判断
def panDuanJiOu():
    while True:
        num1 = int(input("请输入数字："))
        if num1 % 2 == 0:
            print(f"{num1}是一个偶数")
        else:
            print(f"{num1}为一个奇数")

#字符串反转
def fanZhuanZiFuChuan():
    str = input(f"请输入一个字符串：")
    char = ""
    for i in str:
        char = i + char
    print(char)
    """
    🥇 方法一：切片（最推荐，Python 独有绝技）
    这是 Python 最强大的特性之一，一行代码搞定。
    s = "Agent开发"
    result = s[::-1]

    print(result) 
    # 输出: 发开tnegA
    恩哥原理解析：
    语法是 [start:stop:step]。
    当 step（步长）为 -1 时，Python 就知道：“嘿，从后往前，一个一个取！”
    优点：代码最少，执行速度最快，资深开发都这么写。
    🥈 方法二：使用 reversed() 函数（最规范）
    如果你觉得切片太 “魔术”，看不懂，用这个函数式写法，可读性最好。
    s = "Agent开发"
    result = "".join(reversed(s))

    print(result)
    # 输出: 发开tnegA
    恩哥原理解析：
    reversed(s)：返回一个反向的迭代器（倒序的字符流）。
    "".join(...)：用空字符串把这些字符重新拼起来。
    """


if __name__ == "__main__":
    # 运行系统
    # student_grade_system()
    # getNum()
    # panDuanJiOu()
    fanZhuanZiFuChuan()
    # 运行计算器5
    # simple_calculator()
    # 运行游戏
    # main()