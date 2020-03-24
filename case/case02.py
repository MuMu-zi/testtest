# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : case02.py
# @time   : 2020-03-06 18:51
# @Author : yangmuzi
import unittest
import requests

'''
unittest框架的每个用例都是独立的，测试数据要共享的话，需要设置全局变量
可以使用globals()函数来解决
'''

class Test_02(unittest.TestCase):

    def setUp(self) -> None:
        self.g = globals()

    def test_1(self):
        result_a = '用例a的返回值'
        self.g['a'] = result_a      # 将用例1的值设置为全局变量
        self.assertEqual(result_a,'用例a的返回值')

    def test_2(self):
        b = globals()['a']      # 这块需要直接使用globals()
        self.assertEqual(b, '用例a的返回值')

    def test_3(self):
        b = self.g['a']
        result_b = b + '111'
        self.g[b] = result_b
        self.assertEqual(result_b, '用例a的返回值111')


if __name__ == '__main__':
    unittest.main()