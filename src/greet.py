"""练习用的最小脚本：打印一句问候。

存在意义是给「改一行代码、提交、看 diff」提供一个具体的靶子。
"""

import sys


def greet(name: str = "世界") -> str:
    """返回一句问候语。"""
    return f"你好，{name}！"


def main(argv: list[str]) -> int:
    name = argv[1] if len(argv) > 1 else "世界"
    print(greet(name))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
