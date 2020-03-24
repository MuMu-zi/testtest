# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : case03.py
# @time   : 2020-03-06 18:51
# @Author : yangmuzi

import unittest
import requests

class Test_03(unittest.TestCase):

    def test_3(self):

        url = 'http://www.httpbin.org/post'
        data_dic = {'k1':'v1'}
        response = requests.post(url=url, data=data_dic)
        print(response.json())
        print('case3')

# if __name__ == '__main__':
#     unittest.main()
