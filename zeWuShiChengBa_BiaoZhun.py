
###五年级   50*8    男
def wunianji_nan_wushichengba_jisuan_fenshu(wunianji_nan_wushichengba):
    if wunianji_nan_wushichengba < 60:
        return ("太大", "低于60秒，请检查")
    elif 60 <= wunianji_nan_wushichengba < 99:
        return (100, "优秀")
    elif 99 <= wunianji_nan_wushichengba < 102:
        return (95, "优秀")
    elif 102 <= wunianji_nan_wushichengba < 105:
        return (90, "优秀")
    elif 105 <= wunianji_nan_wushichengba < 108:
        return (85, "良好")
    elif 108 <= wunianji_nan_wushichengba < 111:
        return (80, "良好")
    elif 111 <= wunianji_nan_wushichengba < 114:
        return (78, "及格")
    elif 114 <= wunianji_nan_wushichengba < 117:
        return (76, "及格")
    elif 117 <= wunianji_nan_wushichengba < 120:
        return (74, "及格")
    elif 120 <= wunianji_nan_wushichengba < 123:
        return (72, "及格")
    elif 123 <= wunianji_nan_wushichengba < 126:
        return (70, "及格")
    elif 126 <= wunianji_nan_wushichengba < 129:
        return (68, "及格")
    elif 129 <= wunianji_nan_wushichengba < 132:
        return (66, "及格")
    elif 132 <= wunianji_nan_wushichengba < 135:
        return (64, "及格")
    elif 135 <= wunianji_nan_wushichengba < 138:
        return (62, "及格")
    elif 138 <= wunianji_nan_wushichengba < 142:
        return (60, "及格")
    elif 142 <= wunianji_nan_wushichengba < 146:
        return (50, "不及格")
    elif 146 <= wunianji_nan_wushichengba < 150:
        return (40, "不及格")
    elif 150 <= wunianji_nan_wushichengba < 154:
        return (30, "不及格")
    elif 154 <= wunianji_nan_wushichengba < 158:
        return (20, "不及格")
    elif 158 <= wunianji_nan_wushichengba < 240:
        return (10, "不及格")
    elif 240 <= wunianji_nan_wushichengba:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50*8数值（单位：分钟‘ 秒“）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    result = wunianji_nan_wushichengba_jisuan_fenshu(90)
    print("1'30\"得分", result[0], result[1])


###五年级   50*8    女

def wunianji_nv_wushichengba_jisuan_fenshu(wunianji_nv_wushichengba):
    if wunianji_nv_wushichengba < 60:
        return ("太大", "低于60秒，请检查")
    elif 60 <= wunianji_nv_wushichengba < 104:
        return (100, "优秀")
    elif 104 <= wunianji_nv_wushichengba < 107:
        return (95, "优秀")
    elif 107 <= wunianji_nv_wushichengba < 110:
        return (90, "优秀")
    elif 110 <= wunianji_nv_wushichengba < 113:
        return (85, "良好")
    elif 113 <= wunianji_nv_wushichengba < 116:
        return (80, "良好")
    elif 116 <= wunianji_nv_wushichengba < 119:
        return (78, "及格")
    elif 119 <= wunianji_nv_wushichengba < 122:
        return (76, "及格")
    elif 122 <= wunianji_nv_wushichengba < 125:
        return (74, "及格")
    elif 125 <= wunianji_nv_wushichengba < 128:
        return (72, "及格")
    elif 128 <= wunianji_nv_wushichengba < 131:
        return (70, "及格")
    elif 131 <= wunianji_nv_wushichengba < 134:
        return (68, "及格")
    elif 134 <= wunianji_nv_wushichengba < 137:
        return (66, "及格")
    elif 137 <= wunianji_nv_wushichengba < 140:
        return (64, "及格")
    elif 140 <= wunianji_nv_wushichengba < 143:
        return (62, "及格")
    elif 143 <= wunianji_nv_wushichengba < 147:
        return (60, "及格")
    elif 147 <= wunianji_nv_wushichengba < 151:
        return (50, "不及格")
    elif 151 <= wunianji_nv_wushichengba < 155:
        return (40, "不及格")
    elif 155 <= wunianji_nv_wushichengba < 159:
        return (30, "不及格")
    elif 159 <= wunianji_nv_wushichengba < 163:
        return (20, "不及格")
    elif 163 <= wunianji_nv_wushichengba < 240:
        return (10, "不及格")
    elif 240 <= wunianji_nv_wushichengba:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50*8数值（单位：分钟‘ 秒“）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("1'30\"得分", wunianji_nv_wushichengba_jisuan_fenshu(90)[0], wunianji_nv_wushichengba_jisuan_fenshu(90)[1])




