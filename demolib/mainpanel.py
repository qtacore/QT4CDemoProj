# -*- coding: utf-8 -*-
'''
计算器主界面示例
'''

import qt4c.wincontrols as win
from qt4c.qpath import QPath

class MainPanel(win.Window):
    def __init__(self, app):
        # qp = QPath("/ClassName='CalcFrame' && Text='计算器' && Visible='True' && ProcessId='%s'" % app.ProcessId)
        qp = QPath("/ClassName='CalcFrame' && Text='计算器' && Visible='True'")
        super(MainPanel, self).__init__(locator=qp)
        self._app = app

        locators = {
            '按键0': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x82'")},
            '按键1': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x83'")},
            '按键2': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='CalcFrame' /ClassName='#32770' && Instance='1' /ClassName='Button' && Instance='10'")},
            '按键3': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x85'")},
            '按键4': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x86'")},
            '按键5': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x87'")},
            '按键6': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x88'")},
            '按键7': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x89'")},
            '按键8': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x8A'")},
            '按键9': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x8B'")},
            '按键.': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x54'")},
            'BackSpace': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x53'")},
            '清除': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x51'")},
            '除号': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x5B'")},
            '乘号': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x5C'")},
            '加号': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x5D'")},
            '减号': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x5E'")},
            '取反': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x50'")},
            '根号': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x6E'")},
            '倒数': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x72'")},
            '等号': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x79'")},
            '结果': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Static' && MaxDepth='3' && ControlId='0x96'")},

            # 科学型
            '度': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && Text='度'")},
            '弧度': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && Text='弧度'")},
            '梯度': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && Text='梯度'")},
            'pie': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x78'")},
            'sin': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x66'")},
            'cos': {'type': win.Control, 'root': self, 'locator': QPath("/ClassName='Button' && MaxDepth='3' && ControlId='0x67'")}

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