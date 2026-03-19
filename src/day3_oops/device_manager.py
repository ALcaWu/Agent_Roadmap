class Smartphone:
    """智能手机类 - 类似Android中的Java类"""
    
    # 类变量（类似Java的static变量）
    brand = "Generic"
    
    def __init__(self, model, storage):
        """
        构造函数
        相当于Java的: public Smartphone(String model, int storage)
        """
        # 实例变量（类似Java的成员变量）
        self.model = model        # public属性
        self._storage = storage    # protected约定（单下划线）
        self.__serial = "12345"    # private约定（双下划线，实际是name mangling）
    
    def get_info(self):
        """实例方法"""
        return f"{self.brand} {self.model}, {self._storage}GB"
    
    def __str__(self):
        """魔术方法：相当于Java的toString()"""
        return f"Smartphone({self.model} {self.brand})"

    def __eq__(self, other):
        """魔术方法：判断对象相等"""
        if isinstance(other, Smartphone):
            return self.model == other.model
        return False

# 使用类
phone1 = Smartphone("Pixel 7", 128)
phone2 = Smartphone("Pixel 7", 256)

# print(phone1)           # 调用 __str__: Smartphone(Pixel 7)
# print(phone1.get_info()) # Generic Pixel 7, 128GB
# print(phone1 == phone2)  # 调用 __eq__: True (因为model相同)


#继承和多态
from abc import ABC, abstractmethod

# 抽象基类（类似Java的Interface或Abstract Class）
class Device(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def connect(self):
        """抽象方法：子类必须实现"""
        pass
    
    def power_on(self):
        """普通方法：子类可直接使用或重写"""
        print(f"{self.name} 正在开机...")

# 具体类：智能手表
class SmartWatch(Device):
    def __init__(self, name, battery_life):
        super().__init__(name)  # 调用父类构造函数
        self.battery_life = battery_life
    
    def connect(self):
        """实现抽象方法"""
        print(f"{self.name} 通过蓝牙连接手机")
    
    def power_on(self):
        """重写父类方法"""
        print(f"{self.name} 手表启动，电量: {self.battery_life}%")

# 具体类：智能音箱
class SmartSpeaker(Device):
    def connect(self):
        print(f"{self.name} 通过Wi-Fi连接网络")

# 多态演示
def setup_device(device: Device):
    """多态函数：接受任何Device子类"""
    device.power_on()
    device.connect()

# 测试多态
watch = SmartWatch("Galaxy Watch", 85)
speaker = SmartSpeaker("Echo Dot")

setup_device(watch)    # 运行时决定调用哪个方法
setup_device(speaker)


class Agent:
    def __init__(self, name, level):
        self._name = name      # 内部变量
        self._level = level
    
    # Getter（类似Java的getName()）
    @property
    def name(self):
        return self._name.upper()
    
    # Setter（类似Java的setName()）
    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("名字太短")
        self._name = value

    
    # 只读属性
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
         self._level = value

# 使用
agent = Agent("GPT-4", 100)
agent.name = "Claude"  # 自动调用setter
agent.level = 95
print(agent.name)  # 自动调用getter: GPT-4
print(agent.level)

# agent.name = "AI"  # 会抛出ValueError


from abc import ABC,abstractmethod
from enum import Enum
class OS(Enum):
    """操作系统枚举"""
    ANDROID = "Android"
    IOS = "iOS"

class Device(ABC):
    #设备抽象类
    def __init__(self, model, os_version):
        self.model = model
        self.os_version = os_version
        self._is_power_on = False

    @abstractmethod
    def boot(self):
        #启动设备
        pass

    def power_on(self):
        """开机"""
        if not self._is_power_on:
            print(f"设备正在启动。。。")
            self.boot()
            self._is_power_on = True    
            print(f"✅ {self.model}设备已启动")

        else:
            print(f"⚠️ {self.model} 已经是开机状态")

    
