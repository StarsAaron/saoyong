"""
皇极经世书部分算法自动生卦
https://zhuanlan.zhihu.com/p/142932253
注意：这里的除法运算需要转int，否则计算出来的是浮点数
例如：
int((nian - 1) / 10)
"""

# 卦象
names = [
    "坤", "剥", "比", "观", "豫", "晋", "萃", "否",
    "谦", "艮", "蹇", "渐", "小过", "旅", "咸", "遁",
    "师", "蒙", "坎", "涣", "解", "未济", "困", "讼",
    "升", "蛊", "井", "巽", "恒", "鼎", "大过", "姤",
    "复", "颐", "屯", "益", "震", "噬嗑", "随", "无妄",
    "明夷", "贲", "既济", "家人", "丰", "离", "革", "同人",
    "临", "损", "节", "中孚", "归妹", "睽", "兑", "履",
    "泰", "大畜", "需", "小畜", "大壮", "大有", "夬", "乾"
]

# 图像
pics = [
    "乾", "坤", "屯", "蒙", "需", "讼", "师", "比", "小畜", "履", "泰", "否",
    "同人", "大有", "谦", "豫", "随", "蛊", "临", "观", "噬嗑", "贲",
    "剥", "复", "无妄", "大畜", "颐", "大过", "坎", "离",
    "咸", "恒", "遁", "大壮", "晋", "明夷", "家人", "睽",
    "蹇", "解", "损", "益", "夬", "姤", "萃", "升", "困", "井", "革", "鼎", "震",
    "艮", "渐", "归妹", "丰", "旅", "巽", "兑", "涣", "节", "中孚",
    "小过", "既济", "未济"
]


def change(gua: str, yao: int) -> str:
    """
    卦象偏移计算
    :param gua:
    :param yao:
    :return:
    """
    for i in range(0, 64):  # 0-64
        if names[i] == gua:
            ind = i ^ (64 >> yao)
            return names[ind]
    return ""


def order(i: int) -> str:
    """
    根据序号i计算卦象名
    :param i:
    :return:
    """
    if 0 <= i <= 12:
        return names[32 + i]
    elif 13 <= i <= 29:
        return names[33 + i]
    elif 30 <= i <= 42:
        return names[61 - i]
    elif 43 <= i <= 59:
        return names[60 - i]
    return ""


def add(ss: str, a: int) -> str:
    """
    计算卦象偏移
    :param ss:
    :param a:
    :return:
    """
    s = ss
    if "乾" == ss:
        s = "姤"
    if "坤" == ss:
        s = "复"
    if "坎" == ss:
        s = "蒙"
    if "离" == ss:
        s = "革"
    for i in range(0, 65):  # 0-64
        if order(i) == s:
            return order((i + a) % 60)
    return ""


def getPic(name: str) -> str:
    """
    获取卦象图
    :param name:
    :return:
    """
    for i in range(0, 65):  # 0-64
        if pics[i] == name:
            # ord 函数：Unicode 字符转 int
            # chr函数：int 转 Unicode 字符
            return chr(ord('\u4DC0') + i)
    return '\u0000'


def cal(year: int):
    if year == 0:
        print("没有0年")
        return

    if year > 0:
        y = year
    else:
        y = year + 1

    if y >= 1744:
        ayun = int((y - 1744) / 360) + 192
    else:
        ayun = int((y - 1743) / 360) + 191

    if ayun > 360 or ayun < 1:
        print("超出本元")
        return

    if year >= 0:
        print("公元" + str(year) + "年：")
    else:
        print("公元前" + str(-year) + "年：")

    hui = int((ayun - 1) / 30) + 1
    if ayun % 30 == 0:
        yun = 30
    else:
        yun = ayun % 30

    huigua = order(int((ayun - 1) / 6))  # 会卦

    if ayun % 6 == 0:
        yungua = change(huigua, 6)  # 运卦
    else:
        yungua = change(huigua, ayun % 6)

    ayear = y - (ayun - 192) * 360 - 1744  # 0
    shi = int(ayear / 30) + 1  # 世
    nian = ayear % 30 + 1  # 年
    shigua = change(yungua, int((shi - 1) / 2 + 1))  # 世卦

    if shi % 2 == 1:
        shiniangua = change(shigua, int((nian - 1) / 10 + 1))  # 十年卦
    else:
        shiniangua = change(shigua, int((nian - 1) / 10 + 4))

    niangua = add(shigua, ayear % 60)
    print("第" + str(hui) + "会，第" + str(yun) + "运，全元第" + str(ayun) + "运，"
          + "第" + str(shi) + "世，第" + str(nian) + "年，全运第" + str((ayear + 1)) + "年"
          + "，会卦:" + huigua + getPic(huigua)
          + "，运卦:" + yungua + getPic(yungua)
          + "，世卦:" + shigua + getPic(shigua)
          + "，十年卦:" + shiniangua + getPic(shiniangua)
          + "，年卦:" + niangua + getPic(niangua)
          + "，月卦依次为:")

    for i in range(1, 7):  # 1-6
        temp = change(niangua, i)
        print(temp + getPic(temp))


if __name__ == '__main__':
    # 计算变卦的例子
    print("姤卦变动得到的是")
    for i in range(1, 7):  # 1-6
        print(change("姤", i) + getPic(change("姤", i)) + "、")
    # 计算前后各一百年
    for i in range(1920, 2121):  # 1920 - 2120
        cal(i)
    # 计算某年各卦的例子
    print("输入公元年数，公元前用负号表示")
    cal(2023)
