from enum import Enum, auto, unique


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


class Status(Enum):
    PENDING = 1
    RUNNING = 2
    SUCCESS = 3
    FAILED = 4


def print_color_info(color: Color) -> None:
    print(f"Color name: {color.name}")
    print(f"Color value: {color.value}")


def print_status_message(status: Status) -> None:
    if status == Status.PENDING:
        print("状态：待处理")
    elif status == Status.RUNNING:
        print("状态：运行中")
    elif status == Status.SUCCESS:
        print("状态：成功")
    elif status == Status.FAILED:
        print("状态：失败")

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == "__main__":
    print("枚举 Color 示例:")
    print_color_info(Color.RED)
    print_color_info(Color.GREEN)

    print("\n枚举 Status 示例:")
    for status in Status:
        print(f"- {status.name} ({status.value})")
    print_status_message(Status.SUCCESS)

    # 枚举所有成员
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    print(Weekday.Fri)
    print(Weekday.Mon)
    print(Weekday.Sat)
    print(Weekday.Sun)
    print(Weekday.Thu)
    print(Weekday.Wed)
    print(Weekday.Tue)

    # 测试:
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')
