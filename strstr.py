"""
#coding=utf8
（豆瓣2013面试题strstr） 有一个在给定字符串中查找子串的函数strstr， 该函数从给定的字符串src中查找substr并返回一个整数， 指明substr第一次出现的位置（从0开始计数），如果找不到则返回-1。
说明： 1、代码中不允许使用系统已有的库函数，所有用到的库函数都需要自己实现 2、允许使用任何编程语言，函数原型自行给定。
参考的C语言函数原型为 int strstr(char* src , char* substr)
"""


def strstr(string, substring):
    string_len = int(len(string))
    for i in range(string_len):
        k = i
        substring_len = int(len(substring))
        if string_len - k < substring_len:
            return -1
        j = 0
        while j < substring_len:
            if string[k] != substring[j]:
                break
            j += 1
            k += 1
        if j == substring_len:
            return i
    return -1



