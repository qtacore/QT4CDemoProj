# -*- coding: utf-8 -*-
'''
计算器主界面示例
'''

import qt4c.wincontrols as win
import qt4c.uiacontrols as uia
from qt4c.qpath import QPath

class UIAMainPanel(win.Window):
    def __init__(self, app):
        # qp = QPath("/ClassName='CalcFrame' && Text='计算器' && Visible='True' && ProcessId='%s'" % app.ProcessId)
        qp = QPath("/ClassName='CalcFrame' && Text='计算器' && Visible='True'")
        super(UIAMainPanel, self).__init__(locator=qp)
        self._app = app

        locators = {
            '按键0': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='0'")},
            '按键1': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='1'")},
            '按键2': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='2'")},
            '按键3': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='3'")},
            '按键4': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='4'")},
            '按键5': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='5'")},
            '按键6': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='6'")},
            '按键7': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='7'")},
            '按键8': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='8'")},
            '按键9': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='9'")},
            '按键.': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='十进制分隔符'")},
            'BackSpace': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='BackSpace 键'")},
            '清除': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='清除'")},
            '除号': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='除'")},
            '乘号': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='乘'")},
            '加号': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='加'")},
            '减号': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='减'")},
            '取反': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='求反'")},
            '根号': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='平方根'")},
            '倒数': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='倒数'")},
            '等号': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='等于'")},
            '结果': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Static' && MaxDepth='4' && Name='结果'")},

            # 科学型
            '度': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='度'")},
            '弧度': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='弧度'")},
            '梯度': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='梯度'")},
            'pie': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='圆周率'")},
            'sin': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='正弦'")},
            'cos': {'type': uia.Control, 'root': self, 'locator': QPath("/UIType='UIA' && ClassName='Button' && MaxDepth='4' && Name='余弦'")}

        }

        self.updateLocator(locators)

    def addNums(self, num1, num2):
        self.wait_for_exist(5, 0.2) 
        for i in str(num1):
            self.Controls[('按键%s' % i)].click()
        self.Controls['加号'].click()
        for i in str(num2):
            self.Controls[('按键%s' % i)].click()
        self.Controls['等号'].click()

    def minusNums(self, num1, num2):
        self.wait_for_exist(5, 0.2) 
        for i in str(num1):
            self.Controls[('按键%s' % i)].click()
        self.Controls['减号'].click()
        for i in str(num2):
            self.Controls[('按键%s' % i)].click()
        self.Controls['等号'].click()

    def multiNums(self, num1, num2):
        self.wait_for_exist(5, 0.2) 
        for i in str(num1):
            self.Controls[('按键%s' % i)].click()
        self.Controls['乘号'].click()
        for i in str(num2):
            self.Controls[('按键%s' % i)].click()
        self.Controls['等号'].click()

    def divideNums(self, num1, num2):
        self.wait_for_exist(5, 0.2) 
        for i in str(num1):
            self.Controls[('按键%s' % i)].click()
        self.Controls['除号'].click()
        for i in str(num2):
            self.Controls[('按键%s' % i)].click()
        self.Controls['等号'].click()

    def clearAll(self):
        self.Controls['清除'].click()

    def switchAngleType(self, angleType):
        self.Controls[angleType].click()
        
    def sin(self, x):
        self.wait_for_exist(5, 0.2)
        for i in str(x):
            self.Controls[('按键%s' % i)].click()
        self.Controls['sin'].click()

    def cos(self, x):
        self.wait_for_exist(5, 0.2)
        for i in str(x):
            self.Controls[('按键%s' % i)].click()
        self.Control['cos'].click()

    def switchScience(self):
        menu = win.Menu()
        for i in menu.MenuItems:
            if i.Text == '科学型(&S)\tAlt+2':
                i.click()
                break