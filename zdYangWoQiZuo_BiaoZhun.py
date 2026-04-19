######三年级      男生     仰卧起坐标准
def sannianji_nan_yangwoqizuo_jisuan_fenshu(sannianji_nan_yangwoqizuo):
    # if isinstance(sannianji_nan_yangwoqizuo, float):
    #     return "男生仰卧起坐请输入整数"
    # if not isinstance(sannianji_nan_yangwoqizuo, (int, float)):
    #     return ValueError("请传入有效的数字类型仰卧起坐数值（单位：个）")
    if 80 <= sannianji_nan_yangwoqizuo:
        return ("太大", "超出80个，请检查")
    elif 48 <= sannianji_nan_yangwoqizuo < 80:
        return (100, "优秀")
    elif 45 <= sannianji_nan_yangwoqizuo < 48:
        return (95, "优秀")
    elif 42 <= sannianji_nan_yangwoqizuo < 45:
        return (90, "优秀")
    elif 39 <= sannianji_nan_yangwoqizuo < 42:
        return (85, "良好")
    elif 36 <= sannianji_nan_yangwoqizuo < 39:
        return (80, "良好")
    elif 34 <= sannianji_nan_yangwoqizuo < 36:
        return (78, "及格")
    elif 32 <= sannianji_nan_yangwoqizuo < 34:
        return (76, "及格")
    elif 30 <= sannianji_nan_yangwoqizuo < 32:
        return (74, "及格")
    elif 28 <= sannianji_nan_yangwoqizuo < 30:
        return (72, "及格")
    elif 26 <= sannianji_nan_yangwoqizuo < 28:
        return (70, "及格")
    elif 24 <= sannianji_nan_yangwoqizuo < 26:
        return (68, "及格")
    elif 22 <= sannianji_nan_yangwoqizuo < 24:
        return (66, "及格")
    elif 20 <= sannianji_nan_yangwoqizuo < 22:
        return (64, "及格")
    elif 18 <= sannianji_nan_yangwoqizuo < 20:
        return (62, "及格")
    elif 16 <= sannianji_nan_yangwoqizuo < 18:
        return (60, "及格")
    elif 14 <= sannianji_nan_yangwoqizuo < 16:
        return (50, "不及格")
    elif 12 <= sannianji_nan_yangwoqizuo < 14:
        return (40, "不及格")
    elif 10 <= sannianji_nan_yangwoqizuo < 12:
        return (30, "不及格")
    elif 8 <= sannianji_nan_yangwoqizuo < 10:
        return (20, "不及格")
    elif 6 <= sannianji_nan_yangwoqizuo < 8:
        return (10, "不及格")
    elif 0 <= sannianji_nan_yangwoqizuo < 6:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型仰卧起坐数值（单位：个）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{sannianji_nan_yangwoqizuo_jisuan_fenshu(29.8)}")
    print(f"得分：{sannianji_nan_yangwoqizuo_jisuan_fenshu(46)[0]}")
    print(f"得分：{sannianji_nan_yangwoqizuo_jisuan_fenshu(46)[1]}")
    print(f"得分：{sannianji_nan_yangwoqizuo_jisuan_fenshu(16)}")




