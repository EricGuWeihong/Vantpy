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
from utils.generator import random_num
from time import time


class OCE(model):

    def test00_login_success(self):
        c = Config()
        username = c.get_case_data("login").get("msl-username")
        password = c.get_case_data("login").get("msl-password")

        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        sfdc.input_username(username)
        sfdc.input_password(password)
        sfdc.click_login_btn()
        sfdc.sleep(3)
        if sfdc.get_title() == '更改您的密码 | Salesforce':
            sfdc.click_cancel_chgpsw_btn()  # 取消修改密码
        print("News: ", sfdc.find_news())  # 等待通知消息加载完成
        end_time = time()

        sfdc.get_screent_img(__name__ + "_test00_login_success")
        print("Elapse time: ", end_time - start_time)
        self.assertEqual("主页 | Salesforce", sfdc.get_title())

    def test01_check_acct(self):
        # c = Config()
        # menu = c.get_case_data('home').get('menu')
        # menu_list = sorted(menu.split("|"))

        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        target_text = sfdc.open_acct_tab()
        print("Tab Title: ", target_text)
        end_time = time()

        sfdc.get_screent_img(__name__ + "_test01_check_acct")
        print("Elapse time: ", end_time - start_time)
        self.assertEqual("所有客户", target_text)

    def test02_check_acct_type(self):
        c = Config()
        acct_type_list = c.get_case_data("acct").get("type").split("|")
        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        target_list = sfdc.get_acct_types()
        print("Acct Types:", target_list)
        end_time = time()

        sfdc.get_screent_img(__name__ + "_test02_check_acct_type")
        print("Elapse time: ", end_time - start_time)
        self.assertListEqual(sorted(acct_type_list), sorted(target_list))

    def test03_check_view(self):
        c = Config()
        acct_view_list = c.get_case_data("acct").get("view").split("|")
        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        target_list = sfdc.get_acct_view()
        print("Acct View:", target_list)
        end_time = time()

        sfdc.get_screent_img(__name__ + "_test03_check_view")
        print("Elapse time: ", end_time - start_time)
        # self.assertListEqual(sorted(acct_view_list), sorted(target_list))  # 列表完全一致
        for view in acct_view_list:  # 测试列表包含即可
            self.assertIn(view, target_list)

    def test04_check_hco(self):
        c = Config()
        hco_tab_list = c.get_case_data("acct").get("tab").split("|")
        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        sfdc.switch_to_hco()
        seq_no = random_num(1)   # 随机数0-9
        hco_name = sfdc.click_hco_name(seq_no)  # 选择列表的HCO打开，可指定医院名
        print("Acct: No. %d - %s" % (seq_no, hco_name))
        sfdc.wait_for_loading()
        # self.assertIn(hco_name, sfdc.get_title())

        target_list = sfdc.get_hco_tab_list()
        print("Acct Tab:", target_list)
        end_time = time()

        sfdc.get_screent_img(__name__ + "_test04_check_hco")
        print("Elapse time: ", end_time - start_time)
        for tab in hco_tab_list:
            self.assertIn(tab, target_list)

    def test05_check_hco_detail(self):
        c = Config()
        hco_detail_field_list = c.get_case_data("acct").get("detail").split("|")
        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        sfdc.switch_to_default()
        target_list = sfdc.get_detail_field()
        print("Detail fields:", target_list)
        end_time = time()

        sfdc.get_screent_img(__name__ + "_test05_check_hco_detail")
        print("Elapse time: ", end_time - start_time)
        for field in hco_detail_field_list:
            self.assertIn(field, target_list)

    def test06_check_hco_associate(self):
        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        sfdc.switch_to_associate()
        sfdc.sleep(3)
        end_time = time()
        sfdc.get_screent_img(__name__ + "_test06_check_hco_associate")
        print("Elapse time: ", end_time - start_time)

    def test07_check_hco_history(self):
        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        sfdc.switch_to_history()
        sfdc.sleep(3)
        end_time = time()
        sfdc.get_screent_img(__name__ + "_test07_check_hco_history")
        print("Elapse time: ", end_time - start_time)

    def test08_check_hco_related(self):
        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        sfdc.switch_to_related()
        sfdc.sleep(3)
        end_time = time()
        sfdc.get_screent_img(__name__ + "_test08_check_hco_related")
        print("Elapse time: ", end_time - start_time)







