###一年级     50米     男
def yinianji_nan_wushimi_jisuan_fenshu(yinianji_nan_wushimi):
    # if not isinstance(yinianji_nan_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if yinianji_nan_wushimi < 7:
        return ("太大", "低于7秒，请检查")
    elif 7 <= yinianji_nan_wushimi < 10.3:
        return (100, "优秀")
    elif 10.3 <= yinianji_nan_wushimi < 10.4:
        return (95, "优秀")
    elif 10.4 <= yinianji_nan_wushimi < 10.5:
        return (90, "优秀")
    elif 10.5 <= yinianji_nan_wushimi < 10.6:
        return (85, "良好")
    elif 10.6 <= yinianji_nan_wushimi < 10.8:
        return (80, "良好")
    elif 10.8 <= yinianji_nan_wushimi < 11:
        return (78, "及格")
    elif 11 <= yinianji_nan_wushimi < 11.2:
        return (76, "及格")
    elif 11.2 <= yinianji_nan_wushimi < 11.4:
        return (74, "及格")
    elif 11.4 <= yinianji_nan_wushimi < 11.6:
        return (72, "及格")
    elif 11.6 <= yinianji_nan_wushimi < 11.8:
        return (70, "及格")
    elif 11.8 <= yinianji_nan_wushimi < 12:
        return (68, "及格")
    elif 12 <= yinianji_nan_wushimi < 12.2:
        return (66, "及格")
    elif 12.2 <= yinianji_nan_wushimi < 12.4:
        return (64, "及格")
    elif 12.4 <= yinianji_nan_wushimi < 12.6:
        return (62, "及格")
    elif 12.6 <= yinianji_nan_wushimi < 12.8:
        return (60, "及格")
    elif 12.8 <= yinianji_nan_wushimi < 13:
        return (50, "不及格")
    elif 13 <= yinianji_nan_wushimi < 13.2:
        return (40, "不及格")
    elif 13.2 <= yinianji_nan_wushimi < 13.4:
        return (30, "不及格")
    elif 13.4 <= yinianji_nan_wushimi < 13.6:
        return (20, "不及格")
    elif 13.6 <= yinianji_nan_wushimi < 20:
        return (10, "不及格")
    elif 20 <= yinianji_nan_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", yinianji_nan_wushimi_jisuan_fenshu(11)[0], yinianji_nan_wushimi_jisuan_fenshu(11)[1])


###一年级     50米     女
def yinianji_nv_wushimi_jisuan_fenshu(yinianji_nv_wushimi):
    # if not isinstance(yinianji_nv_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if yinianji_nv_wushimi < 7:
        return ("太大", "低于7秒，请检查")
    elif 7 <= yinianji_nv_wushimi < 11.1:
        return (100, "优秀")
    elif 11.1 <= yinianji_nv_wushimi < 11.2:
        return (95, "优秀")
    elif 11.2 <= yinianji_nv_wushimi < 11.5:
        return (90, "优秀")
    elif 11.5 <= yinianji_nv_wushimi < 11.8:
        return (85, "良好")
    elif 11.8 <= yinianji_nv_wushimi < 12:
        return (80, "良好")
    elif 12 <= yinianji_nv_wushimi < 12.2:
        return (78, "及格")
    elif 12.2 <= yinianji_nv_wushimi < 12.4:
        return (76, "及格")
    elif 12.4 <= yinianji_nv_wushimi < 12.6:
        return (74, "及格")
    elif 12.6 <= yinianji_nv_wushimi < 12.8:
        return (72, "及格")
    elif 12.8 <= yinianji_nv_wushimi < 13:
        return (70, "及格")
    elif 13 <= yinianji_nv_wushimi < 13.2:
        return (68, "及格")
    elif 13.2 <= yinianji_nv_wushimi < 13.4:
        return (66, "及格")
    elif 13.4 <= yinianji_nv_wushimi < 13.6:
        return (64, "及格")
    elif 13.6 <= yinianji_nv_wushimi < 13.8:
        return (62, "及格")
    elif 13.8 <= yinianji_nv_wushimi < 14:
        return (60, "及格")
    elif 14 <= yinianji_nv_wushimi < 14.2:
        return (50, "不及格")
    elif 14.2 <= yinianji_nv_wushimi < 14.4:
        return (40, "不及格")
    elif 14.4 <= yinianji_nv_wushimi < 14.6:
        return (30, "不及格")
    elif 14.6 <= yinianji_nv_wushimi < 14.8:
        return (20, "不及格")
    elif 14.8 <= yinianji_nv_wushimi < 20:
        return (10, "不及格")
    elif 20 <= yinianji_nv_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", yinianji_nv_wushimi_jisuan_fenshu(11)[0], yinianji_nv_wushimi_jisuan_fenshu(11)[1])





