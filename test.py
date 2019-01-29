#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
功能：访问对应接口，测试用
作者：陈晨
时间：20190129
"""
import requests

url = 'http://127.0.0.1:8080/createTestSuite'
method = 'POST'
data = {"name":'admin',"pwd":"123456"}

resp = requests.request(method, url, data=data)
print(resp.status_code)
print(resp.text)

if __name__ == "__main__":
    pass