# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : run.py
# @time   : 2020-03-05 18:16
# @Author : yangmuzi

import HTMLTestRunnerNew
import unittest
import os
import datetime, time
# from BSTestRunner import BSTestRunner

case_path = os.path.join(os.getcwd(), 'case')
# report_path = os.path.join(os.getcwd(),'report')

def all_case():
    discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='case*.py')
    return discover

# report_name = datetime.datetime.now().timestamp()     # 时间戳
# report_name = datetime.datetime.now()     # 当前时间
report_name = time.strftime("%Y-%m-%d %H:%M:%S")        # 年月日时分秒
report_title = '{} {}'.format(report_name,'测试报告')
report_des = '用例执行情况 '
report_path = './report/'
report_file = report_path + '{} {}'.format(report_name,'.html')


with open(report_file,'wb') as r:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=r,title=report_title,description=report_des)
    # runner = BSTestRunner(stream=r, title=report_title,description=report_des)
    runner.run(all_case())


'''
可参考：
https://blog.csdn.net/XingLongSKY/article/details/89309729
'''


