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

# =======导入语言包=======
lang_list = []
for line in open("./files/language.txt", encoding="utf-8").readlines():
    lang_list.append(line.strip())
# =======窗口设置=========
w = tk.Tk()
w.title(string=lang_list[0])
w.geometry("600x310")
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
        elif yn_w[1] == 5:
            mb.showerror(lang_list[11], lang_list[3])


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
input_left_eq = tk.Text(w, width=35, height=2, font=("SimSun", 16))
input_left_eq.place(x=100, y=10)
input_right_eq = tk.Text(w, width=35, height=2, font=("SimSun", 16))
input_right_eq.place(x=100, y=90)

# 备注
label_left = tk.Label(w,
                      text=lang_list[1],
                      font=(lang_list[8], 12))
label_left.place(x=20, y=15)
label_right = tk.Label(w,
                       text=lang_list[2],
                       font=(lang_list[8], 12))
label_right.place(x=20, y=100)

label_warn = tk.Label(w,
                      text=lang_list[5],
                      font=(lang_list[8], 20),
                      fg="red")

label_warn.place(x=20, y=150)
label_warn2 = tk.Label(w,
                       text=lang_list[16],
                       font=(lang_list[8], 12),
                       fg="red")

label_warn2.place(x=20, y=180)
label_warn3 = tk.Label(w,
                       text=lang_list[17],
                       font=(lang_list[8], 12),
                       fg="red")

label_warn3.place(x=20, y=200)

about1 = tk.Label(w,
                  text=lang_list[18])
about2 = tk.Label(w,
                  text=lang_list[19])
about3 = tk.Label(w,
                  text=lang_list[20])
about4 = tk.Label(w,
                  text=lang_list[6])

about1.place(x=20, y=220)
about2.place(x=20, y=240)
about3.place(x=20, y=260)
about4.place(x=20, y=280)
w.mainloop()