###二年级     50米     男
def ernianji_nan_wushimi_jisuan_fenshu(ernianji_nan_wushimi):
    # if not isinstance(ernianji_nan_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if ernianji_nan_wushimi < 7:
        return ("太大", "低于7秒，请检查")
    elif 7 <= ernianji_nan_wushimi < 9.7:
        return (100, "优秀")
    elif 9.7 <= ernianji_nan_wushimi < 9.8:
        return (95, "优秀")
    elif 9.8 <= ernianji_nan_wushimi < 9.9:
        return (90, "优秀")
    elif 9.9 <= ernianji_nan_wushimi < 10:
        return (85, "良好")
    elif 10 <= ernianji_nan_wushimi < 10.2:
        return (80, "良好")
    elif 10.2 <= ernianji_nan_wushimi < 10.4:
        return (78, "及格")
    elif 10.4 <= ernianji_nan_wushimi < 10.6:
        return (76, "及格")
    elif 10.6 <= ernianji_nan_wushimi < 10.8:
        return (74, "及格")
    elif 10.8 <= ernianji_nan_wushimi < 11:
        return (72, "及格")
    elif 11 <= ernianji_nan_wushimi < 11.2:
        return (70, "及格")
    elif 11.2 <= ernianji_nan_wushimi < 11.4:
        return (68, "及格")
    elif 11.4 <= ernianji_nan_wushimi < 11.6:
        return (66, "及格")
    elif 11.6 <= ernianji_nan_wushimi < 11.8:
        return (64, "及格")
    elif 11.8 <= ernianji_nan_wushimi < 12:
        return (62, "及格")
    elif 12 <= ernianji_nan_wushimi < 12.2:
        return (60, "及格")
    elif 12.2 <= ernianji_nan_wushimi < 12.4:
        return (50, "不及格")
    elif 12.4 <= ernianji_nan_wushimi < 12.6:
        return (40, "不及格")
    elif 12.6 <= ernianji_nan_wushimi < 12.8:
        return (30, "不及格")
    elif 12.8 <= ernianji_nan_wushimi < 13:
        return (20, "不及格")
    elif 13 <= ernianji_nan_wushimi < 20:
        return (10, "不及格")
    elif 20 <= ernianji_nan_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", ernianji_nan_wushimi_jisuan_fenshu(11)[0], ernianji_nan_wushimi_jisuan_fenshu(11)[1])