######三年级      女生     仰卧起坐标准
def sannianji_nv_yangwoqizuo_jisuan_fenshu(sannianji_nv_yangwoqizuo):
    # if isinstance(sannianji_nv_yangwoqizuo, float):
    #     return "女生仰卧起坐请输入整数"
    # if not isinstance(sannianji_nv_yangwoqizuo, (int, float)):
    #     return ValueError("请传入有效的数字类型仰卧起坐数值（单位：个）")
    if 80 <= sannianji_nv_yangwoqizuo:
        return ("太大", "超出80个，请检查")
    elif 46 <= sannianji_nv_yangwoqizuo < 80:
        return (100, "优秀")
    elif 44 <= sannianji_nv_yangwoqizuo < 46:
        return (95, "优秀")
    elif 42 <= sannianji_nv_yangwoqizuo < 44:
        return (90, "优秀")
    elif 39 <= sannianji_nv_yangwoqizuo < 42:
        return (85, "良好")
    elif 36 <= sannianji_nv_yangwoqizuo < 39:
        return (80, "良好")
    elif 34 <= sannianji_nv_yangwoqizuo < 36:
        return (78, "及格")
    elif 32 <= sannianji_nv_yangwoqizuo < 34:
        return (76, "及格")
    elif 30 <= sannianji_nv_yangwoqizuo < 32:
        return (74, "及格")
    elif 28 <= sannianji_nv_yangwoqizuo < 30:
        return (72, "及格")
    elif 26 <= sannianji_nv_yangwoqizuo < 28:
        return (70, "及格")
    elif 24 <= sannianji_nv_yangwoqizuo < 26:
        return (68, "及格")
    elif 22 <= sannianji_nv_yangwoqizuo < 24:
        return (66, "及格")
    elif 20 <= sannianji_nv_yangwoqizuo < 22:
        return (64, "及格")
    elif 18 <= sannianji_nv_yangwoqizuo < 20:
        return (62, "及格")
    elif 16 <= sannianji_nv_yangwoqizuo < 18:
        return (60, "及格")
    elif 14 <= sannianji_nv_yangwoqizuo < 16:
        return (50, "不及格")
    elif 12 <= sannianji_nv_yangwoqizuo < 14:
        return (40, "不及格")
    elif 10 <= sannianji_nv_yangwoqizuo < 12:
        return (30, "不及格")
    elif 8 <= sannianji_nv_yangwoqizuo < 10:
        return (20, "不及格")
    elif 6 <= sannianji_nv_yangwoqizuo < 8:
        return (10, "不及格")
    elif 0 <= sannianji_nv_yangwoqizuo < 6:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型仰卧起坐数值（单位：个）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{sannianji_nv_yangwoqizuo_jisuan_fenshu(29.8)}")
    print(f"得分：{sannianji_nv_yangwoqizuo_jisuan_fenshu(46)[0]}")
    print(f"得分：{sannianji_nv_yangwoqizuo_jisuan_fenshu(46)[1]}")
    print(f"得分：{sannianji_nv_yangwoqizuo_jisuan_fenshu(16)}")





######四年级      男生     仰卧起坐标准
def sinianji_nan_yangwoqizuo_jisuan_fenshu(sinianji_nan_yangwoqizuo):
    # if isinstance(sinianji_nan_yangwoqizuo, float):
    #     return "男生仰卧起坐请输入整数"
    # if not isinstance(sinianji_nan_yangwoqizuo, (int, float)):
    #     return ValueError("请传入有效的数字类型仰卧起坐数值（单位：个）")
    if 80 <= sinianji_nan_yangwoqizuo:
        return ("太大", "超出80个，请检查")
    elif 49 <= sinianji_nan_yangwoqizuo < 80:
        return (100, "优秀")
    elif 46 <= sinianji_nan_yangwoqizuo < 49:
        return (95, "优秀")
    elif 43 <= sinianji_nan_yangwoqizuo < 46:
        return (90, "优秀")
    elif 40 <= sinianji_nan_yangwoqizuo < 43:
        return (85, "良好")
    elif 37 <= sinianji_nan_yangwoqizuo < 40:
        return (80, "良好")
    elif 35 <= sinianji_nan_yangwoqizuo < 37:
        return (78, "及格")
    elif 33 <= sinianji_nan_yangwoqizuo < 35:
        return (76, "及格")
    elif 31 <= sinianji_nan_yangwoqizuo < 33:
        return (74, "及格")
    elif 29 <= sinianji_nan_yangwoqizuo < 31:
        return (72, "及格")
    elif 27 <= sinianji_nan_yangwoqizuo < 29:
        return (70, "及格")
    elif 25 <= sinianji_nan_yangwoqizuo < 27:
        return (68, "及格")
    elif 23 <= sinianji_nan_yangwoqizuo < 25:
        return (66, "及格")
    elif 21 <= sinianji_nan_yangwoqizuo < 23:
        return (64, "及格")
    elif 19 <= sinianji_nan_yangwoqizuo < 21:
        return (62, "及格")
    elif 17 <= sinianji_nan_yangwoqizuo < 19:
        return (60, "及格")
    elif 15 <= sinianji_nan_yangwoqizuo < 17:
        return (50, "不及格")
    elif 13 <= sinianji_nan_yangwoqizuo < 15:
        return (40, "不及格")
    elif 11 <= sinianji_nan_yangwoqizuo < 13:
        return (30, "不及格")
    elif 9 <= sinianji_nan_yangwoqizuo < 11:
        return (20, "不及格")
    elif 7 <= sinianji_nan_yangwoqizuo < 9:
        return (10, "不及格")
    elif 0 <= sinianji_nan_yangwoqizuo < 7:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型仰卧起坐数值（单位：个）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{sinianji_nan_yangwoqizuo_jisuan_fenshu(29.8)}")
    print(f"得分：{sinianji_nan_yangwoqizuo_jisuan_fenshu(46)[0]}")
    print(f"得分：{sinianji_nan_yangwoqizuo_jisuan_fenshu(46)[1]}")
    print(f"得分：{sinianji_nan_yangwoqizuo_jisuan_fenshu(16)}")



