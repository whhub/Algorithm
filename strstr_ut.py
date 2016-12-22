"""
#coding=utf8
（豆瓣2013面试题strstr） 有一个在给定字符串中查找子串的函数strstr， 该函数从给定的字符串src中查找substr并返回一个整数， 指明substr第一次出现的位置（从0开始计数），如果找不到则返回-1。
说明： 1、代码中不允许使用系统已有的库函数，所有用到的库函数都需要自己实现 2、允许使用任何编程语言，函数原型自行给定。
参考的C语言函数原型为 int strstr(char* src , char* substr)
"""

from nose.tools import *


def strstr_test():
    #Assert