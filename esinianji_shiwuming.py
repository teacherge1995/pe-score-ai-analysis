def sinianji_sort_by_index5(all_rows):
    """
    核心功能：按第三列（索引2）区分男生/女生，男生行在前、女生行在后拼接，无排序纯分组
    适配：无需改主程序，直接替换即可使用，异常时返回原数据
    :param all_rows: 所有Excel合并后的大列表，每行是一个小列表
    :return: 男生行 + 女生行 拼接后的新列表
    """
    try:
        # 初始化两个列表，分别存储男生、女生行
        boy_rows = []  # 男生行：第三列是“男”或“男生”
        girl_rows = []  # 女生行：第三列是“女”或“女生”
        other_rows = []  # 异常行：其他所有情况

        # 遍历所有行，按第三列（索引2）分组
        for row in all_rows:
            # 容错：行数据不足3列（无第三列），归为异常行
            if len(row) < 3:
                other_rows.append(row)
                continue

            # 取第三列值，转字符串+去空格，统一判定
            gender_str = str(row[2]).strip()

            # 精确匹配：只识别“男”“男生”“女”“女生”，其他都不算
            if gender_str == "男" or gender_str == "男生":
                #男生列表
                boy_rows.append(row)
            elif gender_str == "女" or gender_str == "女生":
                # 女生列表
                girl_rows.append(row)
            else:
                other_rows.append(row)

        # ===================== 男生各项排序 =====================
        # 50米成绩升序加排序
        wushimi_sorted_lst = sorted(boy_rows, key=lambda x: x[3])
        wushimi_paixu = [item[:3] + [rank] + item[3:] for rank, item in enumerate(wushimi_sorted_lst, start=1)]
        # 保留 序号 性别  排序 班级 姓名  成绩
        wushimi_result = [[x[0], x[2], x[3], x[47],x[1], x[4]] for x in wushimi_paixu]
        wushimi = [x[:2] + ["50米"] + x[2:] for x in wushimi_result]
        #保留前15名
        wushimi_nan_lst = wushimi[:15]
        #跳绳
        tiaosheng_nan_lst = qianshiwuming(7,8,boy_rows,'跳绳')
        #坐位体前屈
        zuoweitiqianqu_nan_lst = qianshiwuming(12, 13, boy_rows, '坐位体前屈')
        # 仰卧起坐
        yangwoqizuo_nan_lst = qianshiwuming(16, 17, boy_rows, '仰卧起坐')
        # 四项总分
        sixiangzongfen_nan_lst = qianshiwuming(21, 22, boy_rows, '四项总分')
        # 立定跳远
        lidingtiaoyuan_nan_lst = qianshiwuming(24, 25, boy_rows, '立定跳远')
        # 五项总分
        wuxiangzongfen_nan_lst = qianshiwuming(29, 30, boy_rows, '五项总分')

        # ===================== 女生各项排序 =====================
        # 50米成绩升序加排序
        wushimi_sorted_lst = sorted(girl_rows, key=lambda x: x[3])
        wushimi_paixu = [item[:3] + [rank] + item[3:] for rank, item in enumerate(wushimi_sorted_lst, start=1)]
        # 保留 序号 性别  排序 班级 姓名  成绩
        wushimi_result = [[x[0], x[2], x[3], x[47], x[1], x[4]] for x in wushimi_paixu]
        wushimi = [x[:2] + ["50米"] + x[2:] for x in wushimi_result]
        # 保留前15名
        wushimi_nv_lst = wushimi[:15]
        # 跳绳
        tiaosheng_nv_lst = qianshiwuming(7,8,girl_rows,'跳绳')
        # 坐位体前屈
        zuoweitiqianqu_nv_lst = qianshiwuming(12, 13, girl_rows, '坐位体前屈')
        # 仰卧起坐
        yangwoqizuo_nv_lst = qianshiwuming(16, 17, girl_rows, '仰卧起坐')
        # 四项总分
        sixiangzongfen_nv_lst = qianshiwuming(21, 22, girl_rows, '四项总分')
        # 立定跳远
        lidingtiaoyuan_nv_lst = qianshiwuming(24, 25, girl_rows, '立定跳远')
        # 五项总分
        wuxiangzongfen_nv_lst = qianshiwuming(29, 30, girl_rows, '五项总分')

        # 最终拼接规则：男生行 → 女生行 → 异常行（无性别标识/无第三列）
        final_rows = (wushimi_nan_lst + wushimi_nv_lst +
                      tiaosheng_nan_lst + tiaosheng_nv_lst +
                      zuoweitiqianqu_nan_lst + zuoweitiqianqu_nv_lst+
                      yangwoqizuo_nan_lst + yangwoqizuo_nv_lst +
                      sixiangzongfen_nan_lst + sixiangzongfen_nv_lst+
                      lidingtiaoyuan_nan_lst + lidingtiaoyuan_nv_lst +
                      wuxiangzongfen_nan_lst+ wuxiangzongfen_nv_lst)
        # for i in final_rows:
        #     print(i)
        print(f"性别分组完成：男生{len(boy_rows)}人 | 女生{len(girl_rows)}人 | 异常{len(other_rows)}人")
        return final_rows

    except Exception as e:
        # 出错时返回原数据，不崩溃主程序，打印错误信息
        print(f"性别分组处理异常: {e}")
        return all_rows






def qianshiwuming(suoyin1,suoyin2,boy_rows,xiangmu):

    list1 = sorted(boy_rows, key=lambda x: (not isinstance(x[suoyin1], (int, float)), x[suoyin1]), reverse=True)
    list_paixu = [item[:3] + [rank] + item[3:] for rank, item in enumerate(list1, start=1)]
    # 保留                序号    性别  排序   班级    姓名  成绩
    list_result = [[x[0], x[2], x[3], x[47], x[1], x[suoyin2]] for x in list_paixu]
    list_suoyou = [x[:2] + [xiangmu] + x[2:] for x in list_result]
    # 保留前15名
    zuizhonglist = list_suoyou[:15]

    return zuizhonglist