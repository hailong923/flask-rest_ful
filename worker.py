#coding:utf-8
'''
Created on 2016-8-23

@author: hhl
'''



from flask import Flask
from flask_restful import Api
# from flask.ext import restful
import sys
import os


sys = sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# def create_app():
#     app = Flask('main')
#     return app

app = Flask(__name__)
api = Api(app)



from app import views