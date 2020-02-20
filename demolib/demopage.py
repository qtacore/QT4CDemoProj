# -*- coding: utf-8 -*-
'''
百度登录页面示例
'''
from qt4c.webcontrols import XPath
from qt4c.webcontrols import WebPage, WebElement
import qt4c.wincontrols as wincontrols
from qt4w.webcontrols import InputElement, SelectElement

class DemoPage(WebPage):
    '''Demo页面
    '''
    ui_map = {
        'title': XPath('//div[@class="panel-heading"]'),
        'name': {'type': InputElement, 'locator': XPath('//input[@id="name"]')},
        'female': XPath('//input[@value="female"]'),
        'male': XPath('//input[@value="male"]'),
        'age': {'type': SelectElement, 'locator': XPath('//select[@id="age"]')},
        'company': {'type': InputElement, 'locator': XPath('//input[@id="company"]')},
        'submit': XPath('//button[@id="submit"]'),
    }

    def set_name(self, name):
        '''设置姓名
        '''
        self.control('name').value = name

    def set_female(self):
        '''设置性别为女性
        '''
        self.control('female').click()

    def set_male(self):
        '''设置性别为男性
        '''
        self.control('male').click()

    def set_age(self, age):
        '''设置年龄
        '''
        self.control('age').selection = age

    def set_company(self, company):
        '''设置公司名
        '''
        self.control('company').value = company

    def submit(self):
        '''提交
        '''
        self.control("submit").click()


class ProfilePage(WebPage):
    '''个人资料页
    '''
    ui_map = {
        '用户名': XPath('//div[@id="name"]'),
        '性别': XPath('//div[@id="sex"]'),
        '年龄': XPath('//div[@id="age"]'),
        '公司': XPath('//div[@id="company"]')
    }