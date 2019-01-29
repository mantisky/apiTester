#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
功能：框架入口，配置路由
作者：陈晨
时间：20190129
"""
from flask import Flask, request
from apiRunner import testSuite

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome!'

#测试套件构建
@app.route('/createTestSuite', methods=['POST'])
def createTestSuite():
    print('create_form: ', request.form)
    return 'createTestSuite'

@app.route('/retrieveTestSuite', methods=['GET'])
def retrieveTestSuite():
    print('retrieve_args: ', request.args)
    return 'retrieveTestSuite'

@app.route('/updateTestSuite', methods=['POST'])
def updateTestSuite():
    return 'updateTestSuite'

@app.route('/deleteTestSuite', methods=['POST'])
def deleteTestSuite():
    return 'deleteTestSuite'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)