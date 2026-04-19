from zgFeiHuoLiang_BiaoZhun import  ernianji_nan_feihuoliang_jisuan_fenshu, ernianji_nv_feihuoliang_jisuan_fenshu
from zbTiaoSheng_BiaoZhun import   ernianji_nan_tiaosheng_jisuan_fenshu, ernianji_nv_tiaosheng_jisuan_fenshu
from zcZuoWeiTiQianQu_BiaoZhun import  ernianji_nan_zuoweitiqianqu_jisuan_fenshu, ernianji_nv_zuoweitiqianqu_jisuan_fenshu
from zaWuShiMi_BiaoZhun import  ernianji_nan_wushimi_jisuan_fenshu, ernianji_nv_wushimi_jisuan_fenshu
from zZuiHouDengJi_BiaoZhun import zuihoudengji_panduan,zuihoudengji80_panduan,zuihoudengji65_panduan
from zfJiaCeXiangMu_BiaoZhun import 二年级男生仰卧起坐计算分数,二年级女生仰卧起坐计算分数
from zhBMI_BiaoZhun import 二年级男生体重指数计算分数,二年级女生体重指数计算分数
import random



# 全体男生列表
def JiSuan_nan_list(data_list, wenjianming):
    suoyou_nan = []  # 全体男生  无排名
    special_count = 0  # 新增：统计【特殊】同学数量

    for row in data_list:
        try:
            # 获取索引2的性别值，去除空格并转字符串（兼容各种格式）
            gender = str(row[2]).strip()

            # ====================== 新增：特殊判断 ======================
            if gender in ["特殊男"]:
                special_count += 1  # 每遇到一个特殊，计数+1

                # 特殊：所有成绩、分数、等级全部设为 0
                xuhao = row[0]
                xingming = row[1]
                xingbie = gender
                banji = wenjianming

                # 特殊固定数据（全部 0）
                boy_list = [
                    xuhao, xingming, xingbie,
                    0, 0, "特殊",  # 50米：成绩、分数、等级
                    0, 0, 0, "特殊",  # 跳绳：成绩、分数、加分、等级
                    0, 0, "特殊",  # 坐位体前屈：成绩、分数、等级
                    0, 0, "特殊",  # 三项：总分、平均分、等级
                    0, 0, "特殊",  # 仰卧起坐：成绩、分数、等级
                    0, 0, "特殊",  # 四项：总分、平均分、等级
                    0, 0, "特殊",  # 肺活量：成绩、分数、等级
                    0, 0, 0, 0, "特殊",  # 身高、体重、BMI、BMI分数、BMI等级
                    0, 0, "特殊",  # 六项：总分、平均分、等级
                    banji
                ]
                suoyou_nan.append(boy_list)
                continue  # 跳过后续计算，直接处理下一行

            # ====================== 原有男生判断逻辑 ======================
            if gender in ['男', '男生']:
                Bmi = round((float(row[9])) / (((float(row[8])) / 100) * ((int(float(row[8]))) / 100)), 1)

                wushimi_func = ernianji_nan_wushimi_jisuan_fenshu
                tiaosheng_func = ernianji_nan_tiaosheng_jisuan_fenshu
                zuoweitiqianqu_func = ernianji_nan_zuoweitiqianqu_jisuan_fenshu
                yangwoqizuo_func = 二年级男生仰卧起坐计算分数
                feihuoliang_func = ernianji_nan_feihuoliang_jisuan_fenshu
                Bmi_func = 二年级男生体重指数计算分数(Bmi)
                xuhao = row[0]
                xingming = row[1]
                xingbie = row[2]
                banji = wenjianming

                # ====================== 50米 ======================
                try:
                    wushimichengji = float(row[3])
                    wushimi_defen = wushimi_func(float(row[3]))[0]
                    wushimi_dengji = wushimi_func(float(row[3]))[1]

                except Exception as e:
                    raise Exception(f"【50米项目计算错误】男生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # ====================== 跳绳 ======================
                try:
                    tiaosheng_str = str(row[4]).strip()

                    # 只要包含小数点，直接判定为非法成绩
                    if "." in tiaosheng_str:
                        raise ValueError(f"跳绳成绩不能为小数，必须是整数，男生姓名：{xingming}，序号：{xuhao}")

                    # 转换为整数
                    tiaoshengchengji = int(tiaosheng_str)

                    tiaosheng_defen = tiaosheng_func(tiaoshengchengji)[0]
                    tiaosheng_dengji = tiaosheng_func(tiaoshengchengji)[1]
                    tiaosheng_jiafen = tiaosheng_defen - 100 if tiaosheng_defen > 100 else 0

                except Exception as e:
                    raise Exception(f"【跳绳项目计算错误】男生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")
                # ====================== 坐位体前屈 ======================
                try:
                    zuoweitiqianquchengji = float(row[5])
                    zuoweitiqianqu_defen = zuoweitiqianqu_func(float(row[5]))[0]
                    zuoweitiqianqu_dengji = zuoweitiqianqu_func(float(row[5]))[1]
                except Exception as e:
                    raise Exception(f"【坐位体前屈项目计算错误】男生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # 三项   满分65分   50米20%   跳绳30%  坐位体前屈15%
                try:
                    sanxiangzongfen = wushimi_defen + tiaosheng_defen + zuoweitiqianqu_defen
                    sanxiangpingjunfen = round((wushimi_defen * 0.2 +
                                                (tiaosheng_defen - tiaosheng_jiafen) * 0.3 +
                                                zuoweitiqianqu_defen * 0.15) +
                                               tiaosheng_jiafen, 2)
                    sanxiangdengji = zuihoudengji65_panduan(sanxiangpingjunfen)
                except Exception as e:
                    raise Exception(f"【三项总分计算错误】男生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # ====================== 仰卧起坐 ======================
                try:
                    yangwoqizuo_str = str(row[6]).strip()

                    # 只要包含小数点，直接判定为非法成绩
                    if "." in yangwoqizuo_str:
                        raise ValueError(f"仰卧起坐成绩不能为小数，必须是整数，男生姓名：{xingming}，序号：{xuhao}")

                    # 转换为整数
                    yangwoqizuochengji = int(yangwoqizuo_str)

                    yangwoqizuo_defen = yangwoqizuo_func(yangwoqizuochengji)[0]
                    yangwoqizuo_dengji = yangwoqizuo_func(yangwoqizuochengji)[1]

                except Exception as e:
                    raise Exception(f"【仰卧起坐项目计算错误】男生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")


                # 四项 加测项目  4项  满分80分  50米20%   跳绳30%   坐位体前屈15%   仰卧起坐15%
                try:
                    sixiangzongfen = wushimi_defen + tiaosheng_defen + zuoweitiqianqu_defen + yangwoqizuo_defen
                    sixiangpingjunfen = round((wushimi_defen * 0.2 +
                                               (tiaosheng_defen - tiaosheng_jiafen) * 0.3 +
                                               zuoweitiqianqu_defen * 0.15 +
                                               yangwoqizuo_defen * 0.15) +
                                              tiaosheng_jiafen, 2)
                    sixiangdengji = zuihoudengji80_panduan(sixiangpingjunfen)
                except Exception as e:
                    raise Exception(f"【四项总分计算错误】男生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # ====================== 肺活量 ======================
                try:
                    feihuoliangchengji = float(row[7])
                    feihuoliang_defen = feihuoliang_func(float(row[7]))[0]
                    feihuoliang_dengji = feihuoliang_func(float(row[7]))[1]
                except Exception as e:
                    raise Exception(f"【肺活量项目计算错误】男生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # ====================== BMI ======================
                try:
                    shengao = float(row[8])
                    tizhong = float(row[9])
                    Bmi_defen = Bmi_func[0]
                    Bmi_dengji = Bmi_func[1]
                except Exception as e:
                    raise Exception(f"【BMI指数计算错误】男生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # 加上肺活量 bmi 仰卧起坐 6项 满分100分  50米20%   跳绳30%   坐位体前屈15%   仰卧起坐15%   肺活量10%   BMI10%
                try:
                    liuxiangzongfen = wushimi_defen + tiaosheng_defen + zuoweitiqianqu_defen + yangwoqizuo_defen + feihuoliang_defen + Bmi_defen
                    liuxiangpingjunfen = round((wushimi_defen * 0.2 +
                                                (tiaosheng_defen - tiaosheng_jiafen) * 0.3 +
                                                zuoweitiqianqu_defen * 0.15 +
                                                yangwoqizuo_defen * 0.15 +
                                                feihuoliang_defen * 0.1 +
                                                Bmi_defen * 0.1) +
                                               tiaosheng_jiafen, 2)
                    liuxiangdengji = zuihoudengji_panduan(liuxiangpingjunfen)
                except Exception as e:
                    raise Exception(f"【六项总分计算错误】男生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # 男生个人数据列表
                boy_list = [xuhao, xingming, xingbie,
                            wushimichengji, wushimi_defen, wushimi_dengji,
                            tiaoshengchengji, tiaosheng_defen, tiaosheng_jiafen, tiaosheng_dengji,
                            zuoweitiqianquchengji, zuoweitiqianqu_defen, zuoweitiqianqu_dengji,
                            sanxiangzongfen, sanxiangpingjunfen, sanxiangdengji,
                            yangwoqizuochengji, yangwoqizuo_defen, yangwoqizuo_dengji,
                            sixiangzongfen, sixiangpingjunfen, sixiangdengji,
                            feihuoliangchengji, feihuoliang_defen, feihuoliang_dengji,
                            shengao, tizhong, Bmi, Bmi_defen, Bmi_dengji,
                            liuxiangzongfen, liuxiangpingjunfen, liuxiangdengji,
                            banji
                            ]
                suoyou_nan.append(boy_list)

            else:
                # 既不是男/男生，也不是特殊，直接跳过
                continue

        except Exception as e:
            # 顶层捕获，显示精准定位信息，直接终止程序
            raise Exception(f"【男生数据处理失败】班级：{wenjianming}，<br>错误行数据：{row}<br>错误定位：{str(e)}")

    # ====================== 最终返回：男生列表 + 特殊人数 ======================
    return suoyou_nan, special_count



# 全体女生列表
def JiSuan_nv_list(data_list, wenjianming):
    suoyou_nv = []  # 全体女生  无排名
    special_count = 0  # 新增：统计【特殊】同学数量

    for row in data_list:
        try:
            # 获取索引2的性别值，去除空格并转字符串（兼容各种格式）
            gender = str(row[2]).strip()

            # ====================== 新增：特殊判断 ======================
            if gender in ["特殊女"]:
                special_count += 1  # 每遇到一个特殊，计数+1

                # 特殊：所有成绩、分数、等级全部设为 0
                xuhao = row[0]
                xingming = row[1]
                xingbie = gender
                banji = wenjianming

                # 特殊固定数据（全部 0）
                girl_list = [
                    xuhao, xingming, xingbie,
                    0, 0, "特殊",  # 50米：成绩、分数、等级
                    0, 0, 0, "特殊",  # 跳绳：成绩、分数、加分、等级
                    0, 0, "特殊",  # 坐位体前屈：成绩、分数、等级
                    0, 0, "特殊",  # 三项：总分、平均分、等级
                    0, 0, "特殊",  # 仰卧起坐：成绩、分数、等级
                    0, 0, "特殊",  # 四项：总分、平均分、等级
                    0, 0, "特殊",  # 肺活量：成绩、分数、等级
                    0, 0, 0, 0, "特殊",  # 身高、体重、BMI、BMI分数、BMI等级
                    0, 0, "特殊",  # 六项：总分、平均分、等级
                    banji
                ]
                suoyou_nv.append(girl_list)
                continue  # 跳过后续计算，直接处理下一行

            # ====================== 原有女生判断逻辑 ======================
            if gender in ['女', '女生']:
                Bmi = round((float(row[9])) / (((float(row[8])) / 100) * ((int(float(row[8]))) / 100)), 1)

                wushimi_func = ernianji_nv_wushimi_jisuan_fenshu
                tiaosheng_func = ernianji_nv_tiaosheng_jisuan_fenshu
                zuoweitiqianqu_func = ernianji_nv_zuoweitiqianqu_jisuan_fenshu
                yangwoqizuo_func = 二年级女生仰卧起坐计算分数
                feihuoliang_func = ernianji_nv_feihuoliang_jisuan_fenshu
                Bmi_func = 二年级女生体重指数计算分数(Bmi)
                xuhao = row[0]
                xingming = row[1]
                xingbie = row[2]
                banji = wenjianming

                # ====================== 50米 ======================
                try:
                    wushimichengji = float(row[3])
                    wushimi_defen = wushimi_func(float(row[3]))[0]
                    wushimi_dengji = wushimi_func(float(row[3]))[1]

                except Exception as e:
                    raise Exception(f"【50米项目计算错误】女生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # ====================== 跳绳 ======================
                try:
                    tiaosheng_str = str(row[4]).strip()

                    # 只要包含小数点，直接判定为非法成绩
                    if "." in tiaosheng_str:
                        raise ValueError(f"跳绳成绩不能为小数，必须是整数，女生姓名：{xingming}，序号：{xuhao}")

                    # 转换为整数
                    tiaoshengchengji = int(tiaosheng_str)

                    tiaosheng_defen = tiaosheng_func(tiaoshengchengji)[0]
                    tiaosheng_dengji = tiaosheng_func(tiaoshengchengji)[1]
                    tiaosheng_jiafen = tiaosheng_defen - 100 if tiaosheng_defen > 100 else 0

                except Exception as e:
                    raise Exception(f"【跳绳项目计算错误】女生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")
                # ====================== 坐位体前屈 ======================
                try:
                    zuoweitiqianquchengji = float(row[5])
                    zuoweitiqianqu_defen = zuoweitiqianqu_func(float(row[5]))[0]
                    zuoweitiqianqu_dengji = zuoweitiqianqu_func(float(row[5]))[1]
                except Exception as e:
                    raise Exception(f"【坐位体前屈项目计算错误】女生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # 三项   满分65分   50米20%   跳绳30%  坐位体前屈15%
                try:
                    sanxiangzongfen = wushimi_defen + tiaosheng_defen + zuoweitiqianqu_defen
                    sanxiangpingjunfen = round((wushimi_defen * 0.2 +
                                                (tiaosheng_defen - tiaosheng_jiafen) * 0.3 +
                                                zuoweitiqianqu_defen * 0.15) +
                                               tiaosheng_jiafen, 2)
                    sanxiangdengji = zuihoudengji65_panduan(sanxiangpingjunfen)
                except Exception as e:
                    raise Exception(f"【三项总分计算错误】女生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # ====================== 仰卧起坐女 ======================
                try:
                    yangwoqizuo_str = str(row[6]).strip()

                    # 只要包含小数点，直接判定为非法成绩
                    if "." in yangwoqizuo_str:
                        raise ValueError(f"仰卧起坐成绩不能为小数，必须是整数，女生姓名：{xingming}，序号：{xuhao}")

                    # 转换为整数
                    yangwoqizuochengji = int(yangwoqizuo_str)

                    yangwoqizuo_defen = yangwoqizuo_func(yangwoqizuochengji)[0]
                    yangwoqizuo_dengji = yangwoqizuo_func(yangwoqizuochengji)[1]

                except Exception as e:
                    raise Exception(f"【仰卧起坐项目计算错误】女生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # 四项 加测项目  4项  满分80分  50米20%   跳绳30%   坐位体前屈15%   仰卧起坐15%
                try:
                    sixiangzongfen = wushimi_defen + tiaosheng_defen + zuoweitiqianqu_defen + yangwoqizuo_defen
                    sixiangpingjunfen = round((wushimi_defen * 0.2 +
                                               (tiaosheng_defen - tiaosheng_jiafen) * 0.3 +
                                               zuoweitiqianqu_defen * 0.15 +
                                               yangwoqizuo_defen * 0.15) +
                                              tiaosheng_jiafen, 2)
                    sixiangdengji = zuihoudengji80_panduan(sixiangpingjunfen)
                except Exception as e:
                    raise Exception(f"【四项总分计算错误】女生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # ====================== 肺活量 ======================
                try:
                    feihuoliangchengji = float(row[7])
                    feihuoliang_defen = feihuoliang_func(float(row[7]))[0]
                    feihuoliang_dengji = feihuoliang_func(float(row[7]))[1]
                except Exception as e:
                    raise Exception(f"【肺活量项目计算错误】女生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # ====================== BMI ======================
                try:
                    shengao = float(row[8])
                    tizhong = float(row[9])
                    Bmi_defen = Bmi_func[0]
                    Bmi_dengji = Bmi_func[1]
                except Exception as e:
                    raise Exception(f"【BMI指数计算错误】女生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # 加上肺活量 bmi 仰卧起坐 6项 满分100分  50米20%   跳绳30%   坐位体前屈15%   仰卧起坐15%   肺活量10%   BMI10%
                try:
                    liuxiangzongfen = wushimi_defen + tiaosheng_defen + zuoweitiqianqu_defen + yangwoqizuo_defen + feihuoliang_defen + Bmi_defen
                    liuxiangpingjunfen = round((wushimi_defen * 0.2 +
                                                (tiaosheng_defen - tiaosheng_jiafen) * 0.3 +
                                                zuoweitiqianqu_defen * 0.15 +
                                                yangwoqizuo_defen * 0.15 +
                                                feihuoliang_defen * 0.1 +
                                                Bmi_defen * 0.1) +
                                               tiaosheng_jiafen, 2)
                    liuxiangdengji = zuihoudengji_panduan(liuxiangpingjunfen)
                except Exception as e:
                    raise Exception(f"【六项总分计算错误】女生姓名：{xingming}，序号：{xuhao}，<br>错误信息：{str(e)}")

                # 女生个人数据列表
                girl_list = [xuhao, xingming, xingbie,
                            wushimichengji, wushimi_defen, wushimi_dengji,
                            tiaoshengchengji, tiaosheng_defen, tiaosheng_jiafen, tiaosheng_dengji,
                            zuoweitiqianquchengji, zuoweitiqianqu_defen, zuoweitiqianqu_dengji,
                            sanxiangzongfen, sanxiangpingjunfen, sanxiangdengji,
                            yangwoqizuochengji, yangwoqizuo_defen, yangwoqizuo_dengji,
                            sixiangzongfen, sixiangpingjunfen, sixiangdengji,
                            feihuoliangchengji, feihuoliang_defen, feihuoliang_dengji,
                            shengao, tizhong, Bmi, Bmi_defen, Bmi_dengji,
                            liuxiangzongfen, liuxiangpingjunfen, liuxiangdengji,
                            banji
                            ]
                suoyou_nv.append(girl_list)

            else:
                # 既不是女/女生，也不是特殊，直接跳过
                continue

        except Exception as e:
            # 顶层捕获，显示精准定位信息，直接终止程序
            raise Exception(f"【女生数据处理失败】班级：{wenjianming}，<br>错误行数据：{row}<br>错误定位：{str(e)}")

    # ====================== 最终返回：女生列表 + 特殊人数 ======================
    return suoyou_nv, special_count



# 全体学生 成绩排名
def JiSuan_tianjiapaiming(suoyin, quantixuesheng_list):
    # ===================== 新增：先过滤出【非特殊】学生，只给他们排名 =====================
    # 筛选出性别不是特殊的学生（用于排名计算）
    valid_students = []
    for item in quantixuesheng_list:
        gender = str(item[2]).strip()  # 性别列：索引2
        if gender not in ["特殊男","特殊女"]:
            valid_students.append(item)

    # 给【非特殊】学生生成排名字典
    rank_dict = {}
    if valid_students:
        # 提取索引的值并保存原索引
        tiqu_index = [(item[suoyin], index) for index, item in enumerate(valid_students)]
        # 按索引值从大到小排序
        paixu_index = sorted(tiqu_index, key=lambda x: x[0], reverse=True)
        # 分配名次（同分同名次）
        rank = 1
        for i in range(len(paixu_index)):
            value = paixu_index[i][0]
            if value not in rank_dict:
                rank_dict[value] = rank
            rank += 1

    # ===================== 遍历所有学生，插入名次 / 特殊 =====================
    for item in quantixuesheng_list:
        gender = str(item[2]).strip()

        # 特殊学生 → 插入“特殊”，不参与排名
        if gender in ["特殊男","特殊女"]:
            if suoyin == 8:
                item.insert(suoyin + 2, "特殊")
            else:
                item.insert(suoyin + 1, "特殊")

        # 正常学生 → 插入排名
        else:
            value = int(item[suoyin])
            if suoyin == 8:
                item.insert(suoyin + 2, f"{rank_dict[value]}")
            else:
                item.insert(suoyin + 1, f"{rank_dict[value]}")

    return quantixuesheng_list

# 计算 个人项目 总成绩 三项、四项。。。
def JiSuan_zongchengji(suoyin, quanbanpaiming):
    # 🔴 新增：先遍历所有学生，标记特殊（性别=索引2）
    for item in quanbanpaiming:
        gender = str(item[2]).strip()  # 取性别列，去空格
        if gender in ["特殊男","特殊女"]:
            # 特殊：直接插入“特殊”，不参与排名计算
            item.insert(suoyin + 1, "特殊")

    # 过滤掉特殊的学生，只保留正常学生参与排名
    valid_items_for_rank = []
    for idx, item in enumerate(quanbanpaiming):
        gender = str(item[2]).strip()
        if gender not in ["特殊男","特殊女"]:
            valid_items_for_rank.append((idx, item))  # 保存原始索引+数据

    # ===================== 原有排名逻辑（只处理非特殊学生） =====================
    if not valid_items_for_rank:
        return quanbanpaiming  # 全部特殊，直接返回

    # 提取有效学生的分数（用于原逻辑计算）
    values = [item[suoyin] for (idx, item) in valid_items_for_rank]
    total = len(valid_items_for_rank)

    # 严格按你要求的四舍五入规则：44→4，45→5，46→6
    # 计算最小10%的数量（四舍五入，确保至少1个）
    min_count = max(1, int(total * 0.1 + 0.5))

    # 按分数升序排序（从小到大），保留原始索引
    scored_indices = [(valid_items_for_rank[i][1][suoyin], i) for i in range(total)]
    scored_indices.sort()  # 按分数升序

    # 取出前 min_count 个位置（最低分区域）
    selected_low_indices = scored_indices[:min_count]
    # 取出临界分数（第 min_count 名的分数）
    if min_count < total:
        threshold_score = scored_indices[min_count - 1][0]
    else:
        threshold_score = scored_indices[-1][0]

    # 找出所有 分数 == 临界分 的位置（同分临界区）
    critical_candidates = [i for score, i in scored_indices if score == threshold_score]
    # 已经选中的临界区位置
    selected_critical = [i for score, i in selected_low_indices if score == threshold_score]

    # 临界同分随机剔除，保证最终正好 min_count 个不计排名
    final_excluded_indices = set()
    for score, idx in scored_indices:
        if score < threshold_score:
            final_excluded_indices.add(idx)
        elif score == threshold_score:
            final_excluded_indices.add(idx)

    # 超出的临界同分随机删除
    while len(final_excluded_indices) > min_count:
        random_rm = random.choice(critical_candidates)
        if random_rm in final_excluded_indices:
            final_excluded_indices.remove(random_rm)

    # 标记不计排名 & 收集有效数据
    sum_valid = 0
    valid_items = []
    for list_idx, (original_idx, item) in enumerate(valid_items_for_rank):
        if list_idx in final_excluded_indices:
            # 不计排名（插入到原始列表）
            quanbanpaiming[original_idx].insert(suoyin + 1, '不计排名')
        else:
            valid_items.append((original_idx, item))
            sum_valid += item[suoyin]

    # 对有效元素按成绩降序排序
    sorted_valid_items = sorted(valid_items, key=lambda x: x[1][suoyin], reverse=True)

    # 生成名次（同分同名次）
    rank_dict = {}
    rank = 1
    for i in range(len(sorted_valid_items)):
        value = sorted_valid_items[i][1][suoyin]
        if value not in rank_dict:
            rank_dict[value] = rank
        rank += 1

    # 插回名次（保持原顺序）
    for original_idx, item in valid_items:
        value = item[suoyin]
        quanbanpaiming[original_idx].insert(suoyin + 1, f"{rank_dict[value]}")

    return quanbanpaiming


# 去掉不计排名   男、女生列表
def JiSuan_qudiaobujipaiming(suoyin,xuesheng):
    qudiaobujipaiming=[]
    # 正向遍历（无需反向，因为只读取不删除原列表元素）
    for nan_sheng_row in xuesheng:
        # 检查索引18的值是否为「不计排名」（无需容错，直接取）
        if nan_sheng_row[suoyin] != "不计排名":
            # 把「非不计排名」的男生子列表添加到有效列表中
            qudiaobujipaiming.append(nan_sheng_row)
    return qudiaobujipaiming

# 全班总分计算
def JiSuanPingJunFen(suoyin,nan_list,nv_list):
    # 三项总分
    nanzongfen = sum([sublist[suoyin] for sublist in list(nan_list)])
    nvzongfen = sum([sublist[suoyin] for sublist in list(nv_list)])
    pingjunfen = round((nanzongfen + nvzongfen) / (len(list(nan_list)) + len(list(nv_list))), 2)

    # 男生 女生  平均分
    nan_pingjunfen = round(nanzongfen / len(list(nan_list)), 2)
    nv_pingjunfen = round(nvzongfen / len(list(nv_list)), 2)

    return pingjunfen,nan_pingjunfen,nv_pingjunfen

# 全班各种率计算
def JiSuanYouLiangLv(suoyin,nan_list,nv_list):
    nandengji = {'优秀': 0, '良好': 0, '及格': 0, '不及格': 0}
    for sub_list in list(nan_list):
        grade = sub_list[suoyin]
        if grade in nandengji:
            nandengji[grade] += 1

    nvdengji = {'优秀': 0, '良好': 0, '及格': 0, '不及格': 0}
    for sub_list in list(nv_list):
        grade = sub_list[suoyin]
        if grade in nvdengji:
            nvdengji[grade] += 1

    # 各等级总人数
    zong_youxiu_shu = int(nandengji['优秀'] + nvdengji['优秀'])
    zong_lianghao_shu = int(nandengji['良好'] + nvdengji['良好'])
    zong_youliang_shu = int(nandengji['优秀'] + nvdengji['优秀'] + nandengji['良好'] + nvdengji['良好'])
    zong_jige_shu = int(nandengji['及格'] + nvdengji['及格'])
    zong_bujige_shu = int(nandengji['不及格'] + nvdengji['不及格'])

    # 男生  各等级人数
    nan_youxiu_shu = int(nandengji['优秀'])
    nan_lianghao_shu = int(nandengji['良好'])
    nan_youliang_shu = int(nandengji['优秀'] + nandengji['良好'])
    nan_jige_shu = int(nandengji['及格'])
    nan_bujige_shu = int(nandengji['不及格'])

    # 女生 各等级人数
    nv_youxiu_shu = int(nvdengji['优秀'])
    nv_lianghao_shu = int(nvdengji['良好'])
    nv_youliang_shu = int(nvdengji['优秀'] + nvdengji['良好'])
    nv_jige_shu = int(nvdengji['及格'])
    nv_bujige_shu = int(nvdengji['不及格'])

    # 总等级各种率
    zong_youxiulv = round((nandengji['优秀'] + nvdengji['优秀']) / (len(list(nan_list)) + len(list(nv_list))), 4)
    zong_lianghaolv = round( (nandengji['良好'] + nvdengji['良好']) / (len(list(nan_list)) + len(list(nv_list))), 4)
    zong_youlianglv = zong_youxiulv + zong_lianghaolv
    zong_jigelv = round((nandengji['及格'] + nvdengji['及格']) / (len(list(nan_list)) + len(list(nv_list))), 4)
    zong_bujigelv = round((nandengji['不及格'] + nvdengji['不及格']) / (len(list(nan_list)) + len(list(nv_list))), 4)

    # 男生各等级的率
    nan_youxiulv = round((nandengji['优秀']) / (len(list(nan_list))), 4)
    nan_lianghaolv = round((nandengji['良好']) / (len(list(nan_list))), 4)
    nan_youlianglv = nan_youxiulv + nan_lianghaolv
    nan_jigelv = round((nandengji['及格']) / (len(list(nan_list))), 4)
    nan_bujigelv = round((nandengji['不及格']) / (len(list(nan_list))), 4)

    # 女生各等级的率
    nv_youxiulv = round((nvdengji['优秀']) / (len(list(nv_list))), 4)
    nv_lianghaolv = round((nvdengji['良好']) / (len(list(nv_list))), 4)
    nv_youlianglv = nv_youxiulv + nv_lianghaolv
    nv_jigelv = round((nvdengji['及格']) / (len(list(nv_list))), 4)
    nv_bujigelv = round((nvdengji['不及格']) / (len(list(nv_list))), 4)

    return (zong_youxiu_shu, zong_lianghao_shu, zong_youliang_shu, zong_jige_shu, zong_bujige_shu,
            zong_youxiulv,   zong_lianghaolv,   zong_youlianglv,   zong_jigelv,   zong_bujigelv,
            nan_youxiu_shu,  nan_lianghao_shu,  nan_youliang_shu,  nan_jige_shu,  nan_bujige_shu,
            nan_youxiulv,    nan_lianghaolv,    nan_youlianglv,    nan_jigelv,    nan_bujigelv,
            nv_youxiu_shu,   nv_lianghao_shu,   nv_youliang_shu,   nv_jige_shu,   nv_bujige_shu,
            nv_youxiulv,     nv_lianghaolv,     nv_youlianglv,     nv_jigelv,     nv_bujigelv)



def tiaosheng_manfen(suoyin,nan_list,nv_list):
    #男生满120列表
    nan__tiaosheng_120 = []
    #男生100-119之间列表
    nan__tiaosheng_100119 = []
    # 三项成绩女生达120人数 比率 达100-119人数 比率
    for nv in nan_list:
        if nv[suoyin] >= 120:
            nan__tiaosheng_120.append(nv)
        elif 120 > nv[suoyin] >= 100:
            nan__tiaosheng_100119.append(nv)
    nan_man120_renshu = len(nan__tiaosheng_120)
    nan_man120_bilv = round((len(nan__tiaosheng_120)) / (len(nan_list)), 4)
    nan_man100119_renshu = len(nan__tiaosheng_100119)
    nan_man100119_bilv = round((len(nan__tiaosheng_100119)) / (len(nan_list)), 4)


    #女生满120列表
    nv_tiaosheng_120 = []
    #女生100-119之间列表
    nv_tiaosheng_100119 = []

    # 三项成绩女生达120人数 比率 达100-119人数 比率
    for nv in nv_list:
        if nv[suoyin] >= 120:
            nv_tiaosheng_120.append(nv)
        elif 120 > nv[suoyin] >= 100:
            nv_tiaosheng_100119.append(nv)

    nv_man120_renshu = len(nv_tiaosheng_120)
    nv_man120_bilv = round((len(nv_tiaosheng_120)) / (len(nv_list)), 4)
    nv_man100119_renshu = len(nv_tiaosheng_100119)
    nv_man100119_bilv = round((len(nv_tiaosheng_100119)) / (len(nv_list)), 4)

    man120_renshu = nan_man120_renshu + nv_man120_renshu
    man120_bilv = round((nan_man120_renshu + nv_man120_renshu)/(len(nan_list) + len(nv_list)),4)
    man100119_renshu = nan_man100119_renshu + nv_man100119_renshu
    man100119_bilv = round((nan_man100119_renshu + nv_man100119_renshu)/(len(nan_list) + len(nv_list)),4)


    return [man120_bilv,     man120_renshu,      man100119_bilv,      man100119_renshu,
            nan_man120_bilv, nan_man120_renshu,  nan_man100119_bilv,  nan_man100119_renshu,
            nv_man120_bilv,  nv_man120_renshu,   nv_man100119_bilv,   nv_man100119_renshu]