###二年级     50米     女
def ernianji_nv_wushimi_jisuan_fenshu(ernianji_nv_wushimi):
    # if not isinstance(ernianji_nv_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if ernianji_nv_wushimi < 7:
        return ("太大", "低于7秒，请检查")
    elif 7 <= ernianji_nv_wushimi < 10.1:
        return (100, "优秀")
    elif 10.1 <= ernianji_nv_wushimi < 10.2:
        return (95, "优秀")
    elif 10.2 <= ernianji_nv_wushimi < 10.5:
        return (90, "优秀")
    elif 10.5 <= ernianji_nv_wushimi < 10.8:
        return (85, "良好")
    elif 10.8 <= ernianji_nv_wushimi < 11:
        return (80, "良好")
    elif 11 <= ernianji_nv_wushimi < 11.2:
        return (78, "及格")
    elif 11.2 <= ernianji_nv_wushimi < 11.4:
        return (76, "及格")
    elif 11.4 <= ernianji_nv_wushimi < 11.6:
        return (74, "及格")
    elif 11.6 <= ernianji_nv_wushimi < 11.8:
        return (72, "及格")
    elif 11.8 <= ernianji_nv_wushimi < 12:
        return (70, "及格")
    elif 12 <= ernianji_nv_wushimi < 12.2:
        return (68, "及格")
    elif 12.2 <= ernianji_nv_wushimi < 12.4:
        return (66, "及格")
    elif 12.4 <= ernianji_nv_wushimi < 12.6:
        return (64, "及格")
    elif 12.6 <= ernianji_nv_wushimi < 12.8:
        return (62, "及格")
    elif 12.8 <= ernianji_nv_wushimi < 13:
        return (60, "及格")
    elif 13 <= ernianji_nv_wushimi < 13.2:
        return (50, "不及格")
    elif 13.2 <= ernianji_nv_wushimi < 13.4:
        return (40, "不及格")
    elif 13.4 <= ernianji_nv_wushimi < 13.6:
        return (30, "不及格")
    elif 13.6 <= ernianji_nv_wushimi < 13.8:
        return (20, "不及格")
    elif 13.8 <= ernianji_nv_wushimi < 20:
        return (10, "不及格")
    elif 20 <= ernianji_nv_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", ernianji_nv_wushimi_jisuan_fenshu(11)[0], ernianji_nv_wushimi_jisuan_fenshu(11)[1])





###三年级     50米     男
def sannianji_nan_wushimi_jisuan_fenshu(sannianji_nan_wushimi):
    # if not isinstance(sannianji_nan_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if sannianji_nan_wushimi < 7:
        return ("太大", "低于7秒，请检查")
    elif 7 <= sannianji_nan_wushimi < 9.2:
        return (100, "优秀")
    elif 9.2 <= sannianji_nan_wushimi < 9.3:
        return (95, "优秀")
    elif 9.3 <= sannianji_nan_wushimi < 9.4:
        return (90, "优秀")
    elif 9.4 <= sannianji_nan_wushimi < 9.5:
        return (85, "良好")
    elif 9.5 <= sannianji_nan_wushimi < 9.7:
        return (80, "良好")
    elif 9.7 <= sannianji_nan_wushimi < 9.9:
        return (78, "及格")
    elif 9.9 <= sannianji_nan_wushimi < 10.1:
        return (76, "及格")
    elif 10.1 <= sannianji_nan_wushimi < 10.3:
        return (74, "及格")
    elif 10.3 <= sannianji_nan_wushimi < 10.5:
        return (72, "及格")
    elif 10.5 <= sannianji_nan_wushimi < 10.7:
        return (70, "及格")
    elif 10.7 <= sannianji_nan_wushimi < 10.9:
        return (68, "及格")
    elif 10.9 <= sannianji_nan_wushimi < 11.1:
        return (66, "及格")
    elif 11.1 <= sannianji_nan_wushimi < 11.3:
        return (64, "及格")
    elif 11.3 <= sannianji_nan_wushimi < 11.5:
        return (62, "及格")
    elif 11.5 <= sannianji_nan_wushimi < 11.7:
        return (60, "及格")
    elif 11.7 <= sannianji_nan_wushimi < 11.9:
        return (50, "不及格")
    elif 11.9 <= sannianji_nan_wushimi < 12.1:
        return (40, "不及格")
    elif 12.1 <= sannianji_nan_wushimi < 12.3:
        return (30, "不及格")
    elif 12.3 <= sannianji_nan_wushimi < 12.5:
        return (20, "不及格")
    elif 12.5 <= sannianji_nan_wushimi < 20:
        return (10, "不及格")
    elif 20 <= sannianji_nan_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", sannianji_nan_wushimi_jisuan_fenshu(11)[0], sannianji_nan_wushimi_jisuan_fenshu(11)[1])



