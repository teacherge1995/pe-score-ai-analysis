import re
from datetime import timedelta

def ZongMiaoShu(time_str):
    # 使用正则表达式提取分和秒的数值
    match = re.match(r'(\d+)\'(\d*)', time_str)
    if not match:
        raise ValueError("格式错误，请使用 '分'秒' 格式（如 2'23''）")

    # 提取分组中的数值（分和秒）
    minutes = int(match.group(1))
    sec_str = match.group(2)
    if sec_str:
        seconds = int(sec_str)
    else:
        seconds = 0



    # 转换为总秒数
    All_seconds = minutes * 60 + seconds

    return All_seconds


# 测试
if __name__ == "__main__":
    time_str = "2'70"

#min 变量将接收函数返回值序列中的第一个值，通常代表解析出的分钟数。
#sec 变量接收第二个值，代表解析出的秒数。
#total_sec 接收第三个值，可能是将分钟和秒换算成的总秒数。
#time_obj 接收第四个值，可能是一个代表该时间的 datetime.timedelta 对象或其他时间相关对象。


#print(f"{min}分{sec}秒")  # 输出：2分23秒
    print(f"总秒数：{ZongMiaoShu(time_str)}秒")  # 输出：总秒数：143秒
