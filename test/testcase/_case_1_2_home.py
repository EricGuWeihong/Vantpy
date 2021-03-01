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

    def test02_check_modules(self):
        c = Config()
        start_time = time()
        sfdc = SFDC_OCE_Page(self.driver)
        modules = c.get_case_data('home').get('modules')
        # print(modules)
        module_list = modules.split("|")
        print(module_list)
        sfdc.get_screent_img("SFDC_Modules")
        for tab in module_list:
            print(tab)
            tabtitle = sfdc.find_module(tab)
            if tab == tabtitle:
                continue
            else:
                self.assertEqual(tab, tabtitle)
        end_time = time()
        print("Elapse time: ", end_time - start_time)