###三年级     50米     女
def sannianji_nv_wushimi_jisuan_fenshu(sannianji_nv_wushimi):
    # if not isinstance(sannianji_nv_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if sannianji_nv_wushimi < 7:
        return ("太大", "低于7秒，请检查")
    elif 7 <= sannianji_nv_wushimi < 9.3:
        return (100, "优秀")
    elif 9.3 <= sannianji_nv_wushimi < 9.4:
        return (95, "优秀")
    elif 9.4 <= sannianji_nv_wushimi < 9.7:
        return (90, "优秀")
    elif 9.7 <= sannianji_nv_wushimi < 10:
        return (85, "良好")
    elif 10 <= sannianji_nv_wushimi < 10.2:
        return (80, "良好")
    elif 10.2 <= sannianji_nv_wushimi < 10.4:
        return (78, "及格")
    elif 10.4 <= sannianji_nv_wushimi < 10.6:
        return (76, "及格")
    elif 10.6 <= sannianji_nv_wushimi < 10.8:
        return (74, "及格")
    elif 10.8 <= sannianji_nv_wushimi < 11:
        return (72, "及格")
    elif 11 <= sannianji_nv_wushimi < 11.2:
        return (70, "及格")
    elif 11.2 <= sannianji_nv_wushimi < 11.4:
        return (68, "及格")
    elif 11.4 <= sannianji_nv_wushimi < 11.6:
        return (66, "及格")
    elif 11.6 <= sannianji_nv_wushimi < 11.8:
        return (64, "及格")
    elif 11.8 <= sannianji_nv_wushimi < 12:
        return (62, "及格")
    elif 12 <= sannianji_nv_wushimi < 12.2:
        return (60, "及格")
    elif 12.2 <= sannianji_nv_wushimi < 12.4:
        return (50, "不及格")
    elif 12.4 <= sannianji_nv_wushimi < 12.6:
        return (40, "不及格")
    elif 12.6 <= sannianji_nv_wushimi < 12.8:
        return (30, "不及格")
    elif 12.8 <= sannianji_nv_wushimi < 13:
        return (20, "不及格")
    elif 13 <= sannianji_nv_wushimi < 20:
        return (10, "不及格")
    elif 20 <= sannianji_nv_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", sannianji_nv_wushimi_jisuan_fenshu(11)[0], sannianji_nv_wushimi_jisuan_fenshu(11)[1])





###四年级     50米     男
def sinianji_nan_wushimi_jisuan_fenshu(sinianji_nan_wushimi):
    # if not isinstance(sinianji_nan_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if sinianji_nan_wushimi < 6:
        return ("太大", "低于6秒，请检查")
    elif 6 <= sinianji_nan_wushimi < 8.8:
        return (100, "优秀")
    elif 8.8 <= sinianji_nan_wushimi < 8.9:
        return (95, "优秀")
    elif 8.9 <= sinianji_nan_wushimi < 9:
        return (90, "优秀")
    elif 9 <= sinianji_nan_wushimi < 9.1:
        return (85, "良好")
    elif 9.1 <= sinianji_nan_wushimi < 9.3:
        return (80, "良好")
    elif 9.3 <= sinianji_nan_wushimi < 9.5:
        return (78, "及格")
    elif 9.5 <= sinianji_nan_wushimi < 9.7:
        return (76, "及格")
    elif 9.7 <= sinianji_nan_wushimi < 9.9:
        return (74, "及格")
    elif 9.9 <= sinianji_nan_wushimi < 10.1:
        return (72, "及格")
    elif 10.1 <= sinianji_nan_wushimi < 10.3:
        return (70, "及格")
    elif 10.3 <= sinianji_nan_wushimi < 10.5:
        return (68, "及格")
    elif 10.5 <= sinianji_nan_wushimi < 10.7:
        return (66, "及格")
    elif 10.7 <= sinianji_nan_wushimi < 10.9:
        return (64, "及格")
    elif 10.9 <= sinianji_nan_wushimi < 11.1:
        return (62, "及格")
    elif 11.1 <= sinianji_nan_wushimi < 11.3:
        return (60, "及格")
    elif 11.3 <= sinianji_nan_wushimi < 11.5:
        return (50, "不及格")
    elif 11.5 <= sinianji_nan_wushimi < 11.7:
        return (40, "不及格")
    elif 11.7 <= sinianji_nan_wushimi < 11.9:
        return (30, "不及格")
    elif 11.9 <= sinianji_nan_wushimi < 12.1:
        return (20, "不及格")
    elif 12.1 <= sinianji_nan_wushimi < 20:
        return (10, "不及格")
    elif 20 <= sinianji_nan_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", sinianji_nan_wushimi_jisuan_fenshu(11)[0], sinianji_nan_wushimi_jisuan_fenshu(11)[1])