######四年级      女生     仰卧起坐标准
def sinianji_nv_yangwoqizuo_jisuan_fenshu(sinianji_nv_yangwoqizuo):
    # if isinstance(sinianji_nv_yangwoqizuo, float):
    #     return "女生仰卧起坐请输入整数"
    # if not isinstance(sinianji_nv_yangwoqizuo, (int, float)):
    #     return ValueError("请传入有效的数字类型仰卧起坐数值（单位：个）")
    if 80 <= sinianji_nv_yangwoqizuo:
        return ("太大", "超出80个，请检查")
    elif 47 <= sinianji_nv_yangwoqizuo < 80:
        return (100, "优秀")
    elif 45 <= sinianji_nv_yangwoqizuo < 47:
        return (95, "优秀")
    elif 43 <= sinianji_nv_yangwoqizuo < 45:
        return (90, "优秀")
    elif 40 <= sinianji_nv_yangwoqizuo < 43:
        return (85, "良好")
    elif 37 <= sinianji_nv_yangwoqizuo < 40:
        return (80, "良好")
    elif 35 <= sinianji_nv_yangwoqizuo < 37:
        return (78, "及格")
    elif 33 <= sinianji_nv_yangwoqizuo < 35:
        return (76, "及格")
    elif 31 <= sinianji_nv_yangwoqizuo < 33:
        return (74, "及格")
    elif 29 <= sinianji_nv_yangwoqizuo < 31:
        return (72, "及格")
    elif 27 <= sinianji_nv_yangwoqizuo < 29:
        return (70, "及格")
    elif 25 <= sinianji_nv_yangwoqizuo < 27:
        return (68, "及格")
    elif 23 <= sinianji_nv_yangwoqizuo < 25:
        return (66, "及格")
    elif 21 <= sinianji_nv_yangwoqizuo < 23:
        return (64, "及格")
    elif 19 <= sinianji_nv_yangwoqizuo < 21:
        return (62, "及格")
    elif 17 <= sinianji_nv_yangwoqizuo < 19:
        return (60, "及格")
    elif 15 <= sinianji_nv_yangwoqizuo < 17:
        return (50, "不及格")
    elif 13 <= sinianji_nv_yangwoqizuo < 15:
        return (40, "不及格")
    elif 11 <= sinianji_nv_yangwoqizuo < 13:
        return (30, "不及格")
    elif 9 <= sinianji_nv_yangwoqizuo < 11:
        return (20, "不及格")
    elif 7 <= sinianji_nv_yangwoqizuo < 9:
        return (10, "不及格")
    elif 0 <= sinianji_nv_yangwoqizuo < 7:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型仰卧起坐数值（单位：个）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{sinianji_nv_yangwoqizuo_jisuan_fenshu(29.8)}")
    print(f"得分：{sinianji_nv_yangwoqizuo_jisuan_fenshu(46)[0]}")
    print(f"得分：{sinianji_nv_yangwoqizuo_jisuan_fenshu(46)[1]}")
    print(f"得分：{sinianji_nv_yangwoqizuo_jisuan_fenshu(16)}")



