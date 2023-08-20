# coding:utf-8
from django.shortcuts import render
import pandas as pd
from collections import Counter
import numpy as np
from django.views.generic.base import View
from MyHome.settings import *

# 计算全部羁绊关联的武将且优先选择定位属性
sum_atk = 0
sum_def = 0
sum_HP = 0
sum_war = 0
sum_str = 0
sum_move = 0


class SanGuoRenWuJiBanView(View):
    def get(self, request):
        return render(request, "GameTool/SanGuoRenWuJiBan.html")

    def post(self, request):
        dir_root = BASE_DIR + '\\apps\\GameTool\\data\\'

        df = pd.read_excel(dir_root + "sanguo_data.xlsx", sheet_name="全部羁绊")
        df_s = pd.read_excel(dir_root + "sanguo_data.xlsx", sheet_name="特殊羁绊")
        df_c = pd.read_excel(dir_root + "sanguo_data.xlsx", sheet_name="国家")

        name_1 = request.POST.get("name_1")  # 获取提交的武将姓名
        attr_type = request.POST.get("attr_type")  # 获取提交的武将姓名

        # attr属性列表索引序号
        attr_type_dict = {
            "atk": 0, "def": 1, "HP": 2, "war": 3, "str": 4, "move": 5
        }
        try:
            all_data_list = []

            for i in range(len(df)):
                if name_1 in df["name1"][i] or name_1 in df["name2"][i] or name_1 in df["name3"][i]:
                    # 添加遍历的武将姓名
                    name_list = [df['name1'][i], df['name2'][i], df['name3'][i]]
                    name_list = [i for i in name_list if i != '-']
                    name_tuple = tuple(name_list)
                    # 获取当前记录的属性值
                    data_atk = df['atk'][i]
                    data_def = df['def'][i]
                    data_HP = df['HP'][i]
                    data_war = df['war'][i]
                    data_str = df['str'][i]
                    data_move = df['move'][i]
                    data_list = (data_atk, data_def, data_HP, data_war, data_str, data_move)
                    # 计算当前记录所选属性的贡献度
                    attr_dict = {
                        "atk": data_atk, "def": data_def, "HP": data_HP, "war": data_war, "str": data_str,
                        "move": data_move
                    }
                    attr_w = attr_dict[attr_type] / len(name_list)

                    result_data = (name_tuple, data_list, attr_w)

                    if data_list[attr_type_dict[attr_type]] != 0:
                        all_data_list.append(result_data)

            # 根据所选择的羁绊人物填充到列表，数值累计求和
            def append_sum_data(name_list, df, i):

                # 设置全局变量
                global sum_atk, sum_def, sum_HP, sum_war, sum_str, sum_move

                # 添加遍历的武将姓名
                name_list = name_list + [df['name1'][i], df['name2'][i], df['name3'][i]]

                # 累计求和遍历的武将关联的数值属性
                sum_atk = sum_atk + df['atk'][i]
                sum_def = sum_def + df['def'][i]
                sum_HP = sum_HP + df['HP'][i]
                sum_war = sum_war + df['war'][i]
                sum_str = sum_str + df['str'][i]
                sum_move = sum_move + df['move'][i]

                #     print(sum_atk,sum_def,sum_HP,sum_war,sum_str,sum_move)

                return name_list

            # 计算全部羁绊关联的武将且优先选择定位属性
            name_list = []

            for i in range(len(df)):
                # 先遍历 name_1 优选，根据一个优先选择项排除无用的羁绊关联
                if name_1 in df['name1'][i]:
                    # 根据所选择的羁绊人物填充到列表，数值累计求和
                    name_list = append_sum_data(name_list, df, i)
                elif name_1 in df['name2'][i]:
                    name_list = append_sum_data(name_list, df, i)
                elif name_1 in df['name3'][i]:
                    name_list = append_sum_data(name_list, df, i)

            # name1 武将列表去重、删除空白制表符
            name1_list = list(set(name_list))
            name1_list = [i for i in name1_list if i != '-']
            name1_list.remove(name_1)

            print("{} {} 羁绊所需 {} 人物：".format(name_1, attr_type, len(name1_list)), ",".join(name1_list))
            print(
                "计算结果：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(sum_atk, sum_def, sum_HP, sum_war, sum_str, sum_move))

            for name in name1_list:
                for i in range(len(df)):
                    if name in df["name1"][i] or name in df["name2"][i] or name in df["name3"][i]:
                        # 添加遍历的武将姓名
                        name_list = [df['name1'][i], df['name2'][i], df['name3'][i]]
                        name_list = [i for i in name_list if i != '-']
                        name_tuple = tuple(name_list)
                        # 获取当前记录的属性值
                        data_atk = df['atk'][i]
                        data_def = df['def'][i]
                        data_HP = df['HP'][i]
                        data_war = df['war'][i]
                        data_str = df['str'][i]
                        data_move = df['move'][i]
                        data_list = (data_atk, data_def, data_HP, data_war, data_str, data_move)
                        # 计算当前记录所选属性的贡献度
                        attr_dict = {
                            "atk": data_atk, "def": data_def, "HP": data_HP, "war": data_war, "str": data_str,
                            "move": data_move
                        }
                        attr_w = attr_dict[attr_type] / len(name_list)

                        result_data = (name_tuple, data_list, attr_w)

                        if data_list[attr_type_dict[attr_type]] != 0:
                            all_data_list.append(result_data)

            # 按照w权重排序
            all_data_list = list(set(all_data_list))
            all_data_list = sorted(all_data_list, key=lambda x: x[2], reverse=True)

            result_name_list = []
            result_data_list = [0, 0, 0, 0, 0, 0]
            result_all_data_list = []
            person_num = 11  # 限制羁绊1-9人
            for data in all_data_list:
                if len(result_name_list) < person_num:
                    # 累计填充武将
                    result_name_list = result_name_list + list(data[0])
                    result_name_list = list(set(result_name_list))
                    # 累计求和数值
                    result_data_list = list(np.sum([result_data_list, data[1]], axis=0))
                    # 重新构建贡献数据
                    result_all_data_list.append(data)

            # 计算势力数值加成获取3同势力数据
            df_s_3_nation = df_s[df_s["data"] == "3同势力"]
            df_s_3_dict = df_s_3_nation.to_dict('records')[0]

            # 将羁绊全部武将列入
            df_c_result = df_c[df_c['name'].isin(result_name_list)]
            df_c_result.reset_index(inplace=True, drop=True)
            # 统计国家频次list 计算3个同样国家的人物触发羁绊
            counter = Counter(df_c_result["nation"].to_list())
            nation_list = []
            for k, v in counter.items():
                if v > 2:
                    nation_list.append(k)

            # 激活的国家羁绊数量
            len_nation_list = len(nation_list)

            # 国家羁绊增加数值
            nation_data_list = [
                df_s_3_dict["atk"] * len_nation_list,
                df_s_3_dict["def"] * len_nation_list,
                df_s_3_dict["HP"] * len_nation_list,
                df_s_3_dict["war"] * len_nation_list,
                df_s_3_dict["str"] * len_nation_list,
                df_s_3_dict["move"] * len_nation_list
            ]

            result_name_list.remove(name_1)
            result_data_list = list(np.sum([result_data_list, nation_data_list], axis=0))

            print("------------------------------------")
            print("{} {} 羁绊所需 {} 人物：".format(name_1, attr_type, len(result_name_list)), ",".join(result_name_list))
            print("国家羁绊激活 {} 个".format(len_nation_list))
            print("计算结果：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(result_data_list[0], result_data_list[1],
                                                                    result_data_list[2], result_data_list[3],
                                                                    result_data_list[4], result_data_list[5]))
            print("------------------------------------")
            print("羁绊贡献")
            for data in result_all_data_list:
                print("组合:{},贡献：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(data[0], data[1][0], data[1][1], data[1][2],
                                                                            data[1][3], data[1][4], data[1][5], ))
            print("------------------------------------")
            print("还可增加的属性根据武将职业自己搭配")
            print("包含2同名武将：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(30, 30, 30, 30, 30, 30))
            if len(result_name_list) < 10:
                print("包含3同名武将：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(50, 50, 50, 50, 50, 50))
            print("包含1国羁绊：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(30, 30, 30, 30, 30, 30))
            print("包含3攻武将：攻击：{},无双：{}".format(100, 50))
            print("包含3防武将：攻击：{},防御：{}".format(50, 100))
            print("包含3迅武将：攻击：{},气力：{}".format(50, 100))
            print("包含3射武将：攻击：{},无双：{},气力：{}".format(50, 50, 50))
            print("包含3特武将：攻击：{},无双：{},气力：{}".format(50, 50, 50))

            msg = {
                "result": "{} {} 羁绊所需 {} 人物：".format(name_1, attr_type, len(result_name_list)) + "，".join(
                    result_name_list),
                "data2": "国家羁绊激活 {} 个".format(len_nation_list),
                "data3": "计算结果：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(
                    result_data_list[0], result_data_list[1], result_data_list[2], result_data_list[3],
                    result_data_list[4],
                    result_data_list[5]
                ),
                "data4": all_data_list,
                "data5": "包含2同名武将：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(30, 30, 30, 30, 30, 30),
                "data6": "包含3同名武将：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(50, 50, 50, 50, 50, 50),
                "data7": "包含1国羁绊：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(30, 30, 30, 30, 30, 30),
                "data8": "包含3攻武将：攻击：{},无双：{}".format(100, 50),
                "data9": "包含3防武将：攻击：{},防御：{}".format(50, 100),
                "data10": "包含3迅武将：攻击：{},气力：{}".format(50, 100),
                "data11": "包含3射武将：攻击：{},无双：{},气力：{}".format(50, 50, 50),
                "data12": "包含3特武将：攻击：{},无双：{},气力：{}".format(50, 50, 50)
            }
        except:
            msg = {
                "result": "输入数据有误，重新计算吧"
            }

        return render(request, "GameTool/SanGuoRenWuJiBan.html", {"msg": msg})

    # def post(self, request):
    #     dir_root = BASE_DIR + '\\apps\\GameTool\\data\\'
    #
    #     df = pd.read_excel(dir_root + "sanguo_data.xlsx", sheet_name="全部羁绊")
    #
    #     name_1 = request.POST.get("name_1")  # 获取提交的武将姓名
    #
    #     attr_type = "atk"  # 这里选择一个优先选择属性项
    #
    #     # 遍历数据的时候的序号选择名字填充到列表
    #     def append_num_name(num):
    #         data = [df['name1'][num], df['name2'][num], df['name3'][num]]
    #         return data
    #
    #     # 遍历循环字典列表，按照人头贡献权重排序
    #     def order_w_list(attr_dict):
    #         order_list = []
    #         for k, v in attr_dict.items():
    #             order_list.append((k, v["order_w"], v["name_list"], v))
    #             # 按照优先选择order_w权重排序
    #             order_list = sorted(order_list, key=lambda x: x[1], reverse=True)
    #         return order_list
    #
    #     # 计算全部羁绊关联的武将且优先选择定位属性
    #     name_list = []
    #     sum_atk = 0
    #     sum_def = 0
    #     sum_HP = 0
    #     sum_war = 0
    #     sum_str = 0
    #     sum_move = 0
    #
    #     try:
    #         for i in range(len(df)):
    #             # 先遍历 name_1 优选，根据一个优先选择项排除无用的羁绊关联
    #             if name_1 in df['name1'][i] and df[attr_type][i] != 0:
    #                 name_list = name_list + append_num_name(i)
    #                 sum_atk = sum_atk + df['atk'][i]
    #                 sum_def = sum_def + df['def'][i]
    #                 sum_HP = sum_HP + df['HP'][i]
    #                 sum_war = sum_war + df['war'][i]
    #                 sum_str = sum_str + df['str'][i]
    #                 sum_move = sum_move + df['move'][i]
    #                 #         print(df["atk"][i],df["def"][i],df["HP"][i],df["war"][i],df["str"][i],df['move'][i])
    #             elif name_1 in df['name2'][i] and df[attr_type][i] != 0:
    #                 name_list = name_list + append_num_name(i)
    #                 sum_atk = sum_atk + df['atk'][i]
    #                 sum_def = sum_def + df['def'][i]
    #                 sum_HP = sum_HP + df['HP'][i]
    #                 sum_war = sum_war + df['war'][i]
    #                 sum_str = sum_str + df['str'][i]
    #                 sum_move = sum_move + df['move'][i]
    #                 #         print(df["atk"][i],df["def"][i],df["HP"][i],df["war"][i],df["str"][i],df['move'][i])
    #             elif name_1 in df['name3'][i] and df[attr_type][i] != 0:
    #                 name_list = name_list + append_num_name(i)
    #                 sum_atk = sum_atk + df['atk'][i]
    #                 sum_def = sum_def + df['def'][i]
    #                 sum_HP = sum_HP + df['HP'][i]
    #                 sum_war = sum_war + df['war'][i]
    #                 sum_str = sum_str + df['str'][i]
    #                 sum_move = sum_move + df['move'][i]
    #                 #         print(df["atk"][i],df["def"][i],df["HP"][i],df["war"][i],df["str"][i],df['move'][i])
    #
    #         # name1 武将列表去重、删除空白制表符
    #         name1_list = list(set(name_list))
    #         name1_list = [i for i in name1_list if i != '-']
    #         name1_list.remove(name_1)
    #         # name1_list
    #
    #         attr_dict = {}
    #         name_list_all = []
    #         # 循环附属属性的列表
    #         for name in name1_list:
    #             name_list_tmp = []
    #             sum_atk_tmp = 0
    #             sum_def_tmp = 0
    #             sum_HP_tmp = 0
    #             sum_war_tmp = 0
    #             sum_str_tmp = 0
    #             sum_move_tmp = 0
    #             for i in range(len(df)):
    #                 if name in df["name1"][i] or name in df["name2"][i] or name in df["name3"][i]:
    #                     name_list_tmp = name_list_tmp + append_num_name(i)
    #                     name_list_tmp = list(set(name_list_tmp))
    #                     name_list_tmp = [i for i in name_list_tmp if i != '-']
    #                     # 列表中删除优选的武将
    #                     name_list_tmp.remove(name)
    #
    #                     sum_atk_tmp = sum_atk_tmp + df['atk'][i]
    #                     sum_def_tmp = sum_def_tmp + df['def'][i]
    #                     sum_HP_tmp = sum_HP_tmp + df['HP'][i]
    #                     sum_war_tmp = sum_war_tmp + df['war'][i]
    #                     sum_str_tmp = sum_str_tmp + df['str'][i]
    #                     sum_move_tmp = sum_move_tmp + df['move'][i]
    #
    #                     attr_dict[name] = {
    #                         'atk': sum_atk_tmp,
    #                         'def': sum_def_tmp,
    #                         'HP': sum_HP_tmp,
    #                         'war': sum_war_tmp,
    #                         'str': sum_str_tmp,
    #                         'move': sum_move_tmp,
    #                         'name_list': name_list_tmp,
    #                         'order_w': sum_atk_tmp / (len(name_list) + 1)
    #                     }
    #
    #         # 按照权重排序
    #         arrt_list = order_w_list(attr_dict)
    #         # print(arrt_list)
    #
    #         name_name_list = []
    #         for i in arrt_list:
    #             name_name_temp = []
    #             if len(name_name_list + [i[0]] + i[2]) < 11:
    #                 name_name_list = name_name_list + [i[0]] + i[2]
    #                 name_name_list = list(set(name_name_list))
    #                 sum_atk = sum_atk + i[3]["atk"]
    #                 sum_def = sum_def + i[3]["def"]
    #                 sum_HP = sum_HP + i[3]["HP"]
    #                 sum_war = sum_war + i[3]["war"]
    #                 sum_str = sum_str + i[3]["str"]
    #                 sum_move = sum_move + i[3]["move"]
    #
    #         df_s = pd.read_excel(dir_root + "sanguo_data.xlsx", sheet_name="特殊羁绊")
    #         df_c = pd.read_excel(dir_root + "sanguo_data.xlsx", sheet_name="国家")
    #
    #         # 获取3同势力数据
    #         df_s_3_nation = df_s[df_s["data"] == "3同势力"]
    #         df_s_3_dict = df_s_3_nation.to_dict('records')[0]
    #
    #         # 将羁绊全部武将列入
    #         name_name_list = name_name_list + [name_1]
    #
    #         df_c_result = df_c[df_c['name'].isin(name_name_list)]
    #         df_c_result.reset_index(inplace=True, drop=True)
    #         # 统计国家频次list 计算3个同样国家的人物触发羁绊
    #         counter = Counter(df_c_result["nation"].to_list())
    #         nation_list = []
    #         for k, v in counter.items():
    #             if v > 2:
    #                 nation_list.append(k)
    #         len_nation_list = len(nation_list)
    #
    #         # 羁绊增加数值
    #         sum_atk = sum_atk + df_s_3_dict["atk"] * len_nation_list
    #         sum_def = sum_def + df_s_3_dict["def"] * len_nation_list
    #         sum_HP = sum_HP + df_s_3_dict["HP"] * len_nation_list
    #         sum_war = sum_war + df_s_3_dict["war"] * len_nation_list
    #         sum_str = sum_str + df_s_3_dict["str"] * len_nation_list
    #         sum_move = sum_move + df_s_3_dict["move"] * len_nation_list
    #
    #         name_name_list = list(set(name_name_list))
    #         name_name_list.remove(name_1)
    #
    #         print("所选武将：", name_1)
    #         print(
    #             "计算结果：攻击：{},防御：{},生命：{},无双：{},气力：{},移动：{}".format(sum_atk, sum_def, sum_HP, sum_war, sum_str, sum_move))
    #         print("羁绊所需 {} 人物：".format(len(name_name_list)), ",".join(name_name_list))
    #         print("包含3攻武将：攻击：{},无双：{},".format(100, 50))
    #         print("包含3防武将：攻击：{},防御：{}".format(50, 100))
    #         print("包含3迅武将：攻击：{},气力：{}".format(50, 100))
    #         print("包含3射武将：攻击：{},无双：{},气力：{}".format(50, 50, 50))
    #         print("包含3特武将：攻击：{},无双：{},气力：{}".format(50, 50, 50))
    #         msg = {
    #             "name_1": "所选武将：" + name_1,
    #             "result": "计算结果：攻击：{}，防御：{}，生命：{}，无双：{}，气力：{}，移动：{}".format(sum_atk, sum_def, sum_HP, sum_war, sum_str,
    #                                                                         sum_move),
    #             "jiban": "羁绊所需 {} 人物：".format(len(name_name_list)) + "，".join(name_name_list),
    #             "data1": "包含3攻武将：攻击：{},无双：{},".format(100, 50),
    #             "data2": "包含3防武将：攻击：{},防御：{}".format(50, 100),
    #             "data3": "包含3迅武将：攻击：{},气力：{}".format(50, 100),
    #             "data4": "包含3射武将：攻击：{},无双：{},气力：{}".format(50, 50, 50),
    #             "data5": "包含3特武将：攻击：{},无双：{},气力：{}".format(50, 50, 50)
    #         }
    #
    #     except:
    #         msg = {
    #             "result": "输入数据有误，重新计算吧"
    #         }
    #
    #     return render(request, "GameTool/SanGuoRenWuJiBan.html", {"msg": msg})