###四年级     50米     女
def sinianji_nv_wushimi_jisuan_fenshu(sinianji_nv_wushimi):
    # if not isinstance(sinianji_nv_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if sinianji_nv_wushimi < 6:
        return ("太大", "低于6秒，请检查")
    elif 6 <= sinianji_nv_wushimi < 8.8:
        return (100, "优秀")
    elif 8.8 <= sinianji_nv_wushimi < 8.9:
        return (95, "优秀")
    elif 8.9 <= sinianji_nv_wushimi < 9.2:
        return (90, "优秀")
    elif 9.2 <= sinianji_nv_wushimi < 9.5:
        return (85, "良好")
    elif 9.5 <= sinianji_nv_wushimi < 9.7:
        return (80, "良好")
    elif 9.7 <= sinianji_nv_wushimi < 9.9:
        return (78, "及格")
    elif 9.9 <= sinianji_nv_wushimi < 10.1:
        return (76, "及格")
    elif 10.1 <= sinianji_nv_wushimi < 10.3:
        return (74, "及格")
    elif 10.3 <= sinianji_nv_wushimi < 10.5:
        return (72, "及格")
    elif 10.5 <= sinianji_nv_wushimi < 10.7:
        return (70, "及格")
    elif 10.7 <= sinianji_nv_wushimi < 10.9:
        return (68, "及格")
    elif 10.9 <= sinianji_nv_wushimi < 11.1:
        return (66, "及格")
    elif 11.1 <= sinianji_nv_wushimi < 11.3:
        return (64, "及格")
    elif 11.3 <= sinianji_nv_wushimi < 11.5:
        return (62, "及格")
    elif 11.5 <= sinianji_nv_wushimi < 11.7:
        return (60, "及格")
    elif 11.7 <= sinianji_nv_wushimi < 11.9:
        return (50, "不及格")
    elif 11.9 <= sinianji_nv_wushimi < 12.1:
        return (40, "不及格")
    elif 12.1 <= sinianji_nv_wushimi < 12.3:
        return (30, "不及格")
    elif 12.3 <= sinianji_nv_wushimi < 12.5:
        return (20, "不及格")
    elif 12.5 <= sinianji_nv_wushimi < 20:
        return (10, "不及格")
    elif 20 <= sinianji_nv_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", sinianji_nv_wushimi_jisuan_fenshu(11)[0], sinianji_nv_wushimi_jisuan_fenshu(11)[1])






###五年级     50米     男
def wunianji_nan_wushimi_jisuan_fenshu(wunianji_nan_wushimi):
    # if not isinstance(wunianji_nan_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if wunianji_nan_wushimi < 6:
        return ("太大", "低于6秒，请检查")
    elif 6 <= wunianji_nan_wushimi < 8.5:
        return (100, "优秀")
    elif 8.5 <= wunianji_nan_wushimi < 8.6:
        return (95, "优秀")
    elif 8.6 <= wunianji_nan_wushimi < 8.7:
        return (90, "优秀")
    elif 8.7 <= wunianji_nan_wushimi < 8.8:
        return (85, "良好")
    elif 8.8 <= wunianji_nan_wushimi < 9:
        return (80, "良好")
    elif 9 <= wunianji_nan_wushimi < 9.2:
        return (78, "及格")
    elif 9.2 <= wunianji_nan_wushimi < 9.4:
        return (76, "及格")
    elif 9.4 <= wunianji_nan_wushimi < 9.6:
        return (74, "及格")
    elif 9.6 <= wunianji_nan_wushimi < 9.8:
        return (72, "及格")
    elif 9.8 <= wunianji_nan_wushimi < 10:
        return (70, "及格")
    elif 10 <= wunianji_nan_wushimi < 10.2:
        return (68, "及格")
    elif 10.2 <= wunianji_nan_wushimi < 10.4:
        return (66, "及格")
    elif 10.4 <= wunianji_nan_wushimi < 10.6:
        return (64, "及格")
    elif 10.6 <= wunianji_nan_wushimi < 10.8:
        return (62, "及格")
    elif 10.8 <= wunianji_nan_wushimi < 11:
        return (60, "及格")
    elif 11 <= wunianji_nan_wushimi < 11.2:
        return (50, "不及格")
    elif 11.2 <= wunianji_nan_wushimi < 11.4:
        return (40, "不及格")
    elif 11.4 <= wunianji_nan_wushimi < 11.6:
        return (30, "不及格")
    elif 11.6 <= wunianji_nan_wushimi < 11.8:
        return (20, "不及格")
    elif 11.8 <= wunianji_nan_wushimi < 20:
        return (10, "不及格")
    elif 20 <= wunianji_nan_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", wunianji_nan_wushimi_jisuan_fenshu(11)[0], wunianji_nan_wushimi_jisuan_fenshu(11)[1])





