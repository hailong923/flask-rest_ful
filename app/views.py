#coding:utf-8
'''
Created on 2016-8-23

@author: hhl
'''


from worker import app,api
from flask import jsonify
from flask import request,redirect,render_template
from flask_restful import Resource, Api
from toolfunc import *

@app.route('/test')
def test():
    return 'ok'

# @add_api_resource('/v1/api/test')
@api.resource('/v1/api/test')
class ApiTest(Resource):
    
    def get(self):
        r = {}
        r['code'] = 0
        r['msg'] = 'ok'
        return jsonify(r)



@api.resource('/v1/api/test1')
class ApiNTest(Resource):
    
    def post(self):
        r = {}
        r['code'] = 0
        r['msg'] = 'you are right'
        return jsonify(r)
