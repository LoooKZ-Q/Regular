#!/usr/bin/python3.5
#_*_coding:utf-8_*_
import re
import os


def is_match():
    os.system('cls')
    print('-' * 15, '匹配模式', '-' * 15, )
    while True:
        re_set = input('请输入表达式:')
        re_set_str = input('输入匹配字符:')
        re_num = input('输入匹配分组:')
        if not len(re_num):
            try:
                re_rueslt = re.match(re_set, re_set_str).group()
            except:
                print('匹配失败!')
            else:
                print('匹配结果-->:', re_rueslt)
        else:
            try:
                re_rueslt = re.match(re_set, re_set_str).group(int(re_num))
            except:
                print('匹配失败!')
            else:
                print('匹配结果-->:', re_rueslt)
        print('--' * 20)


def is_search():
    os.system('cls')
    print('-' * 15, '搜索模式', '-' * 15, )
    while True:
        re_set = input('请输入表达式:')
        re_set_str = input('输入匹配字符:')
        try:
            re_result = re.search(re_set, re_set_str).group()
        except:
            print('匹配失败!')
        else:
            print('匹配结果-->:', re_result)
        print('--' * 20)


def is_findall():
    os.system('cls')
    print('-' * 15, '查找模式', '-' * 15, )
    while True:
        re_set = input('请输入表达式:')
        re_set_str = input('输入匹配字符:')
        try:
            re_result = re.findall(re_set, re_set_str)
        except:
            print('匹配失败!')
        else:
            print('匹配结果-->:', end='')
            for i in re_result:
                print(i, end='  ')
        print('\n', '--' * 20)


def run_main():
    os.system('cls')
    print('''
*******  正则筛选器  ******
*     ① match   匹配对象  *
*     ② search  搜索一个  *
*     ③ findall 搜索全部  *
***************************
        ''')
    num = input('请输入匹配选项:')
    if num == '1':
        is_match()
    elif num == '2':
        is_search()
    elif num == '3':
        is_findall()
    else:
        pass


if __name__ == '__main__':
    run_main()