###五年级     50米     女
def wunianji_nv_wushimi_jisuan_fenshu(wunianji_nv_wushimi):
    # if not isinstance(wunianji_nv_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if wunianji_nv_wushimi < 6:
        return ("太大", "低于6秒，请检查")
    elif 6 <= wunianji_nv_wushimi < 8.4:
        return (100, "优秀")
    elif 8.4 <= wunianji_nv_wushimi < 8.5:
        return (95, "优秀")
    elif 8.5 <= wunianji_nv_wushimi < 8.8:
        return (90, "优秀")
    elif 8.8 <= wunianji_nv_wushimi < 9.1:
        return (85, "良好")
    elif 9.1 <= wunianji_nv_wushimi < 9.3:
        return (80, "良好")
    elif 9.3 <= wunianji_nv_wushimi < 9.5:
        return (78, "及格")
    elif 9.5 <= wunianji_nv_wushimi < 9.7:
        return (76, "及格")
    elif 9.7 <= wunianji_nv_wushimi < 9.9:
        return (74, "及格")
    elif 9.9 <= wunianji_nv_wushimi < 10.1:
        return (72, "及格")
    elif 10.1 <= wunianji_nv_wushimi < 10.3:
        return (70, "及格")
    elif 10.3 <= wunianji_nv_wushimi < 10.5:
        return (68, "及格")
    elif 10.5 <= wunianji_nv_wushimi < 10.7:
        return (66, "及格")
    elif 10.7 <= wunianji_nv_wushimi < 10.9:
        return (64, "及格")
    elif 10.9 <= wunianji_nv_wushimi < 11.1:
        return (62, "及格")
    elif 11.1 <= wunianji_nv_wushimi < 11.3:
        return (60, "及格")
    elif 11.3 <= wunianji_nv_wushimi < 11.5:
        return (50, "不及格")
    elif 11.5 <= wunianji_nv_wushimi < 11.7:
        return (40, "不及格")
    elif 11.7 <= wunianji_nv_wushimi < 11.9:
        return (30, "不及格")
    elif 11.9 <= wunianji_nv_wushimi < 12.1:
        return (20, "不及格")
    elif 12.1 <= wunianji_nv_wushimi < 20:
        return (10, "不及格")
    elif 20 <= wunianji_nv_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", wunianji_nv_wushimi_jisuan_fenshu(11)[0], wunianji_nv_wushimi_jisuan_fenshu(11)[1])



