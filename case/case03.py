# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : case03.py
# @time   : 2020-03-06 18:51
# @Author : yangmuzi

import unittest
import requests

import requests
import unittest
from time import sleep

class Test_03(unittest.TestCase):
    def setUp(self):
       pass

    #正常查询长沙的天气，断言
    def test_weather_changsha(self):
        r=requests.get('http://t.weather.sojson.com/api/weather/city/101250101')
        result= r.json()

        #断言
        self.assertEqual(result['status'],200)
        self.assertIn('success', result['message'])
        self.assertEqual(result['cityInfo']['city'],'长沙市')
        #设置间隔时间，避免IP被封，这个接口本身有限制的
        sleep(3)

    # 不传city_code，断言
    def test_weather_no_reference(self):
        r=requests.get('http://t.weather.sojson.com/api/weather/city/')
        result=r.json()
        self.assertEqual(result['status'], 404)
        self.assertEqual(result['message'], 'Request resource not found.')
        sleep(3)

    #传入一个不存在的city_code，断言
    def test_weather_reference_error(self):
        r=requests.get('http://t.weather.sojson.com/api/weather/city/100250101')
        result = r.json()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], '获取失败')
        sleep(3)

if __name__ == '__main__':
    unittest.main()
