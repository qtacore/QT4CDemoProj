# -*- coding: utf-8 -*-
'''
计算器App示例
'''

from qt4c.app import App

import subprocess, time

class CalcApp(App):
    '''计算器App(必须保证计算器不在"程序员型"下打开,否则打开失败)
    '''

    def __init__(self, cmd, params=[]):
        App.__init__(self)
        params.insert(0, cmd)
        self._process = subprocess.Popen(params, shell=True)
    
    @property
    def ProcessId(self):
        # win10下返回的pid是错误的
        return self._process.pid

    def quit(self):
        self._process.kill()
        App.quit(self) 