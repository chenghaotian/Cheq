# -*- coding:utf-8 -*-
import itertools

"""
Project: Chemical equation calculation
author: CHT(D BOY; 成昊天)
E-mail: dboycht@qq.com
Welcome to visit my gitee or github!
gitee: gitee.com/sky-eye
github: github.com/chenghaotian
Version: 0.12
Time: Feb.1 2022
Environment: python 3.9.0
Update Log:
$#%  0.11 
     !: Only four formulas are supported
     !: Only supports Chinese
$#%  0.12 
     !: Update About
"""

U_L = ["Q", "W", "E", "R", "T", "Y", "U", "I",
       "O", "P", "A", "S", "D", "F", "G", "H",
       "J", "K", "L", "Z", "X", "C", "V", "B",
       "N", "M", "q", "w", "e", "r", "t", "y",
       "u", "i", "o", "p", "a", "s", "d", "f",
       "g", "h", "j", "k", "l", "z", "x", "c",
       "v", "b", "n", "m", "1", "2", "3", "4",
       "5", "6", "7", "8", "9", "0", "+"]


def if_i(b):
    try:
        int(b)
    except ValueError:
        return False
    else:
        return True


def if_s(b):
    try:
        int(b)
    except ValueError:
        return True
    else:
        return False


def main(ld: str, rd: str):
    a, b, c, d = change_data(ld, rd)
    # TODO $%^%^ 配平
    l_n_k = []
    for q in a:
        for w in list(q.keys()):
            l_n_k.append(w)
    l_dict = {}
    # TODO l_dict = {"a":[{0: 2}, {0: 5, 1: 0}], "b" : [{0: 3}, {0: 0, 1: 1}]}
    for q in l_n_k:
        r = []
        # This is a bug
        a_j = {}
        for w in a:
            try:
                a_j[a.index(w)] = w[q]
            except KeyError:
                a_j[a.index(w)] = 0
        r.append(a_j)
        b_j = {}
        for w in b:
            try:
                b_j[b.index(w)] = w[q]
            except KeyError:
                b_j[b.index(w)] = 0
        r.append(b_j)
        l_dict[q] = r
    l_new = {}
    for oj in l_n_k:
        oi = []
        for io in l_dict[oj]:
            oi.append(list(io.values()))
        l_new[oj] = oi
    l_dict = l_new
    nu = "123456789"
    every_number = list(itertools.product(nu, repeat=int(len(a) + len(b))))

    # TODO af_dict = {"a":[[2], [5, 0]]}
    # TODO {a1}*[2]+{a2}*[5+0]
    # TODO {"a":{"l": "{a1}*[2]+{a2}*[5+0]"}}
    keys_dict = {}
    for k in l_n_k:
        # TODO l_k = [[2], [5, 0]]
        l_k = []
        for q in l_dict[k]:
            l_k.append(q)
        keys_dict[k] = l_k
    for qwer in every_number:
        # TODO qwer = (0, 0, 0)
        ok_list = list(";".join(qwer))
        error_num = 0
        for iuj in l_n_k:
            str_l = ""
            str_r = ""
            # TODO
            #  l_dict = {"a":[[2], [5, 0]], "b" : [[3], [0, 1]]}
            l_z = l_dict[iuj]
            l_l = l_z[0]
            l_r = l_z[1]
            # 拆开菲蒂尔数列(我自己起的)
            qwer_l = list(qwer[0: len(l_l)])
            qwer_r = list(qwer[len(l_l): len(l_l) + len(l_r)])
            for aij in range(0, len(qwer_l)):
                str_l = str_l + f"{l_l[aij]}*{qwer_l[aij]}" + "+"
            for aij in range(0, len(qwer_r)):
                str_r = str_r + f"{l_r[aij]}*{qwer_r[aij]}" + "+"
            str_l = str_l.strip("+")
            str_r = str_r.strip("+")
            if eval(str_l) != eval(str_r):
                error_num += 1
            else:
                pass
        if error_num == 0:
            return ok_list, [c, d]
        else:
            continue
    return ["0"], [False, 4]