######五年级      男生     仰卧起坐标准
def wunianji_nan_yangwoqizuo_jisuan_fenshu(wunianji_nan_yangwoqizuo):
    # if isinstance(wunianji_nan_yangwoqizuo, float):
    #     return "男生仰卧起坐请输入整数"
    # if not isinstance(wunianji_nan_yangwoqizuo, (int, float)):
    #     return ValueError("请传入有效的数字类型仰卧起坐数值（单位：个）")
    if 80 <= wunianji_nan_yangwoqizuo:
        return ("太大", "超出80个，请检查")
    elif 50 <= wunianji_nan_yangwoqizuo < 80:
        return (100, "优秀")
    elif 47 <= wunianji_nan_yangwoqizuo < 50:
        return (95, "优秀")
    elif 44 <= wunianji_nan_yangwoqizuo < 47:
        return (90, "优秀")
    elif 41 <= wunianji_nan_yangwoqizuo < 44:
        return (85, "良好")
    elif 38 <= wunianji_nan_yangwoqizuo < 41:
        return (80, "良好")
    elif 36 <= wunianji_nan_yangwoqizuo < 38:
        return (78, "及格")
    elif 34 <= wunianji_nan_yangwoqizuo < 36:
        return (76, "及格")
    elif 32 <= wunianji_nan_yangwoqizuo < 34:
        return (74, "及格")
    elif 30 <= wunianji_nan_yangwoqizuo < 32:
        return (72, "及格")
    elif 28 <= wunianji_nan_yangwoqizuo < 30:
        return (70, "及格")
    elif 26 <= wunianji_nan_yangwoqizuo < 28:
        return (68, "及格")
    elif 24 <= wunianji_nan_yangwoqizuo < 26:
        return (66, "及格")
    elif 22 <= wunianji_nan_yangwoqizuo < 24:
        return (64, "及格")
    elif 20 <= wunianji_nan_yangwoqizuo < 22:
        return (62, "及格")
    elif 18 <= wunianji_nan_yangwoqizuo < 20:
        return (60, "及格")
    elif 16 <= wunianji_nan_yangwoqizuo < 18:
        return (50, "不及格")
    elif 14 <= wunianji_nan_yangwoqizuo < 16:
        return (40, "不及格")
    elif 12 <= wunianji_nan_yangwoqizuo < 14:
        return (30, "不及格")
    elif 10 <= wunianji_nan_yangwoqizuo < 12:
        return (20, "不及格")
    elif 8 <= wunianji_nan_yangwoqizuo < 10:
        return (10, "不及格")
    elif 0 <= wunianji_nan_yangwoqizuo < 8:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型仰卧起坐数值（单位：个）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{wunianji_nan_yangwoqizuo_jisuan_fenshu(29.8)}")
    print(f"得分：{wunianji_nan_yangwoqizuo_jisuan_fenshu(46)[0]}")
    print(f"得分：{wunianji_nan_yangwoqizuo_jisuan_fenshu(46)[1]}")
    print(f"得分：{wunianji_nan_yangwoqizuo_jisuan_fenshu(16)}")





