### 一年级男生跳绳标准
def yinianji_nan_tiaosheng_jisuan_fenshu(yinianji_nan_tiaosheng):
    # if isinstance(yinianji_nan_tiaosheng, float):
    #     return "男生跳绳请输入整数"
    # if not isinstance(yinianji_nan_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if yinianji_nan_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 149 <= yinianji_nan_tiaosheng < 500:
        return (120, "优秀")
    elif 147 <= yinianji_nan_tiaosheng < 149:
        return (119, "优秀")
    elif 145 <= yinianji_nan_tiaosheng < 147:
        return (118, "优秀")
    elif 143 <= yinianji_nan_tiaosheng < 145:
        return (117, "优秀")
    elif 141 <= yinianji_nan_tiaosheng < 143:
        return (116, "优秀")
    elif 139 <= yinianji_nan_tiaosheng < 141:
        return (115, "优秀")
    elif 137 <= yinianji_nan_tiaosheng < 139:
        return (114, "优秀")
    elif 135 <= yinianji_nan_tiaosheng < 137:
        return (113, "优秀")
    elif 133 <= yinianji_nan_tiaosheng < 135:
        return (112, "优秀")
    elif 131 <= yinianji_nan_tiaosheng < 133:
        return (111, "优秀")
    elif 129 <= yinianji_nan_tiaosheng < 131:
        return (110, "优秀")
    elif 127 <= yinianji_nan_tiaosheng < 129:
        return (109, "优秀")
    elif 125 <= yinianji_nan_tiaosheng < 127:
        return (108, "优秀")
    elif 123 <= yinianji_nan_tiaosheng < 125:
        return (107, "优秀")
    elif 121 <= yinianji_nan_tiaosheng < 123:
        return (106, "优秀")
    elif 119 <= yinianji_nan_tiaosheng < 121:
        return (105, "优秀")
    elif 117 <= yinianji_nan_tiaosheng < 119:
        return (104, "优秀")
    elif 115 <= yinianji_nan_tiaosheng < 117:
        return (103, "优秀")
    elif 113 <= yinianji_nan_tiaosheng < 115:
        return (102, "优秀")
    elif 111 <= yinianji_nan_tiaosheng < 113:
        return (101, "优秀")
    elif 109 <= yinianji_nan_tiaosheng < 111:
        return (100, "优秀")
    elif 104 <= yinianji_nan_tiaosheng < 109:
        return (95, "优秀")
    elif 99 <= yinianji_nan_tiaosheng < 104:
        return (90, "优秀")
    elif 93 <= yinianji_nan_tiaosheng < 99:
        return (85, "良好")
    elif 87 <= yinianji_nan_tiaosheng < 93:
        return (80, "良好")
    elif 80 <= yinianji_nan_tiaosheng < 87:
        return (78, "及格")
    elif 73 <= yinianji_nan_tiaosheng < 80:
        return (76, "及格")
    elif 66 <= yinianji_nan_tiaosheng < 73:
        return (74, "及格")
    elif 59 <= yinianji_nan_tiaosheng < 66:
        return (72, "及格")
    elif 52 <= yinianji_nan_tiaosheng < 59:
        return (70, "及格")
    elif 45 <= yinianji_nan_tiaosheng < 52:
        return (68, "及格")
    elif 38 <= yinianji_nan_tiaosheng < 45:
        return (66, "及格")
    elif 31 <= yinianji_nan_tiaosheng < 38:
        return (64, "及格")
    elif 24 <= yinianji_nan_tiaosheng < 31:
        return (62, "及格")
    elif 17 <= yinianji_nan_tiaosheng < 24:
        return (60, "及格")
    elif 14 <= yinianji_nan_tiaosheng < 17:
        return (50, "不及格")
    elif 11 <= yinianji_nan_tiaosheng < 14:
        return (40, "不及格")
    elif 8 <= yinianji_nan_tiaosheng < 11:
        return (30, "不及格")
    elif 5 <= yinianji_nan_tiaosheng < 8:
        return (20, "不及格")
    elif 2 <= yinianji_nan_tiaosheng < 5:
        return (10, "不及格")
    elif 0 <= yinianji_nan_tiaosheng < 2:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{yinianji_nan_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{yinianji_nan_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{yinianji_nan_tiaosheng_jisuan_fenshu(100)}")  # 输出90


### 一年级女生跳绳标准
def yinianji_nv_tiaosheng_jisuan_fenshu(yinianji_nv_tiaosheng):
    # if isinstance(yinianji_nv_tiaosheng, float):
    #     return "女生跳绳请输入整数"
    # if not isinstance(yinianji_nv_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if yinianji_nv_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 157 <= yinianji_nv_tiaosheng < 500:
        return (120, "优秀")
    elif 155 <= yinianji_nv_tiaosheng < 157:
        return (119, "优秀")
    elif 153 <= yinianji_nv_tiaosheng < 155:
        return (118, "优秀")
    elif 151 <= yinianji_nv_tiaosheng < 153:
        return (117, "优秀")
    elif 149 <= yinianji_nv_tiaosheng < 151:
        return (116, "优秀")
    elif 147 <= yinianji_nv_tiaosheng < 149:
        return (115, "优秀")
    elif 145 <= yinianji_nv_tiaosheng < 147:
        return (114, "优秀")
    elif 143 <= yinianji_nv_tiaosheng < 145:
        return (113, "优秀")
    elif 141 <= yinianji_nv_tiaosheng < 143:
        return (112, "优秀")
    elif 139 <= yinianji_nv_tiaosheng < 141:
        return (111, "优秀")
    elif 137 <= yinianji_nv_tiaosheng < 139:
        return (110, "优秀")
    elif 135 <= yinianji_nv_tiaosheng < 137:
        return (109, "优秀")
    elif 133 <= yinianji_nv_tiaosheng < 135:
        return (108, "优秀")
    elif 131 <= yinianji_nv_tiaosheng < 133:
        return (107, "优秀")
    elif 129 <= yinianji_nv_tiaosheng < 131:
        return (106, "优秀")
    elif 127 <= yinianji_nv_tiaosheng < 129:
        return (105, "优秀")
    elif 125 <= yinianji_nv_tiaosheng < 127:
        return (104, "优秀")
    elif 123 <= yinianji_nv_tiaosheng < 125:
        return (103, "优秀")
    elif 121 <= yinianji_nv_tiaosheng < 123:
        return (102, "优秀")
    elif 119 <= yinianji_nv_tiaosheng < 121:
        return (101, "优秀")
    elif 117 <= yinianji_nv_tiaosheng < 119:
        return (100, "优秀")
    elif 110 <= yinianji_nv_tiaosheng < 117:
        return (95, "优秀")
    elif 103 <= yinianji_nv_tiaosheng < 110:
        return (90, "优秀")
    elif 95 <= yinianji_nv_tiaosheng < 103:
        return (85, "良好")
    elif 87 <= yinianji_nv_tiaosheng < 95:
        return (80, "良好")
    elif 80 <= yinianji_nv_tiaosheng < 87:
        return (78, "及格")
    elif 73 <= yinianji_nv_tiaosheng < 80:
        return (76, "及格")
    elif 66 <= yinianji_nv_tiaosheng < 73:
        return (74, "及格")
    elif 59 <= yinianji_nv_tiaosheng < 66:
        return (72, "及格")
    elif 52 <= yinianji_nv_tiaosheng < 59:
        return (70, "及格")
    elif 45 <= yinianji_nv_tiaosheng < 52:
        return (68, "及格")
    elif 38 <= yinianji_nv_tiaosheng < 45:
        return (66, "及格")
    elif 31 <= yinianji_nv_tiaosheng < 38:
        return (64, "及格")
    elif 24 <= yinianji_nv_tiaosheng < 31:
        return (62, "及格")
    elif 17 <= yinianji_nv_tiaosheng < 24:
        return (60, "及格")
    elif 14 <= yinianji_nv_tiaosheng < 17:
        return (50, "不及格")
    elif 11 <= yinianji_nv_tiaosheng < 14:
        return (40, "不及格")
    elif 8 <= yinianji_nv_tiaosheng < 11:
        return (30, "不及格")
    elif 5 <= yinianji_nv_tiaosheng < 8:
        return (20, "不及格")
    elif 2 <= yinianji_nv_tiaosheng < 5:
        return (10, "不及格")
    elif 0 <= yinianji_nv_tiaosheng < 2:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{yinianji_nv_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{yinianji_nv_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{yinianji_nv_tiaosheng_jisuan_fenshu(100)}")  # 输出90




### 二年级男生跳绳标准
def ernianji_nan_tiaosheng_jisuan_fenshu(ernianji_nan_tiaosheng):
    # if isinstance(ernianji_nan_tiaosheng, float):
    #     return "男生跳绳请输入整数"
    # if not isinstance(ernianji_nan_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if ernianji_nan_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 157 <= ernianji_nan_tiaosheng < 500:
        return (120, "优秀")
    elif 155 <= ernianji_nan_tiaosheng < 157:
        return (119, "优秀")
    elif 153 <= ernianji_nan_tiaosheng < 155:
        return (118, "优秀")
    elif 151 <= ernianji_nan_tiaosheng < 153:
        return (117, "优秀")
    elif 149 <= ernianji_nan_tiaosheng < 151:
        return (116, "优秀")
    elif 147 <= ernianji_nan_tiaosheng < 149:
        return (115, "优秀")
    elif 145 <= ernianji_nan_tiaosheng < 147:
        return (114, "优秀")
    elif 143 <= ernianji_nan_tiaosheng < 145:
        return (113, "优秀")
    elif 141 <= ernianji_nan_tiaosheng < 143:
        return (112, "优秀")
    elif 139 <= ernianji_nan_tiaosheng < 141:
        return (111, "优秀")
    elif 137 <= ernianji_nan_tiaosheng < 139:
        return (110, "优秀")
    elif 135 <= ernianji_nan_tiaosheng < 137:
        return (109, "优秀")
    elif 133 <= ernianji_nan_tiaosheng < 135:
        return (108, "优秀")
    elif 131 <= ernianji_nan_tiaosheng < 133:
        return (107, "优秀")
    elif 129 <= ernianji_nan_tiaosheng < 131:
        return (106, "优秀")
    elif 127 <= ernianji_nan_tiaosheng < 129:
        return (105, "优秀")
    elif 125 <= ernianji_nan_tiaosheng < 127:
        return (104, "优秀")
    elif 123 <= ernianji_nan_tiaosheng < 125:
        return (103, "优秀")
    elif 121 <= ernianji_nan_tiaosheng < 123:
        return (102, "优秀")
    elif 119 <= ernianji_nan_tiaosheng < 121:
        return (101, "优秀")
    elif 117 <= ernianji_nan_tiaosheng < 119:
        return (100, "优秀")
    elif 112 <= ernianji_nan_tiaosheng < 117:
        return (95, "优秀")
    elif 107 <= ernianji_nan_tiaosheng < 112:
        return (90, "优秀")
    elif 101 <= ernianji_nan_tiaosheng < 107:
        return (85, "良好")
    elif 95 <= ernianji_nan_tiaosheng < 101:
        return (80, "良好")
    elif 88 <= ernianji_nan_tiaosheng < 95:
        return (78, "及格")
    elif 81 <= ernianji_nan_tiaosheng < 88:
        return (76, "及格")
    elif 74 <= ernianji_nan_tiaosheng < 81:
        return (74, "及格")
    elif 67 <= ernianji_nan_tiaosheng < 74:
        return (72, "及格")
    elif 60 <= ernianji_nan_tiaosheng < 67:
        return (70, "及格")
    elif 53 <= ernianji_nan_tiaosheng < 60:
        return (68, "及格")
    elif 46 <= ernianji_nan_tiaosheng < 53:
        return (66, "及格")
    elif 39 <= ernianji_nan_tiaosheng < 46:
        return (64, "及格")
    elif 32 <= ernianji_nan_tiaosheng < 39:
        return (62, "及格")
    elif 25 <= ernianji_nan_tiaosheng < 32:
        return (60, "及格")
    elif 22 <= ernianji_nan_tiaosheng < 25:
        return (50, "不及格")
    elif 19 <= ernianji_nan_tiaosheng < 22:
        return (40, "不及格")
    elif 16 <= ernianji_nan_tiaosheng < 19:
        return (30, "不及格")
    elif 13 <= ernianji_nan_tiaosheng < 16:
        return (20, "不及格")
    elif 10 <= ernianji_nan_tiaosheng < 13:
        return (10, "不及格")
    elif 0 <= ernianji_nan_tiaosheng < 10:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{ernianji_nan_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{ernianji_nan_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{ernianji_nan_tiaosheng_jisuan_fenshu(100)}")  # 输出90



### 二年级女生跳绳标准
def ernianji_nv_tiaosheng_jisuan_fenshu(ernianji_nv_tiaosheng):
    # if isinstance(ernianji_nv_tiaosheng, float):
    #     return "女生跳绳请输入整数"
    # if not isinstance(ernianji_nv_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if ernianji_nv_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 167 <= ernianji_nv_tiaosheng < 500:
        return (120, "优秀")
    elif 165 <= ernianji_nv_tiaosheng < 167:
        return (119, "优秀")
    elif 163 <= ernianji_nv_tiaosheng < 165:
        return (118, "优秀")
    elif 161 <= ernianji_nv_tiaosheng < 163:
        return (117, "优秀")
    elif 159 <= ernianji_nv_tiaosheng < 161:
        return (116, "优秀")
    elif 157 <= ernianji_nv_tiaosheng < 159:
        return (115, "优秀")
    elif 155 <= ernianji_nv_tiaosheng < 157:
        return (114, "优秀")
    elif 153 <= ernianji_nv_tiaosheng < 155:
        return (113, "优秀")
    elif 151 <= ernianji_nv_tiaosheng < 153:
        return (112, "优秀")
    elif 149 <= ernianji_nv_tiaosheng < 151:
        return (111, "优秀")
    elif 147 <= ernianji_nv_tiaosheng < 149:
        return (110, "优秀")
    elif 145 <= ernianji_nv_tiaosheng < 147:
        return (109, "优秀")
    elif 143 <= ernianji_nv_tiaosheng < 145:
        return (108, "优秀")
    elif 141 <= ernianji_nv_tiaosheng < 143:
        return (107, "优秀")
    elif 139 <= ernianji_nv_tiaosheng < 141:
        return (106, "优秀")
    elif 137 <= ernianji_nv_tiaosheng < 139:
        return (105, "优秀")
    elif 135 <= ernianji_nv_tiaosheng < 137:
        return (104, "优秀")
    elif 133 <= ernianji_nv_tiaosheng < 135:
        return (103, "优秀")
    elif 131 <= ernianji_nv_tiaosheng < 133:
        return (102, "优秀")
    elif 129 <= ernianji_nv_tiaosheng < 131:
        return (101, "优秀")
    elif 127 <= ernianji_nv_tiaosheng < 129:
        return (100, "优秀")
    elif 120 <= ernianji_nv_tiaosheng < 127:
        return (95, "优秀")
    elif 113 <= ernianji_nv_tiaosheng < 120:
        return (90, "优秀")
    elif 105 <= ernianji_nv_tiaosheng < 113:
        return (85, "良好")
    elif 97 <= ernianji_nv_tiaosheng < 105:
        return (80, "良好")
    elif 90 <= ernianji_nv_tiaosheng < 97:
        return (78, "及格")
    elif 83 <= ernianji_nv_tiaosheng < 90:
        return (76, "及格")
    elif 76 <= ernianji_nv_tiaosheng < 83:
        return (74, "及格")
    elif 69 <= ernianji_nv_tiaosheng < 76:
        return (72, "及格")
    elif 62 <= ernianji_nv_tiaosheng < 69:
        return (70, "及格")
    elif 55 <= ernianji_nv_tiaosheng < 62:
        return (68, "及格")
    elif 48 <= ernianji_nv_tiaosheng < 55:
        return (66, "及格")
    elif 41 <= ernianji_nv_tiaosheng < 48:
        return (64, "及格")
    elif 34 <= ernianji_nv_tiaosheng < 41:
        return (62, "及格")
    elif 27 <= ernianji_nv_tiaosheng < 34:
        return (60, "及格")
    elif 24 <= ernianji_nv_tiaosheng < 27:
        return (50, "不及格")
    elif 21 <= ernianji_nv_tiaosheng < 24:
        return (40, "不及格")
    elif 18 <= ernianji_nv_tiaosheng < 21:
        return (30, "不及格")
    elif 15 <= ernianji_nv_tiaosheng < 18:
        return (20, "不及格")
    elif 12 <= ernianji_nv_tiaosheng < 15:
        return (10, "不及格")
    elif 0 <= ernianji_nv_tiaosheng < 12:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{ernianji_nv_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{ernianji_nv_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{ernianji_nv_tiaosheng_jisuan_fenshu(100)}")  # 输出90



### 三年级男生跳绳标准
def sannianji_nan_tiaosheng_jisuan_fenshu(sannianji_nan_tiaosheng):
    # if isinstance(sannianji_nan_tiaosheng, float):
    #     return "男生跳绳请输入整数"
    # if not isinstance(sannianji_nan_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if sannianji_nan_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 166 <= sannianji_nan_tiaosheng < 500:
        return (120, "优秀")
    elif 164 <= sannianji_nan_tiaosheng < 166:
        return (119, "优秀")
    elif 162 <= sannianji_nan_tiaosheng < 164:
        return (118, "优秀")
    elif 160 <= sannianji_nan_tiaosheng < 162:
        return (117, "优秀")
    elif 158 <= sannianji_nan_tiaosheng < 160:
        return (116, "优秀")
    elif 156 <= sannianji_nan_tiaosheng < 158:
        return (115, "优秀")
    elif 154 <= sannianji_nan_tiaosheng < 156:
        return (114, "优秀")
    elif 152 <= sannianji_nan_tiaosheng < 154:
        return (113, "优秀")
    elif 150 <= sannianji_nan_tiaosheng < 152:
        return (112, "优秀")
    elif 148 <= sannianji_nan_tiaosheng < 150:
        return (111, "优秀")
    elif 146 <= sannianji_nan_tiaosheng < 148:
        return (110, "优秀")
    elif 144 <= sannianji_nan_tiaosheng < 146:
        return (109, "优秀")
    elif 142 <= sannianji_nan_tiaosheng < 144:
        return (108, "优秀")
    elif 140 <= sannianji_nan_tiaosheng < 142:
        return (107, "优秀")
    elif 138 <= sannianji_nan_tiaosheng < 140:
        return (106, "优秀")
    elif 136 <= sannianji_nan_tiaosheng < 138:
        return (105, "优秀")
    elif 134 <= sannianji_nan_tiaosheng < 136:
        return (104, "优秀")
    elif 132 <= sannianji_nan_tiaosheng < 134:
        return (103, "优秀")
    elif 130 <= sannianji_nan_tiaosheng < 132:
        return (102, "优秀")
    elif 128 <= sannianji_nan_tiaosheng < 130:
        return (101, "优秀")
    elif 126 <= sannianji_nan_tiaosheng < 128:
        return (100, "优秀")
    elif 121 <= sannianji_nan_tiaosheng < 126:
        return (95, "优秀")
    elif 116 <= sannianji_nan_tiaosheng < 121:
        return (90, "优秀")
    elif 110 <= sannianji_nan_tiaosheng < 116:
        return (85, "良好")
    elif 104 <= sannianji_nan_tiaosheng < 110:
        return (80, "良好")
    elif 97 <= sannianji_nan_tiaosheng < 104:
        return (78, "及格")
    elif 90 <= sannianji_nan_tiaosheng < 97:
        return (76, "及格")
    elif 83 <= sannianji_nan_tiaosheng < 90:
        return (74, "及格")
    elif 76 <= sannianji_nan_tiaosheng < 83:
        return (72, "及格")
    elif 69 <= sannianji_nan_tiaosheng < 76:
        return (70, "及格")
    elif 62 <= sannianji_nan_tiaosheng < 69:
        return (68, "及格")
    elif 55 <= sannianji_nan_tiaosheng < 62:
        return (66, "及格")
    elif 48 <= sannianji_nan_tiaosheng < 55:
        return (64, "及格")
    elif 41 <= sannianji_nan_tiaosheng < 48:
        return (62, "及格")
    elif 34 <= sannianji_nan_tiaosheng < 41:
        return (60, "及格")
    elif 31 <= sannianji_nan_tiaosheng < 34:
        return (50, "不及格")
    elif 28 <= sannianji_nan_tiaosheng < 31:
        return (40, "不及格")
    elif 25 <= sannianji_nan_tiaosheng < 28:
        return (30, "不及格")
    elif 22 <= sannianji_nan_tiaosheng < 25:
        return (20, "不及格")
    elif 19 <= sannianji_nan_tiaosheng < 22:
        return (10, "不及格")
    elif 0 <= sannianji_nan_tiaosheng < 19:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{sannianji_nan_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{sannianji_nan_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{sannianji_nan_tiaosheng_jisuan_fenshu(100)}")  # 输出90


### 三年级女生跳绳标准
def sannianji_nv_tiaosheng_jisuan_fenshu(sannianji_nv_tiaosheng):
    # if isinstance(sannianji_nv_tiaosheng, float):
    #     return "女生跳绳请输入整数"
    # if not isinstance(sannianji_nv_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if sannianji_nv_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 179 <= sannianji_nv_tiaosheng < 500:
        return (120, "优秀")
    elif 177 <= sannianji_nv_tiaosheng < 179:
        return (119, "优秀")
    elif 175 <= sannianji_nv_tiaosheng < 177:
        return (118, "优秀")
    elif 173 <= sannianji_nv_tiaosheng < 175:
        return (117, "优秀")
    elif 171 <= sannianji_nv_tiaosheng < 173:
        return (116, "优秀")
    elif 169 <= sannianji_nv_tiaosheng < 171:
        return (115, "优秀")
    elif 167 <= sannianji_nv_tiaosheng < 169:
        return (114, "优秀")
    elif 165 <= sannianji_nv_tiaosheng < 167:
        return (113, "优秀")
    elif 163 <= sannianji_nv_tiaosheng < 165:
        return (112, "优秀")
    elif 161 <= sannianji_nv_tiaosheng < 163:
        return (111, "优秀")
    elif 159 <= sannianji_nv_tiaosheng < 161:
        return (110, "优秀")
    elif 157 <= sannianji_nv_tiaosheng < 159:
        return (109, "优秀")
    elif 155 <= sannianji_nv_tiaosheng < 157:
        return (108, "优秀")
    elif 153 <= sannianji_nv_tiaosheng < 155:
        return (107, "优秀")
    elif 151 <= sannianji_nv_tiaosheng < 153:
        return (106, "优秀")
    elif 149 <= sannianji_nv_tiaosheng < 151:
        return (105, "优秀")
    elif 147 <= sannianji_nv_tiaosheng < 149:
        return (104, "优秀")
    elif 145 <= sannianji_nv_tiaosheng < 147:
        return (103, "优秀")
    elif 143 <= sannianji_nv_tiaosheng < 145:
        return (102, "优秀")
    elif 141 <= sannianji_nv_tiaosheng < 143:
        return (101, "优秀")
    elif 139 <= sannianji_nv_tiaosheng < 141:
        return (100, "优秀")
    elif 132 <= sannianji_nv_tiaosheng < 139:
        return (95, "优秀")
    elif 125 <= sannianji_nv_tiaosheng < 132:
        return (90, "优秀")
    elif 117 <= sannianji_nv_tiaosheng < 125:
        return (85, "良好")
    elif 109 <= sannianji_nv_tiaosheng < 117:
        return (80, "良好")
    elif 102 <= sannianji_nv_tiaosheng < 109:
        return (78, "及格")
    elif 95 <= sannianji_nv_tiaosheng < 102:
        return (76, "及格")
    elif 88 <= sannianji_nv_tiaosheng < 95:
        return (74, "及格")
    elif 81 <= sannianji_nv_tiaosheng < 88:
        return (72, "及格")
    elif 74 <= sannianji_nv_tiaosheng < 81:
        return (70, "及格")
    elif 67 <= sannianji_nv_tiaosheng < 74:
        return (68, "及格")
    elif 60 <= sannianji_nv_tiaosheng < 67:
        return (66, "及格")
    elif 53 <= sannianji_nv_tiaosheng < 60:
        return (64, "及格")
    elif 46 <= sannianji_nv_tiaosheng < 53:
        return (62, "及格")
    elif 39 <= sannianji_nv_tiaosheng < 46:
        return (60, "及格")
    elif 36 <= sannianji_nv_tiaosheng < 39:
        return (50, "不及格")
    elif 33 <= sannianji_nv_tiaosheng < 36:
        return (40, "不及格")
    elif 30 <= sannianji_nv_tiaosheng < 33:
        return (30, "不及格")
    elif 27 <= sannianji_nv_tiaosheng < 30:
        return (20, "不及格")
    elif 24 <= sannianji_nv_tiaosheng < 27:
        return (10, "不及格")
    elif 0 <= sannianji_nv_tiaosheng < 24:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{sannianji_nv_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{sannianji_nv_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{sannianji_nv_tiaosheng_jisuan_fenshu(100)}")  # 输出90


### 四年级男生跳绳标准
def sinianji_nan_tiaosheng_jisuan_fenshu(sinianji_nan_tiaosheng):
    # if isinstance(sinianji_nan_tiaosheng, float):
    #     return "男生跳绳请输入整数"
    # if not isinstance(sinianji_nan_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if sinianji_nan_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 177 <= sinianji_nan_tiaosheng < 500:
        return (120, "优秀")
    elif 175 <= sinianji_nan_tiaosheng < 177:
        return (119, "优秀")
    elif 173 <= sinianji_nan_tiaosheng < 175:
        return (118, "优秀")
    elif 171 <= sinianji_nan_tiaosheng < 173:
        return (117, "优秀")
    elif 169 <= sinianji_nan_tiaosheng < 171:
        return (116, "优秀")
    elif 167 <= sinianji_nan_tiaosheng < 169:
        return (115, "优秀")
    elif 165 <= sinianji_nan_tiaosheng < 167:
        return (114, "优秀")
    elif 163 <= sinianji_nan_tiaosheng < 165:
        return (113, "优秀")
    elif 161 <= sinianji_nan_tiaosheng < 163:
        return (112, "优秀")
    elif 159 <= sinianji_nan_tiaosheng < 161:
        return (111, "优秀")
    elif 157 <= sinianji_nan_tiaosheng < 159:
        return (110, "优秀")
    elif 155 <= sinianji_nan_tiaosheng < 157:
        return (109, "优秀")
    elif 153 <= sinianji_nan_tiaosheng < 155:
        return (108, "优秀")
    elif 151 <= sinianji_nan_tiaosheng < 153:
        return (107, "优秀")
    elif 149 <= sinianji_nan_tiaosheng < 151:
        return (106, "优秀")
    elif 147 <= sinianji_nan_tiaosheng < 149:
        return (105, "优秀")
    elif 145 <= sinianji_nan_tiaosheng < 147:
        return (104, "优秀")
    elif 143 <= sinianji_nan_tiaosheng < 145:
        return (103, "优秀")
    elif 141 <= sinianji_nan_tiaosheng < 143:
        return (102, "优秀")
    elif 139 <= sinianji_nan_tiaosheng < 141:
        return (101, "优秀")
    elif 137 <= sinianji_nan_tiaosheng < 139:
        return (100, "优秀")
    elif 132 <= sinianji_nan_tiaosheng < 137:
        return (95, "优秀")
    elif 127 <= sinianji_nan_tiaosheng < 132:
        return (90, "优秀")
    elif 121 <= sinianji_nan_tiaosheng < 127:
        return (85, "良好")
    elif 115 <= sinianji_nan_tiaosheng < 121:
        return (80, "良好")
    elif 108 <= sinianji_nan_tiaosheng < 115:
        return (78, "及格")
    elif 101 <= sinianji_nan_tiaosheng < 108:
        return (76, "及格")
    elif 94 <= sinianji_nan_tiaosheng < 101:
        return (74, "及格")
    elif 87 <= sinianji_nan_tiaosheng < 94:
        return (72, "及格")
    elif 80 <= sinianji_nan_tiaosheng < 87:
        return (70, "及格")
    elif 73 <= sinianji_nan_tiaosheng < 80:
        return (68, "及格")
    elif 66 <= sinianji_nan_tiaosheng < 73:
        return (66, "及格")
    elif 59 <= sinianji_nan_tiaosheng < 66:
        return (64, "及格")
    elif 52 <= sinianji_nan_tiaosheng < 59:
        return (62, "及格")
    elif 45 <= sinianji_nan_tiaosheng < 52:
        return (60, "及格")
    elif 42 <= sinianji_nan_tiaosheng < 45:
        return (50, "不及格")
    elif 39 <= sinianji_nan_tiaosheng < 42:
        return (40, "不及格")
    elif 36 <= sinianji_nan_tiaosheng < 39:
        return (30, "不及格")
    elif 33 <= sinianji_nan_tiaosheng < 36:
        return (20, "不及格")
    elif 30 <= sinianji_nan_tiaosheng < 33:
        return (10, "不及格")
    elif 0 <= sinianji_nan_tiaosheng < 30:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{sinianji_nan_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{sinianji_nan_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{sinianji_nan_tiaosheng_jisuan_fenshu(100)}")  # 输出90


### 四年级女生跳绳标准
def sinianji_nv_tiaosheng_jisuan_fenshu(sinianji_nv_tiaosheng):
    # if isinstance(sinianji_nv_tiaosheng, float):
    #     return "女生跳绳请输入整数"
    # if not isinstance(sinianji_nv_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if sinianji_nv_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 189 <= sinianji_nv_tiaosheng < 500:
        return (120, "优秀")
    elif 187 <= sinianji_nv_tiaosheng < 189:
        return (119, "优秀")
    elif 185 <= sinianji_nv_tiaosheng < 187:
        return (118, "优秀")
    elif 183 <= sinianji_nv_tiaosheng < 185:
        return (117, "优秀")
    elif 181 <= sinianji_nv_tiaosheng < 183:
        return (116, "优秀")
    elif 179 <= sinianji_nv_tiaosheng < 181:
        return (115, "优秀")
    elif 177 <= sinianji_nv_tiaosheng < 179:
        return (114, "优秀")
    elif 175 <= sinianji_nv_tiaosheng < 177:
        return (113, "优秀")
    elif 173 <= sinianji_nv_tiaosheng < 175:
        return (112, "优秀")
    elif 171 <= sinianji_nv_tiaosheng < 173:
        return (111, "优秀")
    elif 169 <= sinianji_nv_tiaosheng < 171:
        return (110, "优秀")
    elif 167 <= sinianji_nv_tiaosheng < 169:
        return (109, "优秀")
    elif 165 <= sinianji_nv_tiaosheng < 167:
        return (108, "优秀")
    elif 163 <= sinianji_nv_tiaosheng < 165:
        return (107, "优秀")
    elif 161 <= sinianji_nv_tiaosheng < 163:
        return (106, "优秀")
    elif 159 <= sinianji_nv_tiaosheng < 161:
        return (105, "优秀")
    elif 157 <= sinianji_nv_tiaosheng < 159:
        return (104, "优秀")
    elif 155 <= sinianji_nv_tiaosheng < 157:
        return (103, "优秀")
    elif 153 <= sinianji_nv_tiaosheng < 155:
        return (102, "优秀")
    elif 151 <= sinianji_nv_tiaosheng < 153:
        return (101, "优秀")
    elif 149 <= sinianji_nv_tiaosheng < 151:
        return (100, "优秀")
    elif 142 <= sinianji_nv_tiaosheng < 149:
        return (95, "优秀")
    elif 135 <= sinianji_nv_tiaosheng < 142:
        return (90, "优秀")
    elif 127 <= sinianji_nv_tiaosheng < 135:
        return (85, "良好")
    elif 119 <= sinianji_nv_tiaosheng < 127:
        return (80, "良好")
    elif 112 <= sinianji_nv_tiaosheng < 119:
        return (78, "及格")
    elif 105 <= sinianji_nv_tiaosheng < 112:
        return (76, "及格")
    elif 98 <= sinianji_nv_tiaosheng < 105:
        return (74, "及格")
    elif 91 <= sinianji_nv_tiaosheng < 98:
        return (72, "及格")
    elif 84 <= sinianji_nv_tiaosheng < 91:
        return (70, "及格")
    elif 77 <= sinianji_nv_tiaosheng < 84:
        return (68, "及格")
    elif 70 <= sinianji_nv_tiaosheng < 77:
        return (66, "及格")
    elif 63 <= sinianji_nv_tiaosheng < 70:
        return (64, "及格")
    elif 56 <= sinianji_nv_tiaosheng < 63:
        return (62, "及格")
    elif 49 <= sinianji_nv_tiaosheng < 56:
        return (60, "及格")
    elif 46 <= sinianji_nv_tiaosheng < 49:
        return (50, "不及格")
    elif 43 <= sinianji_nv_tiaosheng < 46:
        return (40, "不及格")
    elif 40 <= sinianji_nv_tiaosheng < 43:
        return (30, "不及格")
    elif 37 <= sinianji_nv_tiaosheng < 40:
        return (20, "不及格")
    elif 34 <= sinianji_nv_tiaosheng < 37:
        return (10, "不及格")
    elif 0 <= sinianji_nv_tiaosheng < 34:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{sinianji_nv_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{sinianji_nv_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{sinianji_nv_tiaosheng_jisuan_fenshu(100)}")  # 输出90


### 五年级男生跳绳得分计算函数
def wunianji_nan_tiaosheng_jisuan_fenshu(wunianji_nan_tiaosheng):
    # if isinstance(wunianji_nan_tiaosheng, float):
    #     return "男生跳绳请输入整数"
    # if not isinstance(wunianji_nan_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if wunianji_nan_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 188 <= wunianji_nan_tiaosheng < 500:
        return (120, "优秀")
    elif 186 <= wunianji_nan_tiaosheng < 188:
        return (119, "优秀")
    elif 184 <= wunianji_nan_tiaosheng < 186:
        return (118, "优秀")
    elif 182 <= wunianji_nan_tiaosheng < 184:
        return (117, "优秀")
    elif 180 <= wunianji_nan_tiaosheng < 182:
        return (116, "优秀")
    elif 178 <= wunianji_nan_tiaosheng < 180:
        return (115, "优秀")
    elif 176 <= wunianji_nan_tiaosheng < 178:
        return (114, "优秀")
    elif 174 <= wunianji_nan_tiaosheng < 176:
        return (113, "优秀")
    elif 172 <= wunianji_nan_tiaosheng < 174:
        return (112, "优秀")
    elif 170 <= wunianji_nan_tiaosheng < 172:
        return (111, "优秀")
    elif 168 <= wunianji_nan_tiaosheng < 170:
        return (110, "优秀")
    elif 166 <= wunianji_nan_tiaosheng < 168:
        return (109, "优秀")
    elif 164 <= wunianji_nan_tiaosheng < 166:
        return (108, "优秀")
    elif 162 <= wunianji_nan_tiaosheng < 164:
        return (107, "优秀")
    elif 160 <= wunianji_nan_tiaosheng < 162:
        return (106, "优秀")
    elif 158 <= wunianji_nan_tiaosheng < 160:
        return (105, "优秀")
    elif 156 <= wunianji_nan_tiaosheng < 158:
        return (104, "优秀")
    elif 154 <= wunianji_nan_tiaosheng < 156:
        return (103, "优秀")
    elif 152 <= wunianji_nan_tiaosheng < 154:
        return (102, "优秀")
    elif 150 <= wunianji_nan_tiaosheng < 152:
        return (101, "优秀")
    elif 148 <= wunianji_nan_tiaosheng < 150:
        return (100, "优秀")
    elif 143 <= wunianji_nan_tiaosheng < 148:
        return (95, "优秀")
    elif 138 <= wunianji_nan_tiaosheng < 143:
        return (90, "优秀")
    elif 132 <= wunianji_nan_tiaosheng < 138:
        return (85, "良好")
    elif 126 <= wunianji_nan_tiaosheng < 132:
        return (80, "良好")
    elif 119 <= wunianji_nan_tiaosheng < 126:
        return (78, "及格")
    elif 112 <= wunianji_nan_tiaosheng < 119:
        return (76, "及格")
    elif 105 <= wunianji_nan_tiaosheng < 112:
        return (74, "及格")
    elif 98 <= wunianji_nan_tiaosheng < 105:
        return (72, "及格")
    elif 91 <= wunianji_nan_tiaosheng < 98:
        return (70, "及格")
    elif 84 <= wunianji_nan_tiaosheng < 91:
        return (68, "及格")
    elif 77 <= wunianji_nan_tiaosheng < 84:
        return (66, "及格")
    elif 70 <= wunianji_nan_tiaosheng < 77:
        return (64, "及格")
    elif 63 <= wunianji_nan_tiaosheng < 70:
        return (62, "及格")
    elif 56 <= wunianji_nan_tiaosheng < 63:
        return (60, "及格")
    elif 53 <= wunianji_nan_tiaosheng < 56:
        return (50, "不及格")
    elif 50 <= wunianji_nan_tiaosheng < 53:
        return (40, "不及格")
    elif 47 <= wunianji_nan_tiaosheng < 50:
        return (30, "不及格")
    elif 44 <= wunianji_nan_tiaosheng < 47:
        return (20, "不及格")
    elif 41 <= wunianji_nan_tiaosheng < 44:
        return (10, "不及格")
    elif 0 <= wunianji_nan_tiaosheng < 41:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{wunianji_nan_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{wunianji_nan_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{wunianji_nan_tiaosheng_jisuan_fenshu(100)}")  # 输出90




### 五年级女生跳绳得分计算函数
def wunianji_nv_tiaosheng_jisuan_fenshu(wunianji_nv_tiaosheng):
    # if isinstance(wunianji_nv_tiaosheng, float):
    #     return "女生跳绳请输入整数"
    # if not isinstance(wunianji_nv_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if wunianji_nv_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 198 <= wunianji_nv_tiaosheng < 500:
        return (120, "优秀")
    elif 196 <= wunianji_nv_tiaosheng < 198:
        return (119, "优秀")
    elif 194 <= wunianji_nv_tiaosheng < 196:
        return (118, "优秀")
    elif 192 <= wunianji_nv_tiaosheng < 194:
        return (117, "优秀")
    elif 190 <= wunianji_nv_tiaosheng < 192:
        return (116, "优秀")
    elif 188 <= wunianji_nv_tiaosheng < 190:
        return (115, "优秀")
    elif 186 <= wunianji_nv_tiaosheng < 188:
        return (114, "优秀")
    elif 184 <= wunianji_nv_tiaosheng < 186:
        return (113, "优秀")
    elif 182 <= wunianji_nv_tiaosheng < 184:
        return (112, "优秀")
    elif 180 <= wunianji_nv_tiaosheng < 182:
        return (111, "优秀")
    elif 178 <= wunianji_nv_tiaosheng < 180:
        return (110, "优秀")
    elif 176 <= wunianji_nv_tiaosheng < 178:
        return (109, "优秀")
    elif 174 <= wunianji_nv_tiaosheng < 176:
        return (108, "优秀")
    elif 172 <= wunianji_nv_tiaosheng < 174:
        return (107, "优秀")
    elif 170 <= wunianji_nv_tiaosheng < 172:
        return (106, "优秀")
    elif 168 <= wunianji_nv_tiaosheng < 170:
        return (105, "优秀")
    elif 166 <= wunianji_nv_tiaosheng < 168:
        return (104, "优秀")
    elif 164 <= wunianji_nv_tiaosheng < 166:
        return (103, "优秀")
    elif 162 <= wunianji_nv_tiaosheng < 164:
        return (102, "优秀")
    elif 160 <= wunianji_nv_tiaosheng < 162:
        return (101, "优秀")
    elif 158 <= wunianji_nv_tiaosheng < 160:
        return (100, "优秀")
    elif 151 <= wunianji_nv_tiaosheng < 158:
        return (95, "优秀")
    elif 144 <= wunianji_nv_tiaosheng < 151:
        return (90, "优秀")
    elif 136 <= wunianji_nv_tiaosheng < 144:
        return (85, "良好")
    elif 128 <= wunianji_nv_tiaosheng < 136:
        return (80, "良好")
    elif 121 <= wunianji_nv_tiaosheng < 128:
        return (78, "及格")
    elif 114 <= wunianji_nv_tiaosheng < 121:
        return (76, "及格")
    elif 107 <= wunianji_nv_tiaosheng < 114:
        return (74, "及格")
    elif 100 <= wunianji_nv_tiaosheng < 107:
        return (72, "及格")
    elif 93 <= wunianji_nv_tiaosheng < 100:
        return (70, "及格")
    elif 86 <= wunianji_nv_tiaosheng < 93:
        return (68, "及格")
    elif 79 <= wunianji_nv_tiaosheng < 86:
        return (66, "及格")
    elif 72 <= wunianji_nv_tiaosheng < 79:
        return (64, "及格")
    elif 65 <= wunianji_nv_tiaosheng < 72:
        return (62, "及格")
    elif 58 <= wunianji_nv_tiaosheng < 65:
        return (60, "及格")
    elif 55 <= wunianji_nv_tiaosheng < 58:
        return (50, "不及格")
    elif 52 <= wunianji_nv_tiaosheng < 55:
        return (40, "不及格")
    elif 49 <= wunianji_nv_tiaosheng < 52:
        return (30, "不及格")
    elif 46 <= wunianji_nv_tiaosheng < 49:
        return (20, "不及格")
    elif 43 <= wunianji_nv_tiaosheng < 46:
        return (10, "不及格")
    elif 0 <= wunianji_nv_tiaosheng < 43:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{wunianji_nv_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{wunianji_nv_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{wunianji_nv_tiaosheng_jisuan_fenshu(100)}")  # 输出90





### 六年级男生跳绳得分计算函数
def liunianji_nan_tiaosheng_jisuan_fenshu(liunianji_nan_tiaosheng):
    # if isinstance(liunianji_nan_tiaosheng, float):
    #     return "男生跳绳请输入整数"
    # if not isinstance(liunianji_nan_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")

    if liunianji_nan_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 197 <= liunianji_nan_tiaosheng < 500:
        return (120, "优秀")
    elif 195 <= liunianji_nan_tiaosheng < 197:
        return (119, "优秀")
    elif 193 <= liunianji_nan_tiaosheng < 195:
        return (118, "优秀")
    elif 191 <= liunianji_nan_tiaosheng < 193:
        return (117, "优秀")
    elif 189 <= liunianji_nan_tiaosheng < 191:
        return (116, "优秀")
    elif 187 <= liunianji_nan_tiaosheng < 189:
        return (115, "优秀")
    elif 185 <= liunianji_nan_tiaosheng < 187:
        return (114, "优秀")
    elif 183 <= liunianji_nan_tiaosheng < 185:
        return (113, "优秀")
    elif 181 <= liunianji_nan_tiaosheng < 183:
        return (112, "优秀")
    elif 179 <= liunianji_nan_tiaosheng < 181:
        return (111, "优秀")
    elif 177 <= liunianji_nan_tiaosheng < 179:
        return (110, "优秀")
    elif 175 <= liunianji_nan_tiaosheng < 177:
        return (109, "优秀")
    elif 173 <= liunianji_nan_tiaosheng < 175:
        return (108, "优秀")
    elif 171 <= liunianji_nan_tiaosheng < 173:
        return (107, "优秀")
    elif 169 <= liunianji_nan_tiaosheng < 171:
        return (106, "优秀")
    elif 167 <= liunianji_nan_tiaosheng < 169:
        return (105, "优秀")
    elif 165 <= liunianji_nan_tiaosheng < 167:
        return (104, "优秀")
    elif 163 <= liunianji_nan_tiaosheng < 165:
        return (103, "优秀")
    elif 161 <= liunianji_nan_tiaosheng < 163:
        return (102, "优秀")
    elif 159 <= liunianji_nan_tiaosheng < 161:
        return (101, "优秀")
    elif 157 <= liunianji_nan_tiaosheng < 159:
        return (100, "优秀")
    elif 152 <= liunianji_nan_tiaosheng < 157:
        return (95, "优秀")
    elif 147 <= liunianji_nan_tiaosheng < 152:
        return (90, "优秀")
    elif 141 <= liunianji_nan_tiaosheng < 147:
        return (85, "良好")
    elif 135 <= liunianji_nan_tiaosheng < 141:
        return (80, "良好")
    elif 128 <= liunianji_nan_tiaosheng < 135:
        return (78, "及格")
    elif 121 <= liunianji_nan_tiaosheng < 128:
        return (76, "及格")
    elif 114 <= liunianji_nan_tiaosheng < 121:
        return (74, "及格")
    elif 107 <= liunianji_nan_tiaosheng < 114:
        return (72, "及格")
    elif 100 <= liunianji_nan_tiaosheng < 107:
        return (70, "及格")
    elif 93 <= liunianji_nan_tiaosheng < 100:
        return (68, "及格")
    elif 86 <= liunianji_nan_tiaosheng < 93:
        return (66, "及格")
    elif 79 <= liunianji_nan_tiaosheng < 86:
        return (64, "及格")
    elif 72 <= liunianji_nan_tiaosheng < 79:
        return (62, "及格")
    elif 65 <= liunianji_nan_tiaosheng < 72:
        return (60, "及格")
    elif 62 <= liunianji_nan_tiaosheng < 65:
        return (50, "不及格")
    elif 59 <= liunianji_nan_tiaosheng < 62:
        return (40, "不及格")
    elif 56 <= liunianji_nan_tiaosheng < 59:
        return (30, "不及格")
    elif 53 <= liunianji_nan_tiaosheng < 56:
        return (20, "不及格")
    elif 50 <= liunianji_nan_tiaosheng < 53:
        return (10, "不及格")
    elif 0 <= liunianji_nan_tiaosheng < 50:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{liunianji_nan_tiaosheng_jisuan_fenshu(150)[0]}")  # 输出100
    print(f"150个跳绳得分：{liunianji_nan_tiaosheng_jisuan_fenshu(150)[1]}")  # 输出100
    print(f"100个跳绳得分：{liunianji_nan_tiaosheng_jisuan_fenshu(100)}")  # 输出90


def liunianji_nv_tiaosheng_jisuan_fenshu(liunianji_nv_tiaosheng):
    # if isinstance(liunianji_nv_tiaosheng, float):
    #     return "女生跳绳请输入整数"
    # if not isinstance(liunianji_nv_tiaosheng, (int, float)):
    #     return ValueError("请传入有效的数字类型跳绳数值（单位：个）")
    if liunianji_nv_tiaosheng >= 500:
        return ("太大", "超出500个，请检查")
    elif 206 <= liunianji_nv_tiaosheng < 500:
        return (120, "优秀")
    elif 204 <= liunianji_nv_tiaosheng < 206:
        return (119, "优秀")
    elif 202 <= liunianji_nv_tiaosheng < 204:
        return (118, "优秀")
    elif 200 <= liunianji_nv_tiaosheng < 202:
        return (117, "优秀")
    elif 198 <= liunianji_nv_tiaosheng < 200:
        return (116, "优秀")
    elif 196 <= liunianji_nv_tiaosheng < 198:
        return (115, "优秀")
    elif 194 <= liunianji_nv_tiaosheng < 196:
        return (114, "优秀")
    elif 192 <= liunianji_nv_tiaosheng < 194:
        return (113, "优秀")
    elif 190 <= liunianji_nv_tiaosheng < 192:
        return (112, "优秀")
    elif 188 <= liunianji_nv_tiaosheng < 190:
        return (111, "优秀")
    elif 186 <= liunianji_nv_tiaosheng < 188:
        return (110, "优秀")
    elif 184 <= liunianji_nv_tiaosheng < 186:
        return (109, "优秀")
    elif 182 <= liunianji_nv_tiaosheng < 184:
        return (108, "优秀")
    elif 180 <= liunianji_nv_tiaosheng < 182:
        return (107, "优秀")
    elif 178 <= liunianji_nv_tiaosheng < 180:
        return (106, "优秀")
    elif 176 <= liunianji_nv_tiaosheng < 178:
        return (105, "优秀")
    elif 174 <= liunianji_nv_tiaosheng < 176:
        return (104, "优秀")
    elif 172 <= liunianji_nv_tiaosheng < 174:
        return (103, "优秀")
    elif 170 <= liunianji_nv_tiaosheng < 172:
        return (102, "优秀")
    elif 168 <= liunianji_nv_tiaosheng < 170:
        return (101, "优秀")
    elif 166 <= liunianji_nv_tiaosheng < 168:
        return (100, "优秀")
    elif 159 <= liunianji_nv_tiaosheng < 166:
        return (95, "优秀")
    elif 152 <= liunianji_nv_tiaosheng < 159:
        return (90, "优秀")
    elif 144 <= liunianji_nv_tiaosheng < 152:
        return (85, "良好")
    elif 136 <= liunianji_nv_tiaosheng < 144:
        return (80, "良好")
    elif 129 <= liunianji_nv_tiaosheng < 136:
        return (78, "及格")
    elif 122 <= liunianji_nv_tiaosheng < 129:
        return (76, "及格")
    elif 115 <= liunianji_nv_tiaosheng < 122:
        return (74, "及格")
    elif 108 <= liunianji_nv_tiaosheng < 115:
        return (72, "及格")
    elif 101 <= liunianji_nv_tiaosheng < 108:
        return (70, "及格")
    elif 94 <= liunianji_nv_tiaosheng < 101:
        return (68, "及格")
    elif 87 <= liunianji_nv_tiaosheng < 94:
        return (66, "及格")
    elif 80 <= liunianji_nv_tiaosheng < 87:
        return (64, "及格")
    elif 73 <= liunianji_nv_tiaosheng < 80:
        return (62, "及格")
    elif 66 <= liunianji_nv_tiaosheng < 73:
        return (60, "及格")
    elif 63 <= liunianji_nv_tiaosheng < 66:
        return (50, "不及格")
    elif 60 <= liunianji_nv_tiaosheng < 63:
        return (40, "不及格")
    elif 57 <= liunianji_nv_tiaosheng < 60:
        return (30, "不及格")
    elif 54 <= liunianji_nv_tiaosheng < 57:
        return (20, "不及格")
    elif 51 <= liunianji_nv_tiaosheng < 54:
        return (10, "不及格")
    elif 0 <= liunianji_nv_tiaosheng < 51:
        return (0, "不及格")
    else:
        return "低于0个跳绳，请检查"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print(f"150个跳绳得分：{liunianji_nv_tiaosheng_jisuan_fenshu(150)[0]}")
    print(f"150个跳绳得分：{liunianji_nv_tiaosheng_jisuan_fenshu(150)[1]}")
    print(f"100个跳绳得分：{liunianji_nv_tiaosheng_jisuan_fenshu(100)}")



