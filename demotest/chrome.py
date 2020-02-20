# -*- coding: utf-8 -*-
'''
Chrome Browser示例
'''

from qt4c.qpath import QPath
from qt4c.testcase import ClientTestCase
from demolib.demopage import DemoPage, ProfilePage
from qt4c.webcontrols import WebPage
from qt4w.browser import Browser
import time
   
class QT4CChromeTest(ClientTestCase):
    '''Chrome示例测试用例
    '''
    owner = "barrymbxu"
    status = ClientTestCase.EnumStatus.Ready
    timeout = 1
    priority = ClientTestCase.EnumPriority.Normal
    
    def run_test(self):
        #-----------------------------
        self.startStep("1. 打开Chrome浏览器")
        #-----------------------------
        Browser.register_browser('Chrome', 'browser.chrome.ChromeBrowser')
        Browser.register_browser('IE', 'browser.ie.IEBrowser') # 注册IE浏览器
        browser = Browser('Chrome')
        page = browser.open_url('https://qtacore.github.io/qt4w/demo.html', DemoPage)
        page._webview._window.Parent.maximize()
        # page.loginclick()

        #-----------------------------
        self.start_step('2. 设置信息并提交')
        #-----------------------------
        page.set_name("qta")
        page.set_female()
        page.set_age(str(20))
        page.set_company("tencent")
        page.submit()
        time.sleep(2) # 等待页面跳转

        #-----------------------------
        self.start_step('3. 检查页面跳转以及内容是否正确')
        #-----------------------------
        page = ProfilePage(page)
        self.assert_equal('检查页面标题', page.title, '欢迎您：qta女士')
        self.assert_equal('检查用户名', page.control('用户名').inner_text, 'qta')
        self.assert_equal('检查性别', page.control('性别').inner_text, '女')
        self.assert_equal('检查年龄', page.control('年龄').inner_text, '20')
        self.assert_equal('检查公司', page.control('公司').inner_text, 'tencent')

if __name__ == '__main__':
    QT4CChromeTest().debug_run()