######五年级      女生     仰卧起坐标准
def wunianji_nv_yangwoqizuo_jisuan_fenshu(wunianji_nv_yangwoqizuo):
    # if isinstance(wunianji_nv_yangwoqizuo, float):
    #     return "女生仰卧起坐请输入整数"
    # if not isinstance(wunianji_nv_yangwoqizuo, (int, float)):
    #     return ValueError("请传入有效的数字类型仰卧起坐数值（单位：个）")
    if 80 <= wunianji_nv_yangwoqizuo:
        return ("太大", "超出80个，请检查")
    elif 48 <= wunianji_nv_yangwoqizuo < 80:
        return (100, "优秀")
    elif 46 <= wunianji_nv_yangwoqizuo < 48:
        return (95, "优秀")
    elif 44 <= wunianji_nv_yangwoqizuo < 46:
        return (90, "优秀")
    elif 41 <= wunianji_nv_yangwoqizuo < 44:
        return (85, "良好")
    elif 38 <= wunianji_nv_yangwoqizuo < 41:
        return (80, "良好")
    elif 36 <= wunianji_nv_yangwoqizuo < 38:
        return (78, "及格")
    elif 34 <= wunianji_nv_yangwoqizuo < 36:
        return (76, "及格")
    elif 32 <= wunianji_nv_yangwoqizuo < 34:
        return (74, "及格")
    elif 30 <= wunianji_nv_yangwoqizuo < 32:
        return (72, "及格")
    elif 28 <= wunianji_nv_yangwoqizuo < 30:
        return (70, "及格")
    elif 26 <= wunianji_nv_yangwoqizuo < 28:
        return (68, "及格")
    elif 24 <= wunianji_nv_yangwoqizuo < 26:
        return (66, "及格")
    elif 22 <= wunianji_nv_yangwoqizuo < 24:
        return (64, "及格")
    elif 20 <= wunianji_nv_yangwoqizuo < 22:
        return (62, "及格")
    elif 18 <= wunianji_nv_yangwoqizuo < 20:
        return (60, "及格")
    elif 16 <= wunianji_nv_yangwoqizuo < 18:
        return (50, "不及格")
    elif 14 <= wunianji_nv_yangwoqizuo < 16:
        return (40, "不及格")
    elif 12 <= wunianji_nv_yangwoqizuo < 14:
        return (30, "不及格")
    elif 10 <= wunianji_nv_yangwoqizuo < 12:
        return (20, "不及格")
    elif 8 <= wunianji_nv_yangwoqizuo < 10:
        return (10, "不及格")
    elif 0 <= wunianji_nv_yangwoqizuo < 8:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型仰卧起坐数值（单位：个）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{wunianji_nv_yangwoqizuo_jisuan_fenshu(29.8)}")
    print(f"得分：{wunianji_nv_yangwoqizuo_jisuan_fenshu(46)[0]}")
    print(f"得分：{wunianji_nv_yangwoqizuo_jisuan_fenshu(46)[1]}")
    print(f"得分：{wunianji_nv_yangwoqizuo_jisuan_fenshu(16)}")




######六年级      男生     仰卧起坐标准
def liunianji_nan_yangwoqizuo_jisuan_fenshu(liunianji_nan_yangwoqizuo):
    # if isinstance(liunianji_nan_yangwoqizuo, float):
    #     return "男生仰卧起坐请输入整数"
    # if not isinstance(liunianji_nan_yangwoqizuo, (int, float)):
    #     return ValueError("请传入有效的数字类型仰卧起坐数值（单位：个）")
    if 80 <= liunianji_nan_yangwoqizuo:
        return ("太大", "超出80个，请检查")
    elif 51 <= liunianji_nan_yangwoqizuo < 80:
        return (100, "优秀")
    elif 48 <= liunianji_nan_yangwoqizuo < 51:
        return (95, "优秀")
    elif 45 <= liunianji_nan_yangwoqizuo < 48:
        return (90, "优秀")
    elif 42 <= liunianji_nan_yangwoqizuo < 45:
        return (85, "良好")
    elif 39 <= liunianji_nan_yangwoqizuo < 42:
        return (80, "良好")
    elif 37 <= liunianji_nan_yangwoqizuo < 39:
        return (78, "及格")
    elif 35 <= liunianji_nan_yangwoqizuo < 37:
        return (76, "及格")
    elif 33 <= liunianji_nan_yangwoqizuo < 35:
        return (74, "及格")
    elif 31 <= liunianji_nan_yangwoqizuo < 33:
        return (72, "及格")
    elif 29 <= liunianji_nan_yangwoqizuo < 31:
        return (70, "及格")
    elif 27 <= liunianji_nan_yangwoqizuo < 29:
        return (68, "及格")
    elif 25 <= liunianji_nan_yangwoqizuo < 27:
        return (66, "及格")
    elif 23 <= liunianji_nan_yangwoqizuo < 25:
        return (64, "及格")
    elif 21 <= liunianji_nan_yangwoqizuo < 23:
        return (62, "及格")
    elif 19 <= liunianji_nan_yangwoqizuo < 21:
        return (60, "及格")
    elif 17 <= liunianji_nan_yangwoqizuo < 19:
        return (50, "不及格")
    elif 15 <= liunianji_nan_yangwoqizuo < 17:
        return (40, "不及格")
    elif 13 <= liunianji_nan_yangwoqizuo < 15:
        return (30, "不及格")
    elif 11 <= liunianji_nan_yangwoqizuo < 13:
        return (20, "不及格")
    elif 9 <= liunianji_nan_yangwoqizuo < 11:
        return (10, "不及格")
    elif 0 <= liunianji_nan_yangwoqizuo < 9:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型仰卧起坐数值（单位：个）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{liunianji_nan_yangwoqizuo_jisuan_fenshu(29.8)}")
    print(f"得分：{liunianji_nan_yangwoqizuo_jisuan_fenshu(46)[0]}")
    print(f"得分：{liunianji_nan_yangwoqizuo_jisuan_fenshu(46)[1]}")
    print(f"得分：{liunianji_nan_yangwoqizuo_jisuan_fenshu(16)}")



