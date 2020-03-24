# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : case02.py
# @time   : 2020-03-06 18:51
# @Author : yangmuzi
import unittest
import requests

class Test_02(unittest.TestCase):

    def test_2(self):

        response = requests.request(method='get', url='http://www.httpbin.org/get')
        self.assertEqual(response.status_code, 200)
        a = response.json()
        # print(a)
        # self.assertEqual(a['origin'], '42.238.209.67', msg='失败')
        self.assertEqual(a['args'], {})  # 验证value为空
        print('case2')

# if __name__ == '__main__':
#     unittest.main()