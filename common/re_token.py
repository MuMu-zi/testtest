 # !/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : re_token.py
# @time   : 2020-03-05 19:31
# @Author : yangmuzi
import os
import yaml

cur = os.path.dirname(os.path.realpath(__file__))
# os.realpath(__file__) 当前文件名的路径，__file__文件名/文件的完整路径
# os.path.dirname() 获取当前路径的上一级路径

def get_tonke(yamlName='token.yml'):

    p = os.path.join(cur, yamlName)
    # os.path.join 连接两个或更多的路径名组件
    f = open(p)
    a = f.read()
    # 获取文件的所有内容
    t = yaml.load(a, Loader=yaml.FullLoader)
    # 读取yaml的文件内容
# https: // www.cnblogs.com / klb561 / p / 9326677.html
    f.close()
    return t["token"]

if __name__ == '__main__':
    print(get_tonke())