#!/usr/bin/python3
#_*_coding:utf-8_*_


import tkinter
import re


def is_match(intv1, intv2, output_date):
    output_date.delete(0.0, tkinter.END)  # 清屏
    if not num:
        try:
            re_rueslt = re.match(intv1.get(), intv2.get()).group()  # 将窗口１和窗口２数据进行比较
        except:
            output_date.insert(1.0, '匹配失败！')
        else:
            output_date.insert(1.0, re_rueslt)
    else:
        try:
            re_rueslt = re.match(intv1.get(), intv2.get()).groups()
        except:
            output_date.insert(1.0, '匹配失败！')
        else:
            output_date.insert(1.0, re_rueslt)


def is_search(intv1, intv2, output_date):
    output_date.delete(0.0, tkinter.END)
    try:
        re_rueslt = re.search(intv1.get(), intv2.get()).group()
    except:
        output_date.insert(1.0, '匹配失败！')
    else:
        output_date.insert(1.0, re_rueslt)


def is_findall(intv1, intv2, output_date):
    output_date.delete(0.0, tkinter.END)
    try:
        re_rueslt = re.findall(intv1.get(), intv2.get())
    except:
        output_date.insert(1.0, '匹配失败！')
    else:
        output_date.insert(1.0, re_rueslt)
        print(re_rueslt)


def is_exit():
    exit()

    
def re_main():
	top = tkinter.Tk()
	top.title('正则匹配器')  # 设置标题
	top.geometry('515x175')  # 设置窗口大小
	# lab = tkinter.Label(top, text='匹配正则表达式内容', width=15, height=2) # 放置标签
	lab1 = tkinter.Label(top, text='正则表达式：').grid(row=1, column=0)
	lab2 = tkinter.Label(top, text='匹 配 内容：').grid(row=2, column=0)
	lab3 = tkinter.Label(top, text='匹 配 结果：').grid(row=3, column=0, rowspan=2, sticky=tkinter.S+tkinter.N)

	intv1 = tkinter.StringVar()
	input_date1 = tkinter.Entry(top, textvariable=intv1, width=35)
	input_date1.grid(row=1, column=1, sticky=tkinter.S+tkinter.N)  # 垂直方向拉伸，水平居中

	intv2 = tkinter.StringVar()
	input_date2 = tkinter.Entry(top, textvariable=intv2, width=35)
	input_date2.grid(row=2, column=1, sticky=tkinter.S+tkinter.N)  # 垂直方向拉伸，水平居中
	output_date = tkinter.Text(top, width=40, height=4)
	output_date.grid(row=3, column=1, rowspan=2, sticky=tkinter.S+tkinter.N)  # 跨越３行,垂直方向拉伸，水平居中
	button_match = tkinter.Button(top, text='match', width=15, height=2, command=lambda : is_match(intv1, intv2, output_date)).grid(row=1, column=2)  # 创建按钮，选定位置
	button_search = tkinter.Button(top, text='search', width=15, height=2, command=lambda : is_search(intv1, intv2, output_date)).grid(row=2, column=2)
	button_findall = tkinter.Button(top, text='findall', width=15, height=2, command=lambda : is_findall(intv1, intv2, output_date)).grid(row=3, column=2)
	button_end = tkinter.Button(top, text='exit', width=15, height=2, command=is_exit).grid(row=4, column=2)
	top.mainloop()


if __name__ == '__main__':
	re_main()
