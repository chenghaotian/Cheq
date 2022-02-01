# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import messagebox as mb
import app

"""
author: CHT(D BOY; 成昊天)
E-mail: dboycht@qq.com
Welcome to visit my gitee or github!
gitee: gitee.com/sky-eye
github: github.com/chenghaotian
Version: 0.11
Time: Jan.31 2022
Environment: python 3.9.0
Update Log:
$#%  0.11 
     !: Only four formulas are supported
     !: Only supports Chinese 
"""

# =======导入语言包=======
lang_list = []
for line in open("./files/language.txt", encoding="utf-8").readlines():
    lang_list.append(line.strip())
# =======窗口设置=========
w = tk.Tk()
w.title(string=lang_list[0])
w.geometry("600x300")
w.iconbitmap("./files/logo.ico")
w.resizable(False, False)


# =======主程序==========
def main():
    left = input_left_eq.get('0.0', 'end').strip()
    right = input_right_eq.get('0.0', 'end').strip()
    main_return = app.main(left, right)
    yn_w = main_return[1]
    main_return = main_return[0]
    # Windows New
    if yn_w[0]:
        main_new = []
        for ios in main_return:
            main_new.append(list(filter(lambda x: x != ";", ios.split(";"))))
        rus_list = []
        for a in main_new:
            rus_list.append(''.join(a))
        mb.showinfo(lang_list[10], lang_list[10] + "\n" + "\t".join(rus_list))
    else:
        if yn_w[1] == 0:
            mb.showerror(lang_list[11], lang_list[12])
        elif yn_w[1] == 1:
            mb.showerror(lang_list[11], lang_list[4])
        elif yn_w[1] == 2:
            mb.showerror(lang_list[11], lang_list[13])
        elif yn_w[1] == 3:
            mb.showerror(lang_list[11], lang_list[14])
        elif yn_w[1] == 4:
            mb.showerror(lang_list[11], lang_list[15])


# =======控件============
# 按钮
begin_button = tk.Button(w,
                         command=main,
                         text=lang_list[7],
                         bd=3,
                         relief=tk.RIDGE,
                         font=(lang_list[8], 32))
begin_button.place(x=450, y=200)

# 文本框
input_left_eq = tk.Text(w, width=35, height=1, font=("SimSun", 16))
input_left_eq.place(x=100, y=10)
input_right_eq = tk.Text(w, width=35, height=1, font=("SimSun", 16))
input_right_eq.place(x=100, y=90)

# 备注

w.mainloop()
