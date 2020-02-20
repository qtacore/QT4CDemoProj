# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2018/12/17 QTAF自动生成

from demolib.testcase import DemoTestCase
from demolib.calcapp import CalcApp
from demolib.mainpanel import MainPanel
from demolib.uiamainpanel import UIAMainPanel

from qt4c.keyboard import Keyboard

class QT4CHelloTest(DemoTestCase):
    '''QT4C示例测试用例
    '''
    owner = "barrymbxu"
    timeout = 10
    priority = DemoTestCase.EnumPriority.Normal
    status = DemoTestCase.EnumStatus.Design

    def pre_test(self):
        from qt4c.util import Process
        for i in Process.GetProcessesByName('calc.exe'):
            i.terminate()
    
    def run_test(self):
        #-----------------------------
        self.startStep("打开计算器")
        #-----------------------------
        calcApp = CalcApp('calc.exe')
        mainpanel = MainPanel(calcApp)
        mainpanel.bringForeground()
        #-----------------------------
        self.startStep("加法运算测试")
        #-----------------------------
        mainpanel.addNums(1, 2)
        self.assert_equal("检查运算结果", mainpanel.Controls['结果'].Text, '3')
        mainpanel.clearAll()
        #-----------------------------
        self.startStep("减法运算测试")
        #-----------------------------
        mainpanel.minusNums(40, 2)
        self.assert_equal("检查运算结果", mainpanel.Controls['结果'].Text, '38')
        mainpanel.clearAll()
        #-----------------------------
        self.startStep("切换科学型测试")
        #-----------------------------
        import time
        time.sleep(1)
        Keyboard.inputKeys("{ALT}")
        time.sleep(1)
        Keyboard.inputKeys("{ENTER}")
        mainpanel.switchScience()


        #-----------------------------
        self.startStep("科学型切换角度类型测试")
        #-----------------------------
        mainpanel.switchAngleType('弧度')
        mainpanel.sin('3.1415926535897932384626433832795')
        self.assert_equal("检查运算结果", mainpanel.Controls['结果'].Text, '1')
        mainpanel.clearAll()

        calcApp.quit()

class QT4CUIAHelloTest(DemoTestCase):
    '''QT4C UIA控件示例测试用例
    '''
    owner = "barrymbxu"
    timeout = 10
    priority = DemoTestCase.EnumPriority.Normal
    status = DemoTestCase.EnumStatus.Design

    def pre_test(self):
        from qt4c.util import Process
        for i in Process.GetProcessesByName('calc.exe'):
            i.terminate()
    
    def run_test(self):
        #-----------------------------
        self.startStep("Win7打开计算器")
        #-----------------------------
        calcApp = CalcApp('calc.exe')
        mainpanel = UIAMainPanel(calcApp)
        mainpanel.bringForeground()
        #-----------------------------
        self.startStep("加法运算测试")
        #-----------------------------
        mainpanel.addNums(1, 2)
        self.assert_equal("检查运算结果", mainpanel.Controls['结果'].Value, '3 ')   # 计算器uia控件返回的结果值最后会带一个空格
        mainpanel.clearAll()
        #-----------------------------
        self.startStep("减法运算测试")
        #-----------------------------
        mainpanel.minusNums(40, 2)
        self.assert_equal("检查运算结果", mainpanel.Controls['结果'].Value, '38 ')
        mainpanel.clearAll()
        #-----------------------------
        self.startStep("切换科学型测试")
        #-----------------------------
        import time
        time.sleep(1)
        Keyboard.inputKeys("{ALT}")
        time.sleep(1)
        Keyboard.inputKeys("{ENTER}")
        mainpanel.switchScience()


        #-----------------------------
        self.startStep("科学型切换角度类型测试")
        #-----------------------------
        mainpanel.switchAngleType('弧度')
        mainpanel.sin('3.1415926535897932384626433832795')
        self.assert_equal("检查运算结果", mainpanel.Controls['结果'].Value, '1 ')
        mainpanel.clearAll()

        calcApp.quit()
    
if __name__ == '__main__':
    QT4CHelloTest().debug_run()

