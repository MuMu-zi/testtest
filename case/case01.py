# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : case01.py
# @time   : 2020-03-05 21:13
# @Author : yangmuzi

import unittest
# from common.re_token import get_token
import requests,json

class Test_01(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.token = get_token()
    #     print('获取到的token：%s' % cls.token)

    def test_1(self):
        host = 'http://httpbin.org/'
        endpoint = 'get'
        url = ''.join([host,endpoint])
        req = requests.get(url)
        print(req.text)     # 返回数据
        print('case1')
    #
    #
    # def test_2(self):
    #     response = requests.request(method='get',url='http://www.httpbin.org/get')
    #     self.assertEqual(response.status_code, 200)
    #     a = response.json()
    #     # print(a)
    #     # self.assertEqual(a['origin'],'42.238.209.67',msg='失败')
    #     self.assertEqual(a['args'],{})   # 验证value为空

    #
    # def test_3(self):
    #     url = 'http://www.httpbin.org/post'
    #     data_dic = {'k1':'v1'}
    #     response = requests.post(url=url, data=data_dic)
    #     self.assertEqual(response.json()['url'], "http://www.httpbin.org/post")





#
# if __name__ == '__main__':
#     unittest.main()
# # 将单元测试模块变成可以运行的测试脚本

