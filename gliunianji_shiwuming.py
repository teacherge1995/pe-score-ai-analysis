def liunianji_sort_by_index5(all_rows):
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
                boy_rows.append(row)
            elif gender_str == "女" or gender_str == "女生":
                girl_rows.append(row)
            else:
                other_rows.append(row)

        # ===================== 男生各项排序 =====================
        # 50米成绩升序
        wushimi_nan_lst = sudu(3, 4, "50米", boy_rows)
        # 跳绳
        tiaosheng_nan_lst = qianshiwuming(7, 8, boy_rows, '跳绳')
        # 坐位体前屈
        zuoweitiqianqu_nan_lst = qianshiwuming(12, 13, boy_rows, '坐位体前屈')
        # 仰卧起坐
        yangwoqizuo_nan_lst = qianshiwuming(16, 17, boy_rows, '仰卧起坐')
        # 50*8 升序
        wushichengba_nan_lst = sudu(20, 21, "50*8", boy_rows)
        # 五项总分
        wuxiangchengji_nan_lst = qianshiwuming(25, 26, boy_rows, '五项总分')
        # 直臂悬垂
        zhibixuanchui_nan_lst = qianshiwuming(28, 29, boy_rows, '直臂悬垂')
        # 六项总分
        liuxiangzongfen_nan_lst = qianshiwuming(33, 34, boy_rows, '六项总分')

        # ===================== 女生各项排序 =====================
        # 50米成绩升序
        wushimi_nv_lst = sudu(3, 4, "50米", girl_rows)
        # 跳绳
        tiaosheng_nv_lst = qianshiwuming(7, 8, girl_rows, '跳绳')
        # 坐位体前屈
        zuoweitiqianqu_nv_lst = qianshiwuming(12, 13, girl_rows, '坐位体前屈')
        # 仰卧起坐
        yangwoqizuo_nv_lst = qianshiwuming(16, 17, girl_rows, '仰卧起坐')
        # 50*8 升序
        wushichengba_nv_lst = sudu(20, 21, "50*8", girl_rows)
        # 五项成绩
        wuxiangchengji_nv_lst = qianshiwuming(25, 26, girl_rows, '五项总分')
        # 六项总分
        liuxiangzongfen_nv_lst = qianshiwuming(33, 34, girl_rows, '六项总分')

        # 最终拼接
        final_rows = (wushimi_nan_lst + wushimi_nv_lst +
                      tiaosheng_nan_lst + tiaosheng_nv_lst +
                      zuoweitiqianqu_nan_lst + zuoweitiqianqu_nv_lst +
                      yangwoqizuo_nan_lst + yangwoqizuo_nv_lst +
                      wushichengba_nan_lst + wushichengba_nv_lst +
                      wuxiangchengji_nan_lst + wuxiangchengji_nv_lst +
                      zhibixuanchui_nan_lst +
                      liuxiangzongfen_nan_lst + liuxiangzongfen_nv_lst)

        print(f"性别分组完成：男生{len(boy_rows)}人 | 女生{len(girl_rows)}人 | 异常{len(other_rows)}人")
        return final_rows

    except Exception as e:
        print(f"性别分组处理异常: {e}")
        return all_rows







def qianshiwuming(suoyin1,suoyin2,boy_rows,xiangmu):

    list1 = sorted(boy_rows, key=lambda x: (not isinstance(x[suoyin1], (int, float)), x[suoyin1]), reverse=True)
    list_paixu = [item[:3] + [rank] + item[3:] for rank, item in enumerate(list1, start=1)]
    # 保留                序号    性别  排序   班级    姓名  成绩
    list_result = [[x[0], x[2], x[3], x[51], x[1], x[suoyin2]] for x in list_paixu]
    list_suoyou = [x[:2] + [xiangmu] + x[2:] for x in list_result]
    # 保留前15名
    zuizhonglist = list_suoyou[:15]

    return zuizhonglist




def  sudu (chengjisuoyin,suoyin2, xiangmu,rows):
    # 50米成绩升序加排序
    sorted_lst = sorted(rows, key=lambda x: x[chengjisuoyin])
    paixu = [item[:chengjisuoyin] + [rank] + item[chengjisuoyin:] for rank, item in enumerate(sorted_lst, start=1)]
    # 保留 序号 性别  排序 班级 姓名  成绩
    result = [[x[0], x[2], x[chengjisuoyin], x[51], x[1], x[suoyin2]] for x in paixu]
    zuizhongpaixu = [x[:2] + [xiangmu] + x[2:] for x in result]
    # 保留前15名
    n_lst15 = zuizhongpaixu[:15]

    return n_lst15