# "KMnO₄", "O₂+MnO₂+K₂MnO₄" ->
# [{"K": 1, Mn:1, "O":4}, {**}]   同   是否有错   原因
def change_data(data_l: str, data_r: str):
    try:
        if data_l == "\n" or data_r == "\n":
            # 判断是否为空
            print("空的")
            return [], [], False, 0
        elif if_i(data_l[0]) or if_i(data_r[0]):
            # 判断是否为数字开头
            print("数字开头")
            return [], [], False, 2
        elif if_s(data_l[-1]) or if_s(data_r[-1]):
            # 判断是否为文字结尾
            print("文字结尾")
            return [], [], False, 2
        else:
            not_n = 0
            for a in data_l + data_r:
                if a not in U_L:
                    not_n += 1
                else:
                    not_n += 0
            if not_n >= 1:
                print("不支持的文字")
                return [], [], False, 2

            not_n = 0
            for la in range(0, int(len(data_l)) - 2):
                if data_l[la] != "+":
                    if if_i(data_l[la]) == if_i(data_l[la + 1]) == if_i(data_l[la + 2]):
                        not_n += 1
            for la in range(0, int(len(data_r)) - 2):
                if data_r[la] != "+":
                    if if_i(data_r[la]) == if_i(data_r[la + 1]) == if_i(data_r[la + 2]):
                        not_n += 1
            if not_n > 0:
                print("元素错误或数值过大")
                return [], [], False, 2

            # 文字转列表
            # -cut
            data_l = data_l.split("+")
            l_list = list(filter(lambda x: x != "+", data_l))
            data_r = data_r.split("+")
            r_list = list(filter(lambda x: x != "+", data_r))

            l_r = []
            r_r = []
            for cut_l in l_list:
                l_dict = {}
                l_k_list = []
                l_v_list = []
                jump = 0
                for a in range(0, len(cut_l)):
                    if jump == 0:
                        if if_s(cut_l[a]):
                            if if_s(cut_l[a + 1]):
                                l_k_list.append(cut_l[a:a + 1])
                                jump += 1
                            else:
                                l_k_list.append(cut_l[a])
                        else:
                            if a != len(cut_l) - 1:
                                if if_i(cut_l[a + 1]):
                                    l_v_list.append(cut_l[a:a + 1])
                                    jump += 1
                                else:
                                    l_v_list.append(cut_l[a])
                            else:
                                l_v_list.append(cut_l[a])
                    else:
                        jump = 0
                for a in range(0, len(l_k_list)):
                    l_dict[l_k_list[a]] = int(l_v_list[a])
                l_r.append(l_dict)

            for cut_r in r_list:
                r_dict = {}
                r_k_list = []
                r_v_list = []
                jump = 0
                for a in range(0, len(cut_r)):
                    if jump == 0:
                        if if_s(cut_r[a]):
                            if if_s(cut_r[a + 1]):
                                r_k_list.append(cut_r[a: a + 1])
                                jump += 1
                            else:
                                r_k_list.append(cut_r[a])
                        else:
                            if a != len(cut_r) - 1:
                                if if_i(cut_r[a + 1]):
                                    r_v_list.append(cut_r[a: a + 1])
                                    jump += 1
                                else:
                                    r_v_list.append(cut_r[a])
                            else:
                                r_v_list.append(cut_r[a])
                    else:
                        jump = 0
                for a in range(0, len(r_k_list)):
                    r_dict[r_k_list[a]] = int(r_v_list[a])
                r_r.append(r_dict)
            # 检查式子个数 -大于5
            if len(l_r) >= 5 or len(r_r) >= 5:
                return [], [], False, 3
            else:
                # 质量守恒
                key_l_list = []
                for mc in l_r:
                    key_l_list.append(list(mc.keys()))
                l_keys = []
                for a in key_l_list:
                    for b in a:
                        if b not in l_keys:
                            l_keys.append(b)
                        else:
                            pass

                key_r_list = []
                for mc in r_r:
                    key_r_list.append(list(mc.keys()))
                r_keys = []
                for a in key_r_list:
                    for b in a:
                        if b not in r_keys:
                            r_keys.append(b)
                        else:
                            pass
                for a in l_keys:
                    if a not in r_keys:
                        return [], [], False, 1
                for a in r_keys:
                    if a not in l_keys:
                        return [], [], False, 1
                return l_r, r_r, True, 0
    except IndexError:
        return [], [], False, 5


if __name__ == '__main__':
    print(change_data("a2b3", "a5+b1"))