###六年级     50米     男
def liunianji_nan_wushimi_jisuan_fenshu(liunianji_nan_wushimi):
    # if not isinstance(liunianji_nan_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if liunianji_nan_wushimi < 6:
        return ("太大", "低于6秒，请检查")
    elif 6 <= liunianji_nan_wushimi < 8.3:
        return (100, "优秀")
    elif 8.3 <= liunianji_nan_wushimi < 8.4:
        return (95, "优秀")
    elif 8.4 <= liunianji_nan_wushimi < 8.5:
        return (90, "优秀")
    elif 8.5 <= liunianji_nan_wushimi < 8.6:
        return (85, "良好")
    elif 8.6 <= liunianji_nan_wushimi < 8.8:
        return (80, "良好")
    elif 8.8 <= liunianji_nan_wushimi < 9:
        return (78, "及格")
    elif 9 <= liunianji_nan_wushimi < 9.2:
        return (76, "及格")
    elif 9.2 <= liunianji_nan_wushimi < 9.4:
        return (74, "及格")
    elif 9.4 <= liunianji_nan_wushimi < 9.6:
        return (72, "及格")
    elif 9.6 <= liunianji_nan_wushimi < 9.8:
        return (70, "及格")
    elif 9.8 <= liunianji_nan_wushimi < 10:
        return (68, "及格")
    elif 10 <= liunianji_nan_wushimi < 10.2:
        return (66, "及格")
    elif 10.2 <= liunianji_nan_wushimi < 10.4:
        return (64, "及格")
    elif 10.4 <= liunianji_nan_wushimi < 10.6:
        return (62, "及格")
    elif 10.6 <= liunianji_nan_wushimi < 10.8:
        return (60, "及格")
    elif 10.8 <= liunianji_nan_wushimi < 11:
        return (50, "不及格")
    elif 11 <= liunianji_nan_wushimi < 11.2:
        return (40, "不及格")
    elif 11.2 <= liunianji_nan_wushimi < 11.4:
        return (30, "不及格")
    elif 11.4 <= liunianji_nan_wushimi < 11.6:
        return (20, "不及格")
    elif 11.6 <= liunianji_nan_wushimi < 20:
        return (10, "不及格")
    elif 20 <= liunianji_nan_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", liunianji_nan_wushimi_jisuan_fenshu(11)[0], liunianji_nan_wushimi_jisuan_fenshu(11)[1])



###六年级     50米     女
def liunianji_nv_wushimi_jisuan_fenshu(liunianji_nv_wushimi):
    # if not isinstance(liunianji_nv_wushimi, (int, float)):
    #     return ValueError("请传入有效的数字类型50米数值（单位：秒）")
    if liunianji_nv_wushimi < 6:
        return ("太大", "低于6秒，请检查")
    elif 6 <= liunianji_nv_wushimi < 8.3:
        return (100, "优秀")
    elif 8.3 <= liunianji_nv_wushimi < 8.4:
        return (95, "优秀")
    elif 8.4 <= liunianji_nv_wushimi < 8.7:
        return (90, "优秀")
    elif 8.7 <= liunianji_nv_wushimi < 9:
        return (85, "良好")
    elif 9 <= liunianji_nv_wushimi < 9.2:
        return (80, "良好")
    elif 9.2 <= liunianji_nv_wushimi < 9.4:
        return (78, "及格")
    elif 9.4 <= liunianji_nv_wushimi < 9.6:
        return (76, "及格")
    elif 9.6 <= liunianji_nv_wushimi < 9.8:
        return (74, "及格")
    elif 9.8 <= liunianji_nv_wushimi < 10:
        return (72, "及格")
    elif 10 <= liunianji_nv_wushimi < 10.2:
        return (70, "及格")
    elif 10.2 <= liunianji_nv_wushimi < 10.4:
        return (68, "及格")
    elif 10.4 <= liunianji_nv_wushimi < 10.6:
        return (66, "及格")
    elif 10.6 <= liunianji_nv_wushimi < 10.8:
        return (64, "及格")
    elif 10.8 <= liunianji_nv_wushimi < 11:
        return (62, "及格")
    elif 11 <= liunianji_nv_wushimi < 11.2:
        return (60, "及格")
    elif 11.2 <= liunianji_nv_wushimi < 11.4:
        return (50, "不及格")
    elif 11.4 <= liunianji_nv_wushimi < 11.6:
        return (40, "不及格")
    elif 11.6 <= liunianji_nv_wushimi < 11.8:
        return (30, "不及格")
    elif 11.8 <= liunianji_nv_wushimi < 12:
        return (20, "不及格")
    elif 12 <= liunianji_nv_wushimi < 20:
        return (10, "不及格")
    elif 20 <= liunianji_nv_wushimi:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50米数值（单位：秒）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("10秒得分", liunianji_nv_wushimi_jisuan_fenshu(11)[0], liunianji_nv_wushimi_jisuan_fenshu(11)[1])
