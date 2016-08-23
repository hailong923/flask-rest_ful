#coding:utf-8
'''
Created on 2016-8-23

@author: hhl
'''


from flask_script import Shell, Manager
from worker import app

manager = Manager(app)

def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
    manager.run()
    