###六年级    50*8    男
def liunianji_nan_wushichengba_jisuan_fenshu(liunianji_nan_wushichengba):
    if liunianji_nan_wushichengba < 60:
        return ("太大", "低于60秒，请检查")
    elif 60 <= liunianji_nan_wushichengba < 93:
        return (100, "优秀")
    elif 93 <= liunianji_nan_wushichengba < 96:
        return (95, "优秀")
    elif 96 <= liunianji_nan_wushichengba < 99:
        return (90, "优秀")
    elif 99 <= liunianji_nan_wushichengba < 102:
        return (85, "良好")
    elif 102 <= liunianji_nan_wushichengba < 105:
        return (80, "良好")
    elif 105 <= liunianji_nan_wushichengba < 108:
        return (78, "及格")
    elif 108 <= liunianji_nan_wushichengba < 111:
        return (76, "及格")
    elif 111 <= liunianji_nan_wushichengba < 114:
        return (74, "及格")
    elif 114 <= liunianji_nan_wushichengba < 117:
        return (72, "及格")
    elif 117 <= liunianji_nan_wushichengba < 120:
        return (70, "及格")
    elif 120 <= liunianji_nan_wushichengba < 123:
        return (68, "及格")
    elif 123 <= liunianji_nan_wushichengba < 126:
        return (66, "及格")
    elif 126 <= liunianji_nan_wushichengba < 129:
        return (64, "及格")
    elif 129 <= liunianji_nan_wushichengba < 132:
        return (62, "及格")
    elif 132 <= liunianji_nan_wushichengba < 136:
        return (60, "及格")
    elif 136 <= liunianji_nan_wushichengba < 140:
        return (50, "不及格")
    elif 140 <= liunianji_nan_wushichengba < 144:
        return (40, "不及格")
    elif 144 <= liunianji_nan_wushichengba < 148:
        return (30, "不及格")
    elif 148 <= liunianji_nan_wushichengba < 152:
        return (20, "不及格")
    elif 152 <= liunianji_nan_wushichengba < 240:
        return (10, "不及格")
    elif 240 <= liunianji_nan_wushichengba:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50*8数值（单位：分钟‘ 秒“）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("1'30\"得分", liunianji_nan_wushichengba_jisuan_fenshu(90)[0], liunianji_nan_wushichengba_jisuan_fenshu(90)[1])



###六年级    50*8    女
def liunianji_nv_wushichengba_jisuan_fenshu(liunianji_nv_wushichengba):
    if liunianji_nv_wushichengba < 60:
        return ("太大", "低于60秒，请检查")
    elif 60 <= liunianji_nv_wushichengba < 100:
        return (100, "优秀")
    elif 100 <= liunianji_nv_wushichengba < 103:
        return (95, "优秀")
    elif 103 <= liunianji_nv_wushichengba < 106:
        return (90, "优秀")
    elif 106 <= liunianji_nv_wushichengba < 109:
        return (85, "良好")
    elif 109 <= liunianji_nv_wushichengba < 112:
        return (80, "良好")
    elif 112 <= liunianji_nv_wushichengba < 115:
        return (78, "及格")
    elif 115 <= liunianji_nv_wushichengba < 118:
        return (76, "及格")
    elif 118 <= liunianji_nv_wushichengba < 121:
        return (74, "及格")
    elif 121 <= liunianji_nv_wushichengba < 124:
        return (72, "及格")
    elif 124 <= liunianji_nv_wushichengba < 127:
        return (70, "及格")
    elif 127 <= liunianji_nv_wushichengba < 130:
        return (68, "及格")
    elif 130 <= liunianji_nv_wushichengba < 133:
        return (66, "及格")
    elif 133 <= liunianji_nv_wushichengba < 136:
        return (64, "及格")
    elif 136 <= liunianji_nv_wushichengba < 139:
        return (62, "及格")
    elif 139 <= liunianji_nv_wushichengba < 143:
        return (60, "及格")
    elif 143 <= liunianji_nv_wushichengba < 147:
        return (50, "不及格")
    elif 147 <= liunianji_nv_wushichengba < 151:
        return (40, "不及格")
    elif 151 <= liunianji_nv_wushichengba < 155:
        return (30, "不及格")
    elif 155 <= liunianji_nv_wushichengba < 159:
        return (20, "不及格")
    elif 159 <= liunianji_nv_wushichengba < 240:
        return (10, "不及格")
    elif 240 <= liunianji_nv_wushichengba:
        return (0, "不及格")
    else:
        return "请传入有效的数字类型50*8数值（单位：分钟‘ 秒“）"


# 直接运行此文件时执行
if __name__ == "__main__":
    print("直接运行 触发：")
    print("1'30\"得分", liunianji_nv_wushichengba_jisuan_fenshu(90)[0], liunianji_nv_wushichengba_jisuan_fenshu(90)[1])


