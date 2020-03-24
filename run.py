# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : run.py
# @time   : 2020-03-05 18:16
# @Author : yangmuzi

import HTMLTestRunnerNew
import unittest
import os
import datetime

case_path = os.path.join(os.getcwd(), 'case')
# report_path = os.path.join(os.getcwd(),'report')

def all_case():
    discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='case*.py')
    return discover

report_name = datetime.datetime.now().timestamp()
report_title = '{} {}'.format(report_name,'测试报告')
report_des = '测试报告详细描述 '
report_path = './report/'
report_file = report_path + 'report.html'

with open(report_file,'wb') as r:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=r,title=report_title,description=report_des)
    runner.run(all_case())





