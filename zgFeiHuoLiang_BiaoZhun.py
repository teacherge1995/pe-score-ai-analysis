### 一年级 男生 肺活量标准
def yinianji_nan_feihuoliang_jisuan_fenshu(yinianji_nan_feihuoliang):
    # if isinstance(yinianji_nan_feihuoliang, float):
    #     return "男生肺活量请输入整数"
    # if not isinstance(yinianji_nan_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if yinianji_nan_feihuoliang > 5000:
        return ("太大", "超出5000ml，请检查")
    elif 1700 <= yinianji_nan_feihuoliang <= 5000:
        return (100, "优秀")
    elif 1600 <= yinianji_nan_feihuoliang < 1700:
        return (95, "优秀")
    elif 1500 <= yinianji_nan_feihuoliang < 1600:
        return (90, "优秀")
    elif 1400 <= yinianji_nan_feihuoliang < 1500:
        return (85, "良好")
    elif 1300 <= yinianji_nan_feihuoliang < 1400:
        return (80, "良好")
    elif 1240 <= yinianji_nan_feihuoliang < 1300:
        return (78, "及格")
    elif 1180 <= yinianji_nan_feihuoliang < 1240:
        return (76, "及格")
    elif 1120 <= yinianji_nan_feihuoliang < 1180:
        return (74, "及格")
    elif 1060 <= yinianji_nan_feihuoliang < 1120:
        return (72, "及格")
    elif 1000 <= yinianji_nan_feihuoliang < 1060:
        return (70, "及格")
    elif 940 <= yinianji_nan_feihuoliang < 1000:
        return (68, "及格")
    elif 880 <= yinianji_nan_feihuoliang < 940:
        return (66, "及格")
    elif 820 <= yinianji_nan_feihuoliang < 880:
        return (64, "及格")
    elif 760 <= yinianji_nan_feihuoliang < 820:
        return (62, "及格")
    elif 700 <= yinianji_nan_feihuoliang < 760:
        return (60, "及格")
    elif 660 <= yinianji_nan_feihuoliang < 700:
        return (50, "不及格")
    elif 620 <= yinianji_nan_feihuoliang < 660:
        return (40, "不及格")
    elif 580 <= yinianji_nan_feihuoliang < 620:
        return (30, "不及格")
    elif 540 <= yinianji_nan_feihuoliang < 580:
        return (20, "不及格")
    elif 500 <= yinianji_nan_feihuoliang < 540:
        return (10, "不及格")
    elif 0 <= yinianji_nan_feihuoliang < 500:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"

# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升男得分：{yinianji_nan_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升男得分：{yinianji_nan_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1600毫升男得分：{yinianji_nan_feihuoliang_jisuan_fenshu(1600)}")  # 输出90




### 一年级 女生 肺活量标准
def yinianji_nv_feihuoliang_jisuan_fenshu(yinianji_nv_feihuoliang):
    # if isinstance(yinianji_nv_feihuoliang, float):
    #     return "女生肺活量请输入整数"
    # if not isinstance(yinianji_nv_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if yinianji_nv_feihuoliang > 5000:
        return ("太大", "超出5000ml，请检查")
    elif 1400 <= yinianji_nv_feihuoliang <= 5000:
        return (100, "优秀")
    elif 1300 <= yinianji_nv_feihuoliang < 1400:
        return (95, "优秀")
    elif 1200 <= yinianji_nv_feihuoliang < 1300:
        return (90, "优秀")
    elif 1100 <= yinianji_nv_feihuoliang < 1200:
        return (85, "良好")
    elif 1000 <= yinianji_nv_feihuoliang < 1100:
        return (80, "良好")
    elif 960 <= yinianji_nv_feihuoliang < 1000:
        return (78, "及格")
    elif 920 <= yinianji_nv_feihuoliang < 960:
        return (76, "及格")
    elif 880 <= yinianji_nv_feihuoliang < 920:
        return (74, "及格")
    elif 840 <= yinianji_nv_feihuoliang < 880:
        return (72, "及格")
    elif 800 <= yinianji_nv_feihuoliang < 840:
        return (70, "及格")
    elif 760 <= yinianji_nv_feihuoliang < 800:
        return (68, "及格")
    elif 720 <= yinianji_nv_feihuoliang < 760:
        return (66, "及格")
    elif 680 <= yinianji_nv_feihuoliang < 720:
        return (64, "及格")
    elif 640 <= yinianji_nv_feihuoliang < 680:
        return (62, "及格")
    elif 600 <= yinianji_nv_feihuoliang < 640:
        return (60, "及格")
    elif 580 <= yinianji_nv_feihuoliang < 600:
        return (50, "不及格")
    elif 560 <= yinianji_nv_feihuoliang < 580:
        return (40, "不及格")
    elif 540 <= yinianji_nv_feihuoliang < 560:
        return (30, "不及格")
    elif 520 <= yinianji_nv_feihuoliang < 540:
        return (20, "不及格")
    elif 500 <= yinianji_nv_feihuoliang < 520:
        return (10, "不及格")
    elif 0 <= yinianji_nv_feihuoliang < 500:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"

# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    # 修正此处调用的函数名，应该是 yinianji_nv_feihuoliang_jisuan_fenshu
    print(f"2900毫升女得分：{yinianji_nv_feihuoliang_jisuan_fenshu(2900)[0]}")
    print(f"2900毫升女得分：{yinianji_nv_feihuoliang_jisuan_fenshu(2900)[1]}")
    # 修正此处调用的函数名，应该是 yinianji_nv_feihuoliang_jisuan_fenshu
    print(f"1600毫升女得分：{yinianji_nv_feihuoliang_jisuan_fenshu(600)}")





### 二年级 男生 肺活量标准
def ernianji_nan_feihuoliang_jisuan_fenshu(ernianji_nan_feihuoliang):
    # if isinstance(ernianji_nan_feihuoliang, float):
    #     return "男生肺活量请输入整数"
    # if not isinstance(ernianji_nan_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if ernianji_nan_feihuoliang > 6000:
        return ("太大", "超出6000ml，请检查")
    elif 2000 <= ernianji_nan_feihuoliang <= 6000:
        return (100, "优秀")
    elif 1900 <= ernianji_nan_feihuoliang < 2000:
        return (95, "优秀")
    elif 1800 <= ernianji_nan_feihuoliang < 1900:
        return (90, "优秀")
    elif 1650 <= ernianji_nan_feihuoliang < 1800:
        return (85, "良好")
    elif 1500 <= ernianji_nan_feihuoliang < 1650:
        return (80, "良好")
    elif 1430 <= ernianji_nan_feihuoliang < 1500:
        return (78, "及格")
    elif 1360 <= ernianji_nan_feihuoliang < 1430:
        return (76, "及格")
    elif 1290 <= ernianji_nan_feihuoliang < 1360:
        return (74, "及格")
    elif 1220 <= ernianji_nan_feihuoliang < 1290:
        return (72, "及格")
    elif 1150 <= ernianji_nan_feihuoliang < 1220:
        return (70, "及格")
    elif 1080 <= ernianji_nan_feihuoliang < 1150:
        return (68, "及格")
    elif 1010 <= ernianji_nan_feihuoliang < 1080:
        return (66, "及格")
    elif 940 <= ernianji_nan_feihuoliang < 1010:
        return (64, "及格")
    elif 870 <= ernianji_nan_feihuoliang < 940:
        return (62, "及格")
    elif 800 <= ernianji_nan_feihuoliang < 870:
        return (60, "及格")
    elif 750 <= ernianji_nan_feihuoliang < 800:
        return (50, "不及格")
    elif 700 <= ernianji_nan_feihuoliang < 750:
        return (40, "不及格")
    elif 650 <= ernianji_nan_feihuoliang < 700:
        return (30, "不及格")
    elif 600 <= ernianji_nan_feihuoliang < 650:
        return (20, "不及格")
    elif 550 <= ernianji_nan_feihuoliang < 600:
        return (10, "不及格")
    elif 0 <= ernianji_nan_feihuoliang < 550:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升男得分：{ernianji_nan_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升男得分：{ernianji_nan_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1600毫升男得分：{ernianji_nan_feihuoliang_jisuan_fenshu(1600)}")  # 输出90




### 二年级 女生 肺活量标准
def ernianji_nv_feihuoliang_jisuan_fenshu(ernianji_nv_feihuoliang):
    # if isinstance(ernianji_nv_feihuoliang, float):
    #     return "女生肺活量请输入整数"
    # if not isinstance(ernianji_nv_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if ernianji_nv_feihuoliang > 6000:
        return ("太大", "超出6000ml，请检查")
    elif 1600 <= ernianji_nv_feihuoliang <= 6000:
        return (100, "优秀")
    elif 1500 <= ernianji_nv_feihuoliang < 1600:
        return (95, "优秀")
    elif 1400 <= ernianji_nv_feihuoliang < 1500:
        return (90, "优秀")
    elif 1300 <= ernianji_nv_feihuoliang < 1400:
        return (85, "良好")
    elif 1200 <= ernianji_nv_feihuoliang < 1300:
        return (80, "良好")
    elif 1150 <= ernianji_nv_feihuoliang < 1200:
        return (78, "及格")
    elif 1100 <= ernianji_nv_feihuoliang < 1150:
        return (76, "及格")
    elif 1050 <= ernianji_nv_feihuoliang < 1100:
        return (74, "及格")
    elif 1000 <= ernianji_nv_feihuoliang < 1050:
        return (72, "及格")
    elif 950 <= ernianji_nv_feihuoliang < 1000:
        return (70, "及格")
    elif 900 <= ernianji_nv_feihuoliang < 950:
        return (68, "及格")
    elif 850 <= ernianji_nv_feihuoliang < 900:
        return (66, "及格")
    elif 800 <= ernianji_nv_feihuoliang < 850:
        return (64, "及格")
    elif 750 <= ernianji_nv_feihuoliang < 800:
        return (62, "及格")
    elif 700 <= ernianji_nv_feihuoliang < 750:
        return (60, "及格")
    elif 680 <= ernianji_nv_feihuoliang < 700:
        return (50, "不及格")
    elif 660 <= ernianji_nv_feihuoliang < 680:
        return (40, "不及格")
    elif 640 <= ernianji_nv_feihuoliang < 660:
        return (30, "不及格")
    elif 620 <= ernianji_nv_feihuoliang < 640:
        return (20, "不及格")
    elif 600 <= ernianji_nv_feihuoliang < 620:
        return (10, "不及格")
    elif 0 <= ernianji_nv_feihuoliang < 600:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升女得分：{ernianji_nv_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升女得分：{ernianji_nv_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1600毫升女得分：{ernianji_nv_feihuoliang_jisuan_fenshu(600)}")  # 输出90





### 三年级 男生 肺活量标准
def sannianji_nan_feihuoliang_jisuan_fenshu(sannianji_nan_feihuoliang):
    # if isinstance(sannianji_nan_feihuoliang, float):
    #     return "男生肺活量请输入整数"
    # if not isinstance(sannianji_nan_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if sannianji_nan_feihuoliang > 6000:
        return ("太大", "超出6000ml，请检查")
    elif 2300 <= sannianji_nan_feihuoliang <= 6000:
        return (100, "优秀")
    elif 2200 <= sannianji_nan_feihuoliang < 2300:
        return (95, "优秀")
    elif 2100 <= sannianji_nan_feihuoliang < 2200:
        return (90, "优秀")
    elif 1900 <= sannianji_nan_feihuoliang < 2100:
        return (85, "良好")
    elif 1700 <= sannianji_nan_feihuoliang < 1900:
        return (80, "良好")
    elif 1620 <= sannianji_nan_feihuoliang < 1700:
        return (78, "及格")
    elif 1540 <= sannianji_nan_feihuoliang < 1620:
        return (76, "及格")
    elif 1460 <= sannianji_nan_feihuoliang < 1540:
        return (74, "及格")
    elif 1380 <= sannianji_nan_feihuoliang < 1460:
        return (72, "及格")
    elif 1300 <= sannianji_nan_feihuoliang < 1380:
        return (70, "及格")
    elif 1220 <= sannianji_nan_feihuoliang < 1300:
        return (68, "及格")
    elif 1140 <= sannianji_nan_feihuoliang < 1220:
        return (66, "及格")
    elif 1060 <= sannianji_nan_feihuoliang < 1140:
        return (64, "及格")
    elif 980 <= sannianji_nan_feihuoliang < 1060:
        return (62, "及格")
    elif 900 <= sannianji_nan_feihuoliang < 980:
        return (60, "及格")
    elif 840 <= sannianji_nan_feihuoliang < 900:
        return (50, "不及格")
    elif 780 <= sannianji_nan_feihuoliang < 840:
        return (40, "不及格")
    elif 720 <= sannianji_nan_feihuoliang < 780:
        return (30, "不及格")
    elif 660 <= sannianji_nan_feihuoliang < 720:
        return (20, "不及格")
    elif 600 <= sannianji_nan_feihuoliang < 660:
        return (10, "不及格")
    elif 0 <= sannianji_nan_feihuoliang < 600:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升男得分：{sannianji_nan_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升男得分：{sannianji_nan_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1600毫升男得分：{sannianji_nan_feihuoliang_jisuan_fenshu(1600)}")  # 输出90




### 三年级 女生 肺活量标准
def sannianji_nv_feihuoliang_jisuan_fenshu(sannianji_nv_feihuoliang):
    # if isinstance(sannianji_nv_feihuoliang, float):
    #     return "女生肺活量请输入整数"
    # if not isinstance(sannianji_nv_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if sannianji_nv_feihuoliang > 6000:
        return ("太大", "超出6000ml，请检查")
    elif 1800 <= sannianji_nv_feihuoliang <= 6000:
        return (100, "优秀")
    elif 1700 <= sannianji_nv_feihuoliang < 1800:
        return (95, "优秀")
    elif 1600 <= sannianji_nv_feihuoliang < 1700:
        return (90, "优秀")
    elif 1500 <= sannianji_nv_feihuoliang < 1600:
        return (85, "良好")
    elif 1400 <= sannianji_nv_feihuoliang < 1500:
        return (80, "良好")
    elif 1340 <= sannianji_nv_feihuoliang < 1400:
        return (78, "及格")
    elif 1280 <= sannianji_nv_feihuoliang < 1340:
        return (76, "及格")
    elif 1220 <= sannianji_nv_feihuoliang < 1280:
        return (74, "及格")
    elif 1160 <= sannianji_nv_feihuoliang < 1220:
        return (72, "及格")
    elif 1100 <= sannianji_nv_feihuoliang < 1160:
        return (70, "及格")
    elif 1040 <= sannianji_nv_feihuoliang < 1100:
        return (68, "及格")
    elif 980 <= sannianji_nv_feihuoliang < 1040:
        return (66, "及格")
    elif 920 <= sannianji_nv_feihuoliang < 980:
        return (64, "及格")
    elif 860 <= sannianji_nv_feihuoliang < 920:
        return (62, "及格")
    elif 800 <= sannianji_nv_feihuoliang < 860:
        return (60, "及格")
    elif 780 <= sannianji_nv_feihuoliang < 800:
        return (50, "不及格")
    elif 760 <= sannianji_nv_feihuoliang < 780:
        return (40, "不及格")
    elif 740 <= sannianji_nv_feihuoliang < 760:
        return (30, "不及格")
    elif 720 <= sannianji_nv_feihuoliang < 740:
        return (20, "不及格")
    elif 700 <= sannianji_nv_feihuoliang < 720:
        return (10, "不及格")
    elif 0 <= sannianji_nv_feihuoliang < 700:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升女得分：{sannianji_nv_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升女得分：{sannianji_nv_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1600毫升女得分：{sannianji_nv_feihuoliang_jisuan_fenshu(600)}")  # 输出90





### 四年级男生肺活量标准
def sinianji_nan_feihuoliang_jisuan_fenshu(sinianji_nan_feihuoliang):
    # if isinstance(sinianji_nan_feihuoliang, float):
    #     return "男生肺活量请输入整数"
    # if not isinstance(sinianji_nan_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if sinianji_nan_feihuoliang > 6000:
        return ("太大", "超出6000ml，请检查")
    elif 2600 <= sinianji_nan_feihuoliang <= 6000:
        return (100, "优秀")
    elif 2500 <= sinianji_nan_feihuoliang < 2600:
        return (95, "优秀")
    elif 2400 <= sinianji_nan_feihuoliang < 2500:
        return (90, "优秀")
    elif 2150 <= sinianji_nan_feihuoliang < 2400:
        return (85, "良好")
    elif 1900 <= sinianji_nan_feihuoliang < 2150:
        return (80, "良好")
    elif 1820 <= sinianji_nan_feihuoliang < 1900:
        return (78, "及格")
    elif 1740 <= sinianji_nan_feihuoliang < 1820:
        return (76, "及格")
    elif 1660 <= sinianji_nan_feihuoliang < 1740:
        return (74, "及格")
    elif 1580 <= sinianji_nan_feihuoliang < 1660:
        return (72, "及格")
    elif 1500 <= sinianji_nan_feihuoliang < 1580:
        return (70, "及格")
    elif 1420 <= sinianji_nan_feihuoliang < 1500:
        return (68, "及格")
    elif 1340 <= sinianji_nan_feihuoliang < 1420:
        return (66, "及格")
    elif 1260 <= sinianji_nan_feihuoliang < 1340:
        return (64, "及格")
    elif 1180 <= sinianji_nan_feihuoliang < 1260:
        return (62, "及格")
    elif 1100 <= sinianji_nan_feihuoliang < 1180:
        return (60, "及格")
    elif 1030 <= sinianji_nan_feihuoliang < 1100:
        return (50, "不及格")
    elif 960 <= sinianji_nan_feihuoliang < 1030:
        return (40, "不及格")
    elif 890 <= sinianji_nan_feihuoliang < 960:
        return (30, "不及格")
    elif 820 <= sinianji_nan_feihuoliang < 890:
        return (20, "不及格")
    elif 750 <= sinianji_nan_feihuoliang < 820:
        return (10, "不及格")
    elif 0 <= sinianji_nan_feihuoliang < 750:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升男得分：{sinianji_nan_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升男得分：{sinianji_nan_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1600毫升男得分：{sinianji_nan_feihuoliang_jisuan_fenshu(1600)}")  # 输出90





### 四年级女生肺活量标准
def sinianji_nv_feihuoliang_jisuan_fenshu(sinianji_nv_feihuoliang):
    # if isinstance(sinianji_nv_feihuoliang, float):
    #     return "女生肺活量请输入整数"
    # if not isinstance(sinianji_nv_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if sinianji_nv_feihuoliang > 6000:
        return ("太大", "超出6000ml，请检查")
    elif 2000 <= sinianji_nv_feihuoliang <= 6000:
        return (100, "优秀")
    elif 1900 <= sinianji_nv_feihuoliang < 2000:
        return (95, "优秀")
    elif 1800 <= sinianji_nv_feihuoliang < 1900:
        return (90, "优秀")
    elif 1700 <= sinianji_nv_feihuoliang < 1800:
        return (85, "良好")
    elif 1600 <= sinianji_nv_feihuoliang < 1700:
        return (80, "良好")
    elif 1530 <= sinianji_nv_feihuoliang < 1600:
        return (78, "及格")
    elif 1460 <= sinianji_nv_feihuoliang < 1530:
        return (76, "及格")
    elif 1390 <= sinianji_nv_feihuoliang < 1460:
        return (74, "及格")
    elif 1320 <= sinianji_nv_feihuoliang < 1390:
        return (72, "及格")
    elif 1250 <= sinianji_nv_feihuoliang < 1320:
        return (70, "及格")
    elif 1180 <= sinianji_nv_feihuoliang < 1250:
        return (68, "及格")
    elif 1110 <= sinianji_nv_feihuoliang < 1180:
        return (66, "及格")
    elif 1040 <= sinianji_nv_feihuoliang < 1110:
        return (64, "及格")
    elif 970 <= sinianji_nv_feihuoliang < 1040:
        return (62, "及格")
    elif 900 <= sinianji_nv_feihuoliang < 970:
        return (60, "及格")
    elif 880 <= sinianji_nv_feihuoliang < 900:
        return (50, "不及格")
    elif 860 <= sinianji_nv_feihuoliang < 880:
        return (40, "不及格")
    elif 840 <= sinianji_nv_feihuoliang < 860:
        return (30, "不及格")
    elif 820 <= sinianji_nv_feihuoliang < 840:
        return (20, "不及格")
    elif 800 <= sinianji_nv_feihuoliang < 820:
        return (10, "不及格")
    elif 0 <= sinianji_nv_feihuoliang < 800:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升女得分：{sinianji_nv_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升女得分：{sinianji_nv_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1600毫升女得分：{sinianji_nv_feihuoliang_jisuan_fenshu(600)}")  # 输出90



### 五年级男生肺活量标准
def wunianji_nan_feihuoliang_jisuan_fenshu(wunianji_nan_feihuoliang):
    # if isinstance(wunianji_nan_feihuoliang, float):
    #     return "男生肺活量请输入整数"
    # if not isinstance(wunianji_nan_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if wunianji_nan_feihuoliang > 7000:
        return ("太大", "超出7000ml，请检查")
    elif 2900 <= wunianji_nan_feihuoliang <= 7000:
        return (100, "优秀")
    elif 2800 <= wunianji_nan_feihuoliang < 2900:
        return (95, "优秀")
    elif 2700 <= wunianji_nan_feihuoliang < 2800:
        return (90, "优秀")
    elif 2450 <= wunianji_nan_feihuoliang < 2700:
        return (85, "良好")
    elif 2200 <= wunianji_nan_feihuoliang < 2450:
        return (80, "良好")
    elif 2110 <= wunianji_nan_feihuoliang < 2200:
        return (78, "及格")
    elif 2020 <= wunianji_nan_feihuoliang < 2110:
        return (76, "及格")
    elif 1930 <= wunianji_nan_feihuoliang < 2020:
        return (74, "及格")
    elif 1840 <= wunianji_nan_feihuoliang < 1930:
        return (72, "及格")
    elif 1750 <= wunianji_nan_feihuoliang < 1840:
        return (70, "及格")
    elif 1660 <= wunianji_nan_feihuoliang < 1750:
        return (68, "及格")
    elif 1570 <= wunianji_nan_feihuoliang < 1660:
        return (66, "及格")
    elif 1480 <= wunianji_nan_feihuoliang < 1570:
        return (64, "及格")
    elif 1390 <= wunianji_nan_feihuoliang < 1480:
        return (62, "及格")
    elif 1300 <= wunianji_nan_feihuoliang < 1390:
        return (60, "及格")
    elif 1220 <= wunianji_nan_feihuoliang < 1300:
        return (50, "不及格")
    elif 1140 <= wunianji_nan_feihuoliang < 1220:
        return (40, "不及格")
    elif 1060 <= wunianji_nan_feihuoliang < 1140:
        return (30, "不及格")
    elif 980 <= wunianji_nan_feihuoliang < 1060:
        return (20, "不及格")
    elif 900 <= wunianji_nan_feihuoliang < 980:
        return (10, "不及格")
    elif 0 <= wunianji_nan_feihuoliang < 900:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升男得分：{wunianji_nan_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升男得分：{wunianji_nan_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1600毫升男得分：{wunianji_nan_feihuoliang_jisuan_fenshu(1600)}")  # 输出90


### 五年级女生肺活量标准
def wunianji_nv_feihuoliang_jisuan_fenshu(wunianji_nv_feihuoliang):
    # if isinstance(wunianji_nv_feihuoliang, float):
    #     return "女生肺活量请输入整数"
    # if not isinstance(wunianji_nv_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if wunianji_nv_feihuoliang > 7000:
        return ("太大", "超出7000ml，请检查")
    elif 2250 <= wunianji_nv_feihuoliang <= 7000:
        return (100, "优秀")
    elif 2150 <= wunianji_nv_feihuoliang < 2250:
        return (95, "优秀")
    elif 2050 <= wunianji_nv_feihuoliang < 2150:
        return (90, "优秀")
    elif 1950 <= wunianji_nv_feihuoliang < 2050:
        return (85, "良好")
    elif 1850 <= wunianji_nv_feihuoliang < 1950:
        return (80, "良好")
    elif 1770 <= wunianji_nv_feihuoliang < 1850:
        return (78, "及格")
    elif 1690 <= wunianji_nv_feihuoliang < 1770:
        return (76, "及格")
    elif 1610 <= wunianji_nv_feihuoliang < 1690:
        return (74, "及格")
    elif 1530 <= wunianji_nv_feihuoliang < 1610:
        return (72, "及格")
    elif 1450 <= wunianji_nv_feihuoliang < 1530:
        return (70, "及格")
    elif 1370 <= wunianji_nv_feihuoliang < 1450:
        return (68, "及格")
    elif 1290 <= wunianji_nv_feihuoliang < 1370:
        return (66, "及格")
    elif 1210 <= wunianji_nv_feihuoliang < 1290:
        return (64, "及格")
    elif 1130 <= wunianji_nv_feihuoliang < 1210:
        return (62, "及格")
    elif 1050 <= wunianji_nv_feihuoliang < 1130:
        return (60, "及格")
    elif 1020 <= wunianji_nv_feihuoliang < 1050:
        return (50, "不及格")
    elif 990 <= wunianji_nv_feihuoliang < 1020:
        return (40, "不及格")
    elif 960 <= wunianji_nv_feihuoliang < 990:
        return (30, "不及格")
    elif 930 <= wunianji_nv_feihuoliang < 960:
        return (20, "不及格")
    elif 900 <= wunianji_nv_feihuoliang < 930:
        return (10, "不及格")
    elif 0 <= wunianji_nv_feihuoliang < 900:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升女得分：{wunianji_nv_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升女得分：{wunianji_nv_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1600毫升女得分：{wunianji_nv_feihuoliang_jisuan_fenshu(600)}")  # 输出90



### 六年级男生肺活量标准
def liunianji_nan_feihuoliang_jisuan_fenshu(liunianji_nan_feihuoliang):
    # if isinstance(liunianji_nan_feihuoliang, float):
    #     return "男生肺活量请输入整数"
    # if not isinstance(liunianji_nan_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if liunianji_nan_feihuoliang > 7000:
        return ("太大", "超出7000ml，请检查")
    elif 3200 <= liunianji_nan_feihuoliang <= 7000:
        return (100, "优秀")
    elif 3100 <= liunianji_nan_feihuoliang < 3200:
        return (95, "优秀")
    elif 3000 <= liunianji_nan_feihuoliang < 3100:
        return (90, "优秀")
    elif 2750 <= liunianji_nan_feihuoliang < 3000:
        return (85, "良好")
    elif 2500 <= liunianji_nan_feihuoliang < 2750:
        return (80, "良好")
    elif 2400 <= liunianji_nan_feihuoliang < 2500:
        return (78, "及格")
    elif 2300 <= liunianji_nan_feihuoliang < 2400:
        return (76, "及格")
    elif 2200 <= liunianji_nan_feihuoliang < 2300:
        return (74, "及格")
    elif 2100 <= liunianji_nan_feihuoliang < 2200:
        return (72, "及格")
    elif 2000 <= liunianji_nan_feihuoliang < 2100:
        return (70, "及格")
    elif 1900 <= liunianji_nan_feihuoliang < 2000:
        return (68, "及格")
    elif 1800 <= liunianji_nan_feihuoliang < 1900:
        return (66, "及格")
    elif 1700 <= liunianji_nan_feihuoliang < 1800:
        return (64, "及格")
    elif 1600 <= liunianji_nan_feihuoliang < 1700:
        return (62, "及格")
    elif 1500 <= liunianji_nan_feihuoliang < 1600:
        return (60, "及格")
    elif 1410 <= liunianji_nan_feihuoliang < 1500:
        return (50, "不及格")
    elif 1320 <= liunianji_nan_feihuoliang < 1410:
        return (40, "不及格")
    elif 1230 <= liunianji_nan_feihuoliang < 1320:
        return (30, "不及格")
    elif 1140 <= liunianji_nan_feihuoliang < 1230:
        return (20, "不及格")
    elif 1050 <= liunianji_nan_feihuoliang < 1140:
        return (10, "不及格")
    elif 0 <= liunianji_nan_feihuoliang < 1050:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升男得分：{liunianji_nan_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升男得分：{liunianji_nan_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1600毫升男得分：{liunianji_nan_feihuoliang_jisuan_fenshu(1600)}")  # 输出90



### 六年级女生肺活量标准
def liunianji_nv_feihuoliang_jisuan_fenshu(liunianji_nv_feihuoliang):
    # if isinstance(liunianji_nv_feihuoliang, float):
    #     return "女生肺活量请输入整数"
    # if not isinstance(liunianji_nv_feihuoliang, (int, float)):
    #     return ValueError("请传入有效的数字类型肺活量数值（单位：毫升）")

    if liunianji_nv_feihuoliang > 7000:
        return ("太大", "超出7000ml，请检查")
    elif 2500 <= liunianji_nv_feihuoliang <= 7000:
        return (100, "优秀")
    elif 2400 <= liunianji_nv_feihuoliang < 2500:
        return (95, "优秀")
    elif 2300 <= liunianji_nv_feihuoliang < 2400:
        return (90, "优秀")
    elif 2200 <= liunianji_nv_feihuoliang < 2300:
        return (85, "良好")
    elif 2100 <= liunianji_nv_feihuoliang < 2200:
        return (80, "良好")
    elif 2010 <= liunianji_nv_feihuoliang < 2100:
        return (78, "及格")
    elif 1920 <= liunianji_nv_feihuoliang < 2010:
        return (76, "及格")
    elif 1830 <= liunianji_nv_feihuoliang < 1920:
        return (74, "及格")
    elif 1740 <= liunianji_nv_feihuoliang < 1830:
        return (72, "及格")
    elif 1650 <= liunianji_nv_feihuoliang < 1740:
        return (70, "及格")
    elif 1560 <= liunianji_nv_feihuoliang < 1650:
        return (68, "及格")
    elif 1470 <= liunianji_nv_feihuoliang < 1560:
        return (66, "及格")
    elif 1380 <= liunianji_nv_feihuoliang < 1470:
        return (64, "及格")
    elif 1290 <= liunianji_nv_feihuoliang < 1380:
        return (62, "及格")
    elif 1200 <= liunianji_nv_feihuoliang < 1290:
        return (60, "及格")
    elif 1170 <= liunianji_nv_feihuoliang < 1200:
        return (50, "不及格")
    elif 1140 <= liunianji_nv_feihuoliang < 1170:
        return (40, "不及格")
    elif 1110 <= liunianji_nv_feihuoliang < 1140:
        return (30, "不及格")
    elif 1080 <= liunianji_nv_feihuoliang < 1110:
        return (20, "不及格")
    elif 1050 <= liunianji_nv_feihuoliang < 1080:
        return (10, "不及格")
    elif 0 <= liunianji_nv_feihuoliang < 1050:
        return (0, "不及格")
    else:
        return "低于0ml，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"2900毫升女得分：{liunianji_nv_feihuoliang_jisuan_fenshu(2900)[0]}")  # 输出100
    print(f"2900毫升女得分：{liunianji_nv_feihuoliang_jisuan_fenshu(2900)[1]}")  # 输出100
    print(f"1800毫升女得分：{liunianji_nv_feihuoliang_jisuan_fenshu(1800)}")  # 输出90