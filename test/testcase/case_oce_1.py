#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import sys

sys.path.append('../')
from test.page.SFDC_OCE_Page import SFDC_OCE_Page
from test.testcase.model import *
from test.common.BrowserDriver import BrowserDriver
from utils.config import Config
from utils.generator import random_pystr
from time import time


class OCE(model):

    def test00_login_fail(self):
        c = Config()
        username = c.get_case_data('login').get('msl-username')
        password = random_pystr()  # 随机生成密码

        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        sfdc.input_username(username)
        sfdc.input_password(password)
        sfdc.click_login_btn()
        msg = sfdc.get_errmsg()
        print("Error Message:", msg)
        end_time = time()

        sfdc.get_screent_img(__name__ + "_test00_login_fail")
        print("Elapse time: ", end_time - start_time)
        self.assertIn("请检查您的用户名和密码", msg)

    def test01_login_success(self):
        c = Config()
        username = c.get_case_data('login').get('msl-username')
        password = c.get_case_data('login').get('msl-password')

        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        sfdc.input_username(username)
        sfdc.input_password(password)
        sfdc.click_login_btn()
        sfdc.sleep(3)
        if sfdc.get_title() == '更改您的密码 | Salesforce':
            sfdc.click_cancel_chgpsw_btn()  # 取消修改密码
        print("News: ", sfdc.find_news())
        end_time = time()

        sfdc.get_screent_img(__name__ + "_test01_login_success")
        print("Elapse time: ", end_time - start_time)
        self.assertEqual("主页 | Salesforce", sfdc.get_title())

    def test02_check_menu(self):
        c = Config()
        menu = c.get_case_data('home').get('menu')
        menu_list = sorted(menu.split("|"))

        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        # print(module_list)
        tab_list = sorted(sfdc.get_menus())
        # print(menu_list)
        end_time = time()

        sfdc.get_screent_img(__name__ + "_test02_check_menu")
        print("Elapse time: ", end_time - start_time)
        self.assertListEqual(menu_list, tab_list)

    def test03_check_home(self):
        c = Config()
        components = c.get_case_data('home').get('component')
        component_list = sorted(components.split("|"))

        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        tab_list = []
        if sfdc.find_news() is not None:
            tab_list.append("总部通知")
        tab_list = tab_list + sfdc.get_components()
        tab_list = sorted(tab_list)
        print(tab_list)
        end_time = time()

        sfdc.get_screent_img(__name__ + "_test03_check_home")
        print("Elapse time: ", end_time - start_time)
        self.assertListEqual(component_list, tab_list)