######六年级      女生     仰卧起坐标准
def liunianji_nv_yangwoqizuo_jisuan_fenshu(liunianji_nv_yangwoqizuo):
    # if isinstance(liunianji_nv_yangwoqizuo, float):
    #     return "女生仰卧起坐请输入整数"
    # if not isinstance(liunianji_nv_yangwoqizuo, (int, float)):
    #     return ValueError("请传入有效的数字类型仰卧起坐数值（单位：个）")
    if 80 <= liunianji_nv_yangwoqizuo:
        return ("太大", "超出80个，请检查")
    elif 49 <= liunianji_nv_yangwoqizuo < 80:
        return (100, "优秀")
    elif 47 <= liunianji_nv_yangwoqizuo < 49:
        return (95, "优秀")
    elif 45 <= liunianji_nv_yangwoqizuo < 47:
        return (90, "优秀")
    elif 42 <= liunianji_nv_yangwoqizuo < 45:
        return (85, "良好")
    elif 39 <= liunianji_nv_yangwoqizuo < 42:
        return (80, "良好")
    elif 37 <= liunianji_nv_yangwoqizuo < 39:
        return (78, "及格")
    elif 35 <= liunianji_nv_yangwoqizuo < 37:
        return (76, "及格")
    elif 33 <= liunianji_nv_yangwoqizuo < 35:
        return (74, "及格")
    elif 31 <= liunianji_nv_yangwoqizuo < 33:
        return (72, "及格")
    elif 29 <= liunianji_nv_yangwoqizuo < 31:
        return (70, "及格")
    elif 27 <= liunianji_nv_yangwoqizuo < 29:
        return (68, "及格")
    elif 25 <= liunianji_nv_yangwoqizuo < 27:
        return (66, "及格")
    elif 23 <= liunianji_nv_yangwoqizuo < 25:
        return (64, "及格")
    elif 21 <= liunianji_nv_yangwoqizuo < 23:
        return (62, "及格")
    elif 19 <= liunianji_nv_yangwoqizuo < 21:
        return (60, "及格")
    elif 17 <= liunianji_nv_yangwoqizuo < 19:
        return (50, "不及格")
    elif 15 <= liunianji_nv_yangwoqizuo < 17:
        return (40, "不及格")
    elif 13 <= liunianji_nv_yangwoqizuo < 15:
        return (30, "不及格")
    elif 11 <= liunianji_nv_yangwoqizuo < 13:
        return (20, "不及格")
    elif 9 <= liunianji_nv_yangwoqizuo < 11:
        return (10, "不及格")
    elif 0 <= liunianji_nv_yangwoqizuo < 9:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型仰卧起坐数值（单位：个）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{liunianji_nv_yangwoqizuo_jisuan_fenshu(29.8)}")
    print(f"得分：{liunianji_nv_yangwoqizuo_jisuan_fenshu(46)[0]}")
    print(f"得分：{liunianji_nv_yangwoqizuo_jisuan_fenshu(46)[1]}")
    print(f"得分：{liunianji_nv_yangwoqizuo_jisuan_fenshu(16)}")