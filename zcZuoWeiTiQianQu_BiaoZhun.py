##一年级   坐位体前屈   男
def yinianji_nan_zuoweitiqianqu_jisuan_fenshu(yinianji_nan_zuoweitiqianqu):
    # if not isinstance(yinianji_nan_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 30 <= yinianji_nan_zuoweitiqianqu:
        return ("太大", "超出30cm，请检查")
    elif 16.1 <= yinianji_nan_zuoweitiqianqu < 30:
        return (100, "优秀")
    elif 14.6 <= yinianji_nan_zuoweitiqianqu < 16.1:
        return (95, "优秀")
    elif 13 <= yinianji_nan_zuoweitiqianqu < 14.6:
        return (90, "优秀")
    elif 12 <= yinianji_nan_zuoweitiqianqu < 13:
        return (85, "良好")
    elif 11 <= yinianji_nan_zuoweitiqianqu < 12:
        return (80, "良好")
    elif 9.9 <= yinianji_nan_zuoweitiqianqu < 11:
        return (78, "及格")
    elif 8.8 <= yinianji_nan_zuoweitiqianqu < 9.9:
        return (76, "及格")
    elif 7.7 <= yinianji_nan_zuoweitiqianqu < 8.8:
        return (74, "及格")
    elif 6.6 <= yinianji_nan_zuoweitiqianqu < 7.7:
        return (72, "及格")
    elif 5.5 <= yinianji_nan_zuoweitiqianqu < 6.6:
        return (70, "及格")
    elif 4.4 <= yinianji_nan_zuoweitiqianqu < 5.5:
        return (68, "及格")
    elif 3.3 <= yinianji_nan_zuoweitiqianqu < 4.4:
        return (66, "及格")
    elif 2.2 <= yinianji_nan_zuoweitiqianqu < 3.3:
        return (64, "及格")
    elif 1.1 <= yinianji_nan_zuoweitiqianqu < 2.2:
        return (62, "及格")
    elif 0 <= yinianji_nan_zuoweitiqianqu < 1.1:
        return (60, "及格")
    elif -0.8 <= yinianji_nan_zuoweitiqianqu < 0:
        return (50, "不及格")
    elif -1.6 <= yinianji_nan_zuoweitiqianqu < -0.8:
        return (40, "不及格")
    elif -2.4 <= yinianji_nan_zuoweitiqianqu < -1.6:
        return (30, "不及格")
    elif -3.2 <= yinianji_nan_zuoweitiqianqu < -2.4:
        return (20, "不及格")
    elif -4 <= yinianji_nan_zuoweitiqianqu < -3.2:
        return (10, "不及格")
    elif -30 <= yinianji_nan_zuoweitiqianqu < -4:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{yinianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{yinianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{yinianji_nan_zuoweitiqianqu_jisuan_fenshu(-10)}")





##一年级   坐位体前屈   女
def yinianji_nv_zuoweitiqianqu_jisuan_fenshu(yinianji_nv_zuoweitiqianqu):
    # if not isinstance(yinianji_nv_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 30 <= yinianji_nv_zuoweitiqianqu:
        return ("太大", "超出30cm，请检查")
    elif 18.6 <= yinianji_nv_zuoweitiqianqu < 30:
        return (100, "优秀")
    elif 17.3 <= yinianji_nv_zuoweitiqianqu < 18.6:
        return (95, "优秀")
    elif 16 <= yinianji_nv_zuoweitiqianqu < 17.3:
        return (90, "优秀")
    elif 14.7 <= yinianji_nv_zuoweitiqianqu < 16:
        return (85, "良好")
    elif 13.4 <= yinianji_nv_zuoweitiqianqu < 14.7:
        return (80, "良好")
    elif 12.3 <= yinianji_nv_zuoweitiqianqu < 13.4:
        return (78, "及格")
    elif 11.2 <= yinianji_nv_zuoweitiqianqu < 12.3:
        return (76, "及格")
    elif 10.1 <= yinianji_nv_zuoweitiqianqu < 11.2:
        return (74, "及格")
    elif 9 <= yinianji_nv_zuoweitiqianqu < 10.1:
        return (72, "及格")
    elif 7.9 <= yinianji_nv_zuoweitiqianqu < 9:
        return (70, "及格")
    elif 6.8 <= yinianji_nv_zuoweitiqianqu < 7.9:
        return (68, "及格")
    elif 5.7 <= yinianji_nv_zuoweitiqianqu < 6.8:
        return (66, "及格")
    elif 4.6 <= yinianji_nv_zuoweitiqianqu < 5.7:
        return (64, "及格")
    elif 3.5 <= yinianji_nv_zuoweitiqianqu < 4.6:
        return (62, "及格")
    elif 2.4 <= yinianji_nv_zuoweitiqianqu < 3.5:
        return (60, "及格")
    elif 1.6 <= yinianji_nv_zuoweitiqianqu < 2.4:
        return (50, "不及格")
    elif 0.8 <= yinianji_nv_zuoweitiqianqu < 1.6:
        return (40, "不及格")
    elif 0 <= yinianji_nv_zuoweitiqianqu < 0.8:
        return (30, "不及格")
    elif -0.8 <= yinianji_nv_zuoweitiqianqu < 0:
        return (20, "不及格")
    elif -1.6 <= yinianji_nv_zuoweitiqianqu < -0.8:
        return (10, "不及格")
    elif -30 <= yinianji_nv_zuoweitiqianqu < -1.6:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{yinianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{yinianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{yinianji_nv_zuoweitiqianqu_jisuan_fenshu(-10)}")





##二年级   坐位体前屈   男
def ernianji_nan_zuoweitiqianqu_jisuan_fenshu(ernianji_nan_zuoweitiqianqu):
    # if not isinstance(ernianji_nan_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 40 <= ernianji_nan_zuoweitiqianqu:
        return ("太大", "超出40cm，请检查")
    elif 16.2 <= ernianji_nan_zuoweitiqianqu < 40:
        return (100, "优秀")
    elif 14.7 <= ernianji_nan_zuoweitiqianqu < 16.2:
        return (95, "优秀")
    elif 13.2 <= ernianji_nan_zuoweitiqianqu < 14.7:
        return (90, "优秀")
    elif 11.9 <= ernianji_nan_zuoweitiqianqu < 13.2:
        return (85, "良好")
    elif 10.6 <= ernianji_nan_zuoweitiqianqu < 11.9:
        return (80, "良好")
    elif 9.5 <= ernianji_nan_zuoweitiqianqu < 10.6:
        return (78, "及格")
    elif 8.4 <= ernianji_nan_zuoweitiqianqu < 9.5:
        return (76, "及格")
    elif 7.3 <= ernianji_nan_zuoweitiqianqu < 8.4:
        return (74, "及格")
    elif 6.2 <= ernianji_nan_zuoweitiqianqu < 7.3:
        return (72, "及格")
    elif 5.1 <= ernianji_nan_zuoweitiqianqu < 6.2:
        return (70, "及格")
    elif 4 <= ernianji_nan_zuoweitiqianqu < 5.1:
        return (68, "及格")
    elif 2.9 <= ernianji_nan_zuoweitiqianqu < 4:
        return (66, "及格")
    elif 1.8 <= ernianji_nan_zuoweitiqianqu < 2.9:
        return (64, "及格")
    elif 0.7 <= ernianji_nan_zuoweitiqianqu < 1.8:
        return (62, "及格")
    elif -0.4 <= ernianji_nan_zuoweitiqianqu < 0.7:
        return (60, "及格")
    elif -1.2 <= ernianji_nan_zuoweitiqianqu < -0.4:
        return (50, "不及格")
    elif -2 <= ernianji_nan_zuoweitiqianqu < -1.2:
        return (40, "不及格")
    elif -2.8 <= ernianji_nan_zuoweitiqianqu < -2:
        return (30, "不及格")
    elif -3.6 <= ernianji_nan_zuoweitiqianqu < -2.8:
        return (20, "不及格")
    elif -4.4 <= ernianji_nan_zuoweitiqianqu < -3.6:
        return (10, "不及格")
    elif -30 <= ernianji_nan_zuoweitiqianqu < -4.4:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{ernianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{ernianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{ernianji_nan_zuoweitiqianqu_jisuan_fenshu(-10)}")




##二年级   坐位体前屈   女
def ernianji_nv_zuoweitiqianqu_jisuan_fenshu(ernianji_nv_zuoweitiqianqu):
    # if not isinstance(ernianji_nv_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 40 <= ernianji_nv_zuoweitiqianqu:
        return ("太大", "超出40cm，请检查")
    elif 18.9 <= ernianji_nv_zuoweitiqianqu < 40:
        return (100, "优秀")
    elif 17.6 <= ernianji_nv_zuoweitiqianqu < 18.9:
        return (95, "优秀")
    elif 16.3 <= ernianji_nv_zuoweitiqianqu < 17.6:
        return (90, "优秀")
    elif 14.8 <= ernianji_nv_zuoweitiqianqu < 16.3:
        return (85, "良好")
    elif 13.3 <= ernianji_nv_zuoweitiqianqu < 14.8:
        return (80, "良好")
    elif 12.2 <= ernianji_nv_zuoweitiqianqu < 13.3:
        return (78, "及格")
    elif 11.1 <= ernianji_nv_zuoweitiqianqu < 12.2:
        return (76, "及格")
    elif 10 <= ernianji_nv_zuoweitiqianqu < 11.1:
        return (74, "及格")
    elif 8.9 <= ernianji_nv_zuoweitiqianqu < 10:
        return (72, "及格")
    elif 7.8 <= ernianji_nv_zuoweitiqianqu < 8.9:
        return (70, "及格")
    elif 6.7 <= ernianji_nv_zuoweitiqianqu < 7.8:
        return (68, "及格")
    elif 5.6 <= ernianji_nv_zuoweitiqianqu < 6.7:
        return (66, "及格")
    elif 4.5 <= ernianji_nv_zuoweitiqianqu < 5.6:
        return (64, "及格")
    elif 3.4 <= ernianji_nv_zuoweitiqianqu < 4.5:
        return (62, "及格")
    elif 2.3 <= ernianji_nv_zuoweitiqianqu < 3.4:
        return (60, "及格")
    elif 1.5 <= ernianji_nv_zuoweitiqianqu < 2.3:
        return (50, "不及格")
    elif 0.7 <= ernianji_nv_zuoweitiqianqu < 1.5:
        return (40, "不及格")
    elif -0.1 <= ernianji_nv_zuoweitiqianqu < 0.7:
        return (30, "不及格")
    elif -0.9 <= ernianji_nv_zuoweitiqianqu < -0.1:
        return (20, "不及格")
    elif -1.7 <= ernianji_nv_zuoweitiqianqu < -0.9:
        return (10, "不及格")
    elif -30 <= ernianji_nv_zuoweitiqianqu < -1.7:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{ernianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{ernianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{ernianji_nv_zuoweitiqianqu_jisuan_fenshu(-30)}")




##三年级   坐位体前屈   男
def sannianji_nan_zuoweitiqianqu_jisuan_fenshu(sannianji_nan_zuoweitiqianqu):
    # if not isinstance(sannianji_nan_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 40 <= sannianji_nan_zuoweitiqianqu:
        return ("太大", "超出40cm，请检查")
    elif 16.3 <= sannianji_nan_zuoweitiqianqu < 40:
        return (100, "优秀")
    elif 14.9 <= sannianji_nan_zuoweitiqianqu < 16.3:
        return (95, "优秀")
    elif 13.4 <= sannianji_nan_zuoweitiqianqu < 14.9:
        return (90, "优秀")
    elif 11.8 <= sannianji_nan_zuoweitiqianqu < 13.4:
        return (85, "良好")
    elif 10.2 <= sannianji_nan_zuoweitiqianqu < 11.8:
        return (80, "良好")
    elif 9.1 <= sannianji_nan_zuoweitiqianqu < 10.2:
        return (78, "及格")
    elif 8 <= sannianji_nan_zuoweitiqianqu < 9.1:
        return (76, "及格")
    elif 6.9 <= sannianji_nan_zuoweitiqianqu < 8:
        return (74, "及格")
    elif 5.8 <= sannianji_nan_zuoweitiqianqu < 6.9:
        return (72, "及格")
    elif 4.7 <= sannianji_nan_zuoweitiqianqu < 5.8:
        return (70, "及格")
    elif 3.6 <= sannianji_nan_zuoweitiqianqu < 4.7:
        return (68, "及格")
    elif 2.5 <= sannianji_nan_zuoweitiqianqu < 3.6:
        return (66, "及格")
    elif 1.4 <= sannianji_nan_zuoweitiqianqu < 2.5:
        return (64, "及格")
    elif 0.3 <= sannianji_nan_zuoweitiqianqu < 1.4:
        return (62, "及格")
    elif -0.8 <= sannianji_nan_zuoweitiqianqu < 0.3:
        return (60, "及格")
    elif -1.6 <= sannianji_nan_zuoweitiqianqu < -0.8:
        return (50, "不及格")
    elif -2.4 <= sannianji_nan_zuoweitiqianqu < -1.6:
        return (40, "不及格")
    elif -3.2 <= sannianji_nan_zuoweitiqianqu < -2.4:
        return (30, "不及格")
    elif -4 <= sannianji_nan_zuoweitiqianqu < -3.2:
        return (20, "不及格")
    elif -4.8 <= sannianji_nan_zuoweitiqianqu < -4:
        return (10, "不及格")
    elif -30 <= sannianji_nan_zuoweitiqianqu < -4.8:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{sannianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{sannianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{sannianji_nan_zuoweitiqianqu_jisuan_fenshu(-10)}")



##三年级   坐位体前屈   女
def sannianji_nv_zuoweitiqianqu_jisuan_fenshu(sannianji_nv_zuoweitiqianqu):
    # if not isinstance(sannianji_nv_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 40 <= sannianji_nv_zuoweitiqianqu:
        return ("太大", "超出40cm，请检查")
    elif 19.2 <= sannianji_nv_zuoweitiqianqu < 40:
        return (100, "优秀")
    elif 17.9 <= sannianji_nv_zuoweitiqianqu < 19.2:
        return (95, "优秀")
    elif 16.6 <= sannianji_nv_zuoweitiqianqu < 17.9:
        return (90, "优秀")
    elif 14.9 <= sannianji_nv_zuoweitiqianqu < 16.6:
        return (85, "良好")
    elif 13.2 <= sannianji_nv_zuoweitiqianqu < 14.9:
        return (80, "良好")
    elif 12.1 <= sannianji_nv_zuoweitiqianqu < 13.2:
        return (78, "及格")
    elif 11 <= sannianji_nv_zuoweitiqianqu < 12.1:
        return (76, "及格")
    elif 9.9 <= sannianji_nv_zuoweitiqianqu < 11:
        return (74, "及格")
    elif 8.8 <= sannianji_nv_zuoweitiqianqu < 9.9:
        return (72, "及格")
    elif 7.7 <= sannianji_nv_zuoweitiqianqu < 8.8:
        return (70, "及格")
    elif 6.6 <= sannianji_nv_zuoweitiqianqu < 7.7:
        return (68, "及格")
    elif 5.5 <= sannianji_nv_zuoweitiqianqu < 6.6:
        return (66, "及格")
    elif 4.4 <= sannianji_nv_zuoweitiqianqu < 5.5:
        return (64, "及格")
    elif 3.3 <= sannianji_nv_zuoweitiqianqu < 4.4:
        return (62, "及格")
    elif 2.2 <= sannianji_nv_zuoweitiqianqu < 3.3:
        return (60, "及格")
    elif 1.4 <= sannianji_nv_zuoweitiqianqu < 2.2:
        return (50, "不及格")
    elif 0.6 <= sannianji_nv_zuoweitiqianqu < 1.4:
        return (40, "不及格")
    elif -0.2 <= sannianji_nv_zuoweitiqianqu < 0.6:
        return (30, "不及格")
    elif -1 <= sannianji_nv_zuoweitiqianqu < -0.2:
        return (20, "不及格")
    elif -1.8 <= sannianji_nv_zuoweitiqianqu < -1:
        return (10, "不及格")
    elif -30 <= sannianji_nv_zuoweitiqianqu < -1.8:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{sannianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{sannianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{sannianji_nv_zuoweitiqianqu_jisuan_fenshu(-30)}")




##四年级   坐位体前屈   男
def sinianji_nan_zuoweitiqianqu_jisuan_fenshu(sinianji_nan_zuoweitiqianqu):
    # if not isinstance(sinianji_nan_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 40 <= sinianji_nan_zuoweitiqianqu:
        return ("太大", "超出40cm，请检查")
    elif 16.4 <= sinianji_nan_zuoweitiqianqu < 40:
        return (100, "优秀")
    elif 15 <= sinianji_nan_zuoweitiqianqu < 16.4:
        return (95, "优秀")
    elif 13.6 <= sinianji_nan_zuoweitiqianqu < 15:
        return (90, "优秀")
    elif 11.7 <= sinianji_nan_zuoweitiqianqu < 13.6:
        return (85, "良好")
    elif 9.8 <= sinianji_nan_zuoweitiqianqu < 11.7:
        return (80, "良好")
    elif 8.6 <= sinianji_nan_zuoweitiqianqu < 9.8:
        return (78, "及格")
    elif 7.4 <= sinianji_nan_zuoweitiqianqu < 8.6:
        return (76, "及格")
    elif 6.2 <= sinianji_nan_zuoweitiqianqu < 7.4:
        return (74, "及格")
    elif 5 <= sinianji_nan_zuoweitiqianqu < 6.2:
        return (72, "及格")
    elif 3.8 <= sinianji_nan_zuoweitiqianqu < 5:
        return (70, "及格")
    elif 2.6 <= sinianji_nan_zuoweitiqianqu < 3.8:
        return (68, "及格")
    elif 1.4 <= sinianji_nan_zuoweitiqianqu < 2.6:
        return (66, "及格")
    elif 0.2 <= sinianji_nan_zuoweitiqianqu < 1.4:
        return (64, "及格")
    elif -1 <= sinianji_nan_zuoweitiqianqu < 0.2:
        return (62, "及格")
    elif -2.2 <= sinianji_nan_zuoweitiqianqu < -1:
        return (60, "及格")
    elif -3.2 <= sinianji_nan_zuoweitiqianqu < -2.2:
        return (50, "不及格")
    elif -4.2 <= sinianji_nan_zuoweitiqianqu < -3.2:
        return (40, "不及格")
    elif -5.2 <= sinianji_nan_zuoweitiqianqu < -4.2:
        return (30, "不及格")
    elif -6.2 <= sinianji_nan_zuoweitiqianqu < -5.2:
        return (20, "不及格")
    elif -7.2 <= sinianji_nan_zuoweitiqianqu < -6.2:
        return (10, "不及格")
    elif -30 <= sinianji_nan_zuoweitiqianqu < -7.2:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{sinianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{sinianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{sinianji_nan_zuoweitiqianqu_jisuan_fenshu(-10)}")






##四年级   坐位体前屈   女
def sinianji_nv_zuoweitiqianqu_jisuan_fenshu(sinianji_nv_zuoweitiqianqu):
    # if not isinstance(sinianji_nv_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 40 <= sinianji_nv_zuoweitiqianqu:
        return ("太大", "超出40cm，请检查")
    elif 19.5 <= sinianji_nv_zuoweitiqianqu < 40:
        return (100, "优秀")
    elif 18.1 <= sinianji_nv_zuoweitiqianqu < 19.5:
        return (95, "优秀")
    elif 16.9 <= sinianji_nv_zuoweitiqianqu < 18.1:
        return (90, "优秀")
    elif 15 <= sinianji_nv_zuoweitiqianqu < 16.9:
        return (85, "良好")
    elif 13.1 <= sinianji_nv_zuoweitiqianqu < 15:
        return (80, "良好")
    elif 12 <= sinianji_nv_zuoweitiqianqu < 13.1:
        return (78, "及格")
    elif 10.9 <= sinianji_nv_zuoweitiqianqu < 12:
        return (76, "及格")
    elif 9.8 <= sinianji_nv_zuoweitiqianqu < 10.9:
        return (74, "及格")
    elif 8.7 <= sinianji_nv_zuoweitiqianqu < 9.8:
        return (72, "及格")
    elif 7.6 <= sinianji_nv_zuoweitiqianqu < 8.7:
        return (70, "及格")
    elif 6.5 <= sinianji_nv_zuoweitiqianqu < 7.6:
        return (68, "及格")
    elif 5.4 <= sinianji_nv_zuoweitiqianqu < 6.5:
        return (66, "及格")
    elif 4.3 <= sinianji_nv_zuoweitiqianqu < 5.4:
        return (64, "及格")
    elif 3.2 <= sinianji_nv_zuoweitiqianqu < 4.3:
        return (62, "及格")
    elif 2.1 <= sinianji_nv_zuoweitiqianqu < 3.2:
        return (60, "及格")
    elif 1.3 <= sinianji_nv_zuoweitiqianqu < 2.1:
        return (50, "不及格")
    elif 0.5 <= sinianji_nv_zuoweitiqianqu < 1.3:
        return (40, "不及格")
    elif -0.3 <= sinianji_nv_zuoweitiqianqu < 0.5:
        return (30, "不及格")
    elif -1.1 <= sinianji_nv_zuoweitiqianqu < -0.3:
        return (20, "不及格")
    elif -1.9 <= sinianji_nv_zuoweitiqianqu < -1.1:
        return (10, "不及格")
    elif -30 <= sinianji_nv_zuoweitiqianqu < -1.9:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{sinianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{sinianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{sinianji_nv_zuoweitiqianqu_jisuan_fenshu(-30)}")





##五年级   坐位体前屈   男
def wunianji_nan_zuoweitiqianqu_jisuan_fenshu(wunianji_nan_zuoweitiqianqu):
    # if not isinstance(wunianji_nan_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 40 <= wunianji_nan_zuoweitiqianqu:
        return ("太大", "超出40cm，请检查")
    elif 16.5 <= wunianji_nan_zuoweitiqianqu < 40:
        return (100, "优秀")
    elif 15.2 <= wunianji_nan_zuoweitiqianqu < 16.5:
        return (95, "优秀")
    elif 13.8 <= wunianji_nan_zuoweitiqianqu < 15.2:
        return (90, "优秀")
    elif 11.6 <= wunianji_nan_zuoweitiqianqu < 13.8:
        return (85, "良好")
    elif 9.4 <= wunianji_nan_zuoweitiqianqu < 11.6:
        return (80, "良好")
    elif 8.2 <= wunianji_nan_zuoweitiqianqu < 9.4:
        return (78, "及格")
    elif 7 <= wunianji_nan_zuoweitiqianqu < 8.2:
        return (76, "及格")
    elif 5.8 <= wunianji_nan_zuoweitiqianqu < 7:
        return (74, "及格")
    elif 4.6 <= wunianji_nan_zuoweitiqianqu < 5.8:
        return (72, "及格")
    elif 3.4 <= wunianji_nan_zuoweitiqianqu < 4.6:
        return (70, "及格")
    elif 2.2 <= wunianji_nan_zuoweitiqianqu < 3.4:
        return (68, "及格")
    elif 1 <= wunianji_nan_zuoweitiqianqu < 2.2:
        return (66, "及格")
    elif -0.2 <= wunianji_nan_zuoweitiqianqu < 1:
        return (64, "及格")
    elif -1.4 <= wunianji_nan_zuoweitiqianqu < -0.2:
        return (62, "及格")
    elif -2.6 <= wunianji_nan_zuoweitiqianqu < -1.4:
        return (60, "及格")
    elif -3.6 <= wunianji_nan_zuoweitiqianqu < -2.6:
        return (50, "不及格")
    elif -4.6 <= wunianji_nan_zuoweitiqianqu < -3.6:
        return (40, "不及格")
    elif -5.6 <= wunianji_nan_zuoweitiqianqu < -4.6:
        return (30, "不及格")
    elif -6.6 <= wunianji_nan_zuoweitiqianqu < -5.6:
        return (20, "不及格")
    elif -7.6 <= wunianji_nan_zuoweitiqianqu < -6.6:
        return (10, "不及格")
    elif -30 <= wunianji_nan_zuoweitiqianqu < -7.6:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{wunianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{wunianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{wunianji_nan_zuoweitiqianqu_jisuan_fenshu(-10)}")




##五年级   坐位体前屈   女
def wunianji_nv_zuoweitiqianqu_jisuan_fenshu(wunianji_nv_zuoweitiqianqu):
    # if not isinstance(wunianji_nv_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 40 <= wunianji_nv_zuoweitiqianqu:
        return ("太大", "超出40cm，请检查")
    elif 19.8 <= wunianji_nv_zuoweitiqianqu < 40:
        return (100, "优秀")
    elif 18.5 <= wunianji_nv_zuoweitiqianqu < 19.8:
        return (95, "优秀")
    elif 17.2 <= wunianji_nv_zuoweitiqianqu < 18.5:
        return (90, "优秀")
    elif 15.1 <= wunianji_nv_zuoweitiqianqu < 17.2:
        return (85, "良好")
    elif 13 <= wunianji_nv_zuoweitiqianqu < 15.1:
        return (80, "良好")
    elif 11.9 <= wunianji_nv_zuoweitiqianqu < 13:
        return (78, "及格")
    elif 10.8 <= wunianji_nv_zuoweitiqianqu < 11.9:
        return (76, "及格")
    elif 9.7 <= wunianji_nv_zuoweitiqianqu < 10.8:
        return (74, "及格")
    elif 8.6 <= wunianji_nv_zuoweitiqianqu < 9.7:
        return (72, "及格")
    elif 7.5 <= wunianji_nv_zuoweitiqianqu < 8.6:
        return (70, "及格")
    elif 6.4 <= wunianji_nv_zuoweitiqianqu < 7.5:
        return (68, "及格")
    elif 5.3 <= wunianji_nv_zuoweitiqianqu < 6.4:
        return (66, "及格")
    elif 4.2 <= wunianji_nv_zuoweitiqianqu < 5.3:
        return (64, "及格")
    elif 3.1 <= wunianji_nv_zuoweitiqianqu < 4.2:
        return (62, "及格")
    elif 2 <= wunianji_nv_zuoweitiqianqu < 3.1:
        return (60, "及格")
    elif 1.2 <= wunianji_nv_zuoweitiqianqu < 2:
        return (50, "不及格")
    elif 0.4 <= wunianji_nv_zuoweitiqianqu < 1.2:
        return (40, "不及格")
    elif -0.4 <= wunianji_nv_zuoweitiqianqu < 0.4:
        return (30, "不及格")
    elif -1.2 <= wunianji_nv_zuoweitiqianqu < -0.4:
        return (20, "不及格")
    elif -2 <= wunianji_nv_zuoweitiqianqu < -1.2:
        return (10, "不及格")
    elif -30 <= wunianji_nv_zuoweitiqianqu < -2:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{wunianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{wunianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{wunianji_nv_zuoweitiqianqu_jisuan_fenshu(-30)}")






##六年级   坐位体前屈   男
def liunianji_nan_zuoweitiqianqu_jisuan_fenshu(liunianji_nan_zuoweitiqianqu):
    # if not isinstance(liunianji_nan_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 40 <= liunianji_nan_zuoweitiqianqu:
        return ("太大", "超出40cm，请检查")
    elif 16.6 <= liunianji_nan_zuoweitiqianqu < 40:
        return (100, "优秀")
    elif 15.3 <= liunianji_nan_zuoweitiqianqu < 16.6:
        return (95, "优秀")
    elif 14 <= liunianji_nan_zuoweitiqianqu < 15.3:
        return (90, "优秀")
    elif 11.5 <= liunianji_nan_zuoweitiqianqu < 14:
        return (85, "良好")
    elif 9 <= liunianji_nan_zuoweitiqianqu < 11.5:
        return (80, "良好")
    elif 7.7 <= liunianji_nan_zuoweitiqianqu < 9:
        return (78, "及格")
    elif 6.4 <= liunianji_nan_zuoweitiqianqu < 7.7:
        return (76, "及格")
    elif 5.1 <= liunianji_nan_zuoweitiqianqu < 6.4:
        return (74, "及格")
    elif 3.8 <= liunianji_nan_zuoweitiqianqu < 5.1:
        return (72, "及格")
    elif 2.5 <= liunianji_nan_zuoweitiqianqu < 3.8:
        return (70, "及格")
    elif 1.2 <= liunianji_nan_zuoweitiqianqu < 2.5:
        return (68, "及格")
    elif -0.1 <= liunianji_nan_zuoweitiqianqu < 1.2:
        return (66, "及格")
    elif -1.4 <= liunianji_nan_zuoweitiqianqu < -0.1:
        return (64, "及格")
    elif -2.7 <= liunianji_nan_zuoweitiqianqu < -1.4:
        return (62, "及格")
    elif -4 <= liunianji_nan_zuoweitiqianqu < -2.7:
        return (60, "及格")
    elif -5 <= liunianji_nan_zuoweitiqianqu < -4:
        return (50, "不及格")
    elif -6 <= liunianji_nan_zuoweitiqianqu < -5:
        return (40, "不及格")
    elif -7 <= liunianji_nan_zuoweitiqianqu < -6:
        return (30, "不及格")
    elif -8 <= liunianji_nan_zuoweitiqianqu < -7:
        return (20, "不及格")
    elif -9 <= liunianji_nan_zuoweitiqianqu < -8:
        return (10, "不及格")
    elif -30 <= liunianji_nan_zuoweitiqianqu < -9:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{liunianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{liunianji_nan_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{liunianji_nan_zuoweitiqianqu_jisuan_fenshu(-10)}")



##六年级   坐位体前屈   女
def liunianji_nv_zuoweitiqianqu_jisuan_fenshu(liunianji_nv_zuoweitiqianqu):
    # if not isinstance(liunianji_nv_zuoweitiqianqu, (int, float)):
    #     return ValueError("请传入有效的数字类型坐位体前屈数值（单位：cm）")
    if 40 <= liunianji_nv_zuoweitiqianqu:
        return ("太大", "超出40cm，请检查")
    elif 19.9 <= liunianji_nv_zuoweitiqianqu < 40:
        return (100, "优秀")
    elif 18.7 <= liunianji_nv_zuoweitiqianqu < 19.9:
        return (95, "优秀")
    elif 17.5 <= liunianji_nv_zuoweitiqianqu < 18.7:
        return (90, "优秀")
    elif 15.2 <= liunianji_nv_zuoweitiqianqu < 17.5:
        return (85, "良好")
    elif 12.9 <= liunianji_nv_zuoweitiqianqu < 15.2:
        return (80, "良好")
    elif 11.8 <= liunianji_nv_zuoweitiqianqu < 12.9:
        return (78, "及格")
    elif 10.7 <= liunianji_nv_zuoweitiqianqu < 11.8:
        return (76, "及格")
    elif 9.6 <= liunianji_nv_zuoweitiqianqu < 10.7:
        return (74, "及格")
    elif 8.5 <= liunianji_nv_zuoweitiqianqu < 9.6:
        return (72, "及格")
    elif 7.4 <= liunianji_nv_zuoweitiqianqu < 8.5:
        return (70, "及格")
    elif 6.3 <= liunianji_nv_zuoweitiqianqu < 7.4:
        return (68, "及格")
    elif 5.2 <= liunianji_nv_zuoweitiqianqu < 6.3:
        return (66, "及格")
    elif 4.1 <= liunianji_nv_zuoweitiqianqu < 5.2:
        return (64, "及格")
    elif 3 <= liunianji_nv_zuoweitiqianqu < 4.1:
        return (62, "及格")
    elif 1.9 <= liunianji_nv_zuoweitiqianqu < 3:
        return (60, "及格")
    elif 1.1 <= liunianji_nv_zuoweitiqianqu < 1.9:
        return (50, "不及格")
    elif 0.3 <= liunianji_nv_zuoweitiqianqu < 1.1:
        return (40, "不及格")
    elif -0.5 <= liunianji_nv_zuoweitiqianqu < 0.3:
        return (30, "不及格")
    elif -1.3 <= liunianji_nv_zuoweitiqianqu < -0.5:
        return (20, "不及格")
    elif -2.1 <= liunianji_nv_zuoweitiqianqu < -1.3:
        return (10, "不及格")
    elif -30 <= liunianji_nv_zuoweitiqianqu < -2.1:
        return (0, "不及格")
    else:
        return 0


# 直接运行此文件时执行
# 测试
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"得分：{liunianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[0]}")
    print(f"得分：{liunianji_nv_zuoweitiqianqu_jisuan_fenshu(0)[1]}")
    print(f"得分：{liunianji_nv_zuoweitiqianqu_jisuan_fenshu(-30)}")
