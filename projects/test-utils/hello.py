"""
测试工具模块 - 小研的简单演示
创建时间: 2026-03-14
"""

def hello(name: str = "世界") -> str:
    """
    返回问候语
    
    Args:
        name: 要问候的名字，默认为"世界"
    
    Returns:
        问候语字符串
    """
    return f"你好，{name}！我是小研，你的研发助手。"


def add(a: int, b: int) -> int:
    """简单的加法函数，用于测试"""
    return a + b


if __name__ == "__main__":
    # 简单测试
    print(hello("潘文乐"))
    print(f"1 + 2 = {add(1, 2